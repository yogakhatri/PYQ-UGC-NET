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
    fail("Usage: ocr_pdf_boxes.swift PDF [FIRST_PAGE] [LAST_PAGE] [SCALE] [OUTPUT_JSONL]")
}

let url = URL(fileURLWithPath: CommandLine.arguments[1])
guard let document = PDFDocument(url: url) else { fail("Could not open PDF") }
let first = max(1, CommandLine.arguments.count > 2 ? Int(CommandLine.arguments[2]) ?? 1 : 1)
let last = min(document.pageCount, CommandLine.arguments.count > 3 ? Int(CommandLine.arguments[3]) ?? document.pageCount : document.pageCount)
let scale = max(2.0, CommandLine.arguments.count > 4 ? Double(CommandLine.arguments[4]) ?? 3.0 : 3.0)
let outputURL = CommandLine.arguments.count > 5
    ? URL(fileURLWithPath: CommandLine.arguments[5])
    : nil
if let outputURL {
    FileManager.default.createFile(atPath: outputURL.path, contents: nil)
}
let outputHandle = outputURL.flatMap { try? FileHandle(forWritingTo: $0) }

func emit(_ line: String) {
    let data = (line + "\n").data(using: .utf8)!
    if let outputHandle { outputHandle.write(data) }
    else { FileHandle.standardOutput.write(data) }
}

for pageNumber in first...last {
    autoreleasepool {
        guard let page = document.page(at: pageNumber - 1) else { return }
        let bounds = page.bounds(for: .cropBox)
        let width = max(1, Int(Double(bounds.width) * scale))
        let height = max(1, Int(Double(bounds.height) * scale))
        guard let bitmap = NSBitmapImageRep(
            bitmapDataPlanes: nil, pixelsWide: width, pixelsHigh: height,
            bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true,
            isPlanar: false, colorSpaceName: .deviceRGB,
            bytesPerRow: 0, bitsPerPixel: 0
        ) else { fail("Could not allocate page bitmap") }
        bitmap.size = NSSize(width: bounds.width, height: bounds.height)
        guard let context = NSGraphicsContext(bitmapImageRep: bitmap) else { fail("No graphics context") }
        NSGraphicsContext.saveGraphicsState()
        NSGraphicsContext.current = context
        NSColor.white.setFill()
        NSRect(x: 0, y: 0, width: bounds.width, height: bounds.height).fill()
        page.draw(with: .cropBox, to: context.cgContext)
        context.flushGraphics()
        NSGraphicsContext.restoreGraphicsState()
        guard let image = bitmap.cgImage else { fail("No page image") }

        let request = VNRecognizeTextRequest()
        request.recognitionLevel = .accurate
        request.usesLanguageCorrection = true
        request.recognitionLanguages = ["en-US"]
        request.minimumTextHeight = 0.004
        do { try VNImageRequestHandler(cgImage: image).perform([request]) }
        catch {
            FileHandle.standardError.write(("OCR failed on page \(pageNumber): \(error)\n").data(using: .utf8)!)
            return
        }

        for observation in request.results ?? [] {
            guard let candidate = observation.topCandidates(1).first else { continue }
            let box = observation.boundingBox
            let row: [String: Any] = [
                "page": pageNumber, "text": candidate.string,
                "x": box.minX, "y": box.minY, "w": box.width, "h": box.height
            ]
            let data = try! JSONSerialization.data(withJSONObject: row, options: [.sortedKeys])
            emit(String(data: data, encoding: .utf8)!)
        }
    }
}
try? outputHandle?.close()
