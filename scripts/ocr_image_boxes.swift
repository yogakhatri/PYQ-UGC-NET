#!/usr/bin/env swift

import Foundation
import Vision

func fail(_ message: String) -> Never {
    FileHandle.standardError.write((message + "\n").data(using: .utf8)!)
    exit(1)
}

guard CommandLine.arguments.count == 4 else {
    fail("Usage: ocr_image_boxes.swift IMAGE_DIRECTORY PAGE_PREFIX OUTPUT_JSONL")
}

let directory = URL(fileURLWithPath: CommandLine.arguments[1], isDirectory: true)
let prefix = CommandLine.arguments[2]
let outputURL = URL(fileURLWithPath: CommandLine.arguments[3])
let files = (try? FileManager.default.contentsOfDirectory(
    at: directory, includingPropertiesForKeys: nil,
    options: [.skipsHiddenFiles]
))?.filter { $0.lastPathComponent.hasPrefix(prefix) && $0.pathExtension.lowercased() == "png" }
  .sorted { $0.lastPathComponent < $1.lastPathComponent } ?? []
guard !files.isEmpty else { fail("No matching PNG files") }

FileManager.default.createFile(atPath: outputURL.path, contents: nil)
guard let output = try? FileHandle(forWritingTo: outputURL) else { fail("Cannot open output") }

for file in files {
    autoreleasepool {
        let basename = file.deletingPathExtension().lastPathComponent
        guard let page = Int(basename.split(separator: "-").last ?? "") else { return }
        let request = VNRecognizeTextRequest()
        request.recognitionLevel = .accurate
        request.usesLanguageCorrection = true
        request.recognitionLanguages = ["en-US"]
        request.minimumTextHeight = 0.004
        do { try VNImageRequestHandler(url: file).perform([request]) }
        catch {
            FileHandle.standardError.write(("OCR failed on page \(page): \(error)\n").data(using: .utf8)!)
            return
        }
        for observation in request.results ?? [] {
            guard let candidate = observation.topCandidates(1).first else { continue }
            let box = observation.boundingBox
            let row: [String: Any] = [
                "page": page, "text": candidate.string,
                "x": box.minX, "y": box.minY, "w": box.width, "h": box.height,
            ]
            let data = try! JSONSerialization.data(withJSONObject: row, options: [.sortedKeys])
            output.write(data)
            output.write("\n".data(using: .utf8)!)
        }
    }
}
try? output.close()
print("OCR completed for \(files.count) page images")
