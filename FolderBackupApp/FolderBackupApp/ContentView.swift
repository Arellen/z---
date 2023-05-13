
import SwiftUI
import ZIPFoundation
import Foundation

struct SandboxBookmark: Codable {
    let data: Data
}


struct ContentView: View {
    @State private var sourceFolderURL: URL?
    @State private var destinationFolderURL: URL?
    @State private var timer: Timer?
    @State private var selectedInterval: TimeInterval = 3600
    @State private var backupProgress: Double = 0.0

    var body: some View {
        VStack {
            Text("Folder Backup App")
                .font(.largeTitle)
                .padding(.bottom, 20)

            Button(action: {
                let openPanel = NSOpenPanel()
                openPanel.canChooseFiles = false
                openPanel.canChooseDirectories = true
                openPanel.allowsMultipleSelection = false
                
                if openPanel.runModal() == .OK {
                    sourceFolderURL = openPanel.url
                }
            }, label: {
                Text("选择需要备份的文件夹")
                    .padding()
                    .background(Color.blue)
                    .foregroundColor(.white)
                    .cornerRadius(10)
            })
            .padding(.bottom, 10)
            let task = Process()

            Button(action: {
                let openPanel = NSOpenPanel()
                openPanel.canChooseFiles = false
                openPanel.canChooseDirectories = true
                openPanel.allowsMultipleSelection = false
                
                if openPanel.runModal() == .OK {
                    destinationFolderURL = openPanel.url
                }
            }, label: {
                Text("选择储存备份文件的文件夹")
                    .padding()
                    .background(Color.blue)
                    .foregroundColor(.white)
                    .cornerRadius(10)
            })
            .padding(.bottom, 20)

            Button(action: {
                backupFolder(sourceFolderURL: sourceFolderURL, destinationFolderURL: destinationFolderURL)
            }, label: {
                Text("立即备份")
                    .padding()
                    .background(Color.green)
                    .foregroundColor(.white)
                    .cornerRadius(10)
            })
            .padding(.bottom, 20)

            Text("备份间隔时间")
                .font(.headline)
                .padding(.bottom, 10)

            Picker("", selection: $selectedInterval) {
                Text("1小时").tag(TimeInterval(3600))
                Text("2小时").tag(TimeInterval(7200))
                Text("12小时").tag(TimeInterval(43200))
                Text("24小时").tag(TimeInterval(86400))
            }
            .pickerStyle(MenuPickerStyle())
            .padding(.horizontal, 40)
            .onChange(of: selectedInterval) { newInterval in
                updateBackupInterval(newInterval: newInterval)
            }
            ProgressView("备份进度", value: backupProgress, total: 1.0)
                .padding()
        }
        .padding()
        .onAppear {
            updateBackupInterval(newInterval: selectedInterval)
        }
    }

   
    // ... 之前的函数 ...
    func scheduleFolderBackup(sourceFolderURL: URL, destinationFolderURL: URL, interval: TimeInterval) {
        // Restore the sandbox bookmark for the source folder
        if let bookmarkData = UserDefaults.standard.data(forKey: "sourceFolderBookmark") {
            if let url = restoreAccessForBookmark(bookmarkData) {
                self.timer = Timer.scheduledTimer(withTimeInterval: interval, repeats: true) { _ in
                    self.backupFolder(sourceFolderURL: url, destinationFolderURL: destinationFolderURL)
                }
                RunLoop.current.add(timer!, forMode: .common)
                return
            }
        }
    }

    func backupFolder(sourceFolderURL: URL?, destinationFolderURL: URL?) {
        guard let sourceFolderURL = sourceFolderURL, let destinationFolderURL = destinationFolderURL else {
            print("Source or destination folder URL is not set")
            return
        }

        let dateFormatter = DateFormatter()
        dateFormatter.dateFormat = "yyyyMMddHHmmss"
        let dateString = dateFormatter.string(from: Date())
        let backupFileName = "backup_\(dateString).zip"
        let backupFileURL = destinationFolderURL.appendingPathComponent(backupFileName)

        let fileManager = FileManager.default
        let coordinator = NSFileCoordinator(filePresenter: nil)

        coordinator.coordinate(readingItemAt: sourceFolderURL, options: .withoutChanges, error: nil) { readURL in
            do {
                let archive = Archive(url: backupFileURL, accessMode: .create)
                try fileManager.zipItem(at: readURL, to: backupFileURL)
                print("Successfully backed up folder to \(backupFileURL)")
            } catch {
                print("Error creating backup: \(error.localizedDescription)")
            }
        }
    }



    func getBookmarkForFolder(url: URL) -> Data? {
        do {
            let bookmark = try url.bookmarkData(options: .withSecurityScope, includingResourceValuesForKeys: nil, relativeTo: nil)
            return bookmark
        } catch {
            print("Error creating bookmark for URL: \(url), error: \(error.localizedDescription)")
            return nil
        }
    }
    
    func authorizeFolderAccess() {
        let openPanel = NSOpenPanel()
        openPanel.prompt = "授权"
        openPanel.canChooseFiles = false
        openPanel.canChooseDirectories = true
        openPanel.allowsMultipleSelection = false

        openPanel.begin { response in
            if response == .OK, let url = openPanel.url {
                let bookmark = getBookmarkForFolder(url: url)
                if let data = bookmark {
                    let sandboxBookmark = SandboxBookmark(data: data)
                    let data = try? NSKeyedArchiver.archivedData(withRootObject: sandboxBookmark, requiringSecureCoding: true)
                    UserDefaults.standard.set(data, forKey: "sourceFolderBookmark")
                } else {
                    print("Failed to get bookmark data for URL: \(url)")
                }

            }
        }
    }




    func restoreAccessForBookmark(_ bookmarkData: Data) -> URL? {
        var isStale = false
        do {
            let url = try URL(resolvingBookmarkData: bookmarkData, options: .withSecurityScope, relativeTo: nil, bookmarkDataIsStale: &isStale)
            if isStale {
                print("Bookmark is stale, unable to resolve URL")
                return nil
            }
            guard url.startAccessingSecurityScopedResource() else {
                print("Unable to access URL: \(url)")
                return nil
            }
            return url
        } catch {
            print("Error resolving bookmark data, error: \(error.localizedDescription)")
            return nil
        }
    }



    
    func updateBackupInterval(newInterval: TimeInterval) {
        timer?.invalidate()
        timer = Timer.scheduledTimer(withTimeInterval: newInterval, repeats: true) { _ in
            backupFolder(sourceFolderURL: sourceFolderURL, destinationFolderURL: destinationFolderURL)
        }
    }
}
