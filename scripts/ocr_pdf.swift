#!/usr/bin/env swift

import AppKit
import Foundation
import PDFKit
import Vision

func fail(_ message: String) -> Never {
    FileHandle.standardError.write((message + "\n").data(using: .utf8)!)
    exit(1)
}

guard CommandLine.arguments.count >= 2 else {
    fail("Usage: ocr_pdf.swift PDF [FIRST_PAGE] [LAST_PAGE]")
}

let pdfURL = URL(fileURLWithPath: CommandLine.arguments[1])
guard let document = PDFDocument(url: pdfURL) else {
    fail("Could not open \(pdfURL.path)")
}

let firstPage = max(1, CommandLine.arguments.count >= 3 ? Int(CommandLine.arguments[2]) ?? 1 : 1)
let requestedLast = CommandLine.arguments.count >= 4 ? Int(CommandLine.arguments[3]) ?? document.pageCount : document.pageCount
let lastPage = min(document.pageCount, requestedLast)

guard firstPage <= lastPage else {
    fail("Invalid page range \(firstPage)-\(lastPage) for a \(document.pageCount)-page PDF")
}

for pageNumber in firstPage...lastPage {
    autoreleasepool {
        guard let page = document.page(at: pageNumber - 1) else { return }
        let bounds = page.bounds(for: .cropBox)
        let scale: CGFloat = 2.0
        let width = max(1, Int(bounds.width * scale))
        let height = max(1, Int(bounds.height * scale))

        guard let bitmap = NSBitmapImageRep(
            bitmapDataPlanes: nil,
            pixelsWide: width,
            pixelsHigh: height,
            bitsPerSample: 8,
            samplesPerPixel: 4,
            hasAlpha: true,
            isPlanar: false,
            colorSpaceName: .deviceRGB,
            bytesPerRow: 0,
            bitsPerPixel: 0
        ) else {
            fail("Could not allocate bitmap for page \(pageNumber)")
        }

        bitmap.size = NSSize(width: bounds.width, height: bounds.height)
        guard let context = NSGraphicsContext(bitmapImageRep: bitmap) else {
            fail("Could not create drawing context for page \(pageNumber)")
        }

        NSGraphicsContext.saveGraphicsState()
        NSGraphicsContext.current = context
        NSColor.white.setFill()
        NSRect(x: 0, y: 0, width: bounds.width, height: bounds.height).fill()
        page.draw(with: .cropBox, to: context.cgContext)
        context.flushGraphics()
        NSGraphicsContext.restoreGraphicsState()

        guard let image = bitmap.cgImage else {
            fail("Could not create image for page \(pageNumber)")
        }

        let request = VNRecognizeTextRequest()
        request.recognitionLevel = .accurate
        request.usesLanguageCorrection = true
        request.recognitionLanguages = ["en-US"]
        request.minimumTextHeight = 0.006

        do {
            try VNImageRequestHandler(cgImage: image, options: [:]).perform([request])
        } catch {
            fail("OCR failed on page \(pageNumber): \(error)")
        }

        let observations = (request.results ?? []).sorted {
            if abs($0.boundingBox.maxY - $1.boundingBox.maxY) > 0.012 {
                return $0.boundingBox.maxY > $1.boundingBox.maxY
            }
            return $0.boundingBox.minX < $1.boundingBox.minX
        }
        let lines = observations.compactMap { $0.topCandidates(1).first?.string }

        print("\n===== PAGE \(pageNumber) =====\n")
        print(lines.joined(separator: "\n"))
    }
}
