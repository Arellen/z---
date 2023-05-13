import os
import shutil
import tkinter as tk
from tkinter import filedialog


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("文件夹备份工具")
        self.geometry("800x200")

        self.source_folder_label = tk.Label(self, text="选择需要备份的文件夹A:")
        self.source_folder_label.grid(row=0, column=0, padx=10, pady=10)

        self.source_folder_button = tk.Button(self, text="选择文件夹", command=self.select_source_folder)
        self.source_folder_button.grid(row=0, column=1)

        self.source_folder_path = tk.StringVar()
        self.source_folder_entry = tk.Entry(self, textvariable=self.source_folder_path, width=50)
        self.source_folder_entry.grid(row=0, column=2, padx=10)

        self.target_folder_label = tk.Label(self, text="选择存入的路径B:")
        self.target_folder_label.grid(row=1, column=0, padx=10, pady=10)

        self.target_folder_button = tk.Button(self, text="选择文件夹", command=self.select_target_folder)
        self.target_folder_button.grid(row=1, column=1)

        self.target_folder_path = tk.StringVar()
        self.target_folder_entry = tk.Entry(self, textvariable=self.target_folder_path, width=50)
        self.target_folder_entry.grid(row=1, column=2, padx=10)

        self.backup_button = tk.Button(self, text="立即备份", command=self.backup)
        self.backup_button.grid(row=2, column=1, pady=10)

    def select_source_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.source_folder_path.set(folder)

    def select_target_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.target_folder_path.set(folder)

    def backup(self):
        source = self.source_folder_path.get()
        target = self.target_folder_path.get()

        if not source or not target:
            return

        archive_name = os.path.basename(source) + "_" + self.generate_timestamp()
        archive_path = os.path.join(target, archive_name)

        shutil.make_archive(archive_path, 'zip', source)
        self.target_folder_path.set("备份完成!")

    @staticmethod
    def generate_timestamp():
        import time
        timestamp = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        return timestamp


def main():
    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    main()
