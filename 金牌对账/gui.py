import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import os

class App:
    def __init__(self, root, process_data_func):
        self.root = root
        self.process_data_func = process_data_func
        root.geometry("+%d+%d" % (root.winfo_screenwidth() // 2 - root.winfo_reqwidth() // 2,
                                 root.winfo_screenheight() // 2 - root.winfo_reqheight() // 2))

        # 创建年份选项
        self.year = tk.StringVar(root)
        self.year.set("2023")
        year_label = tk.Label(root, text="选择年份:")
        year_label.grid(row=0, column=0)
        year_entry = tk.Entry(root, textvariable=self.year)
        year_entry.grid(row=0, column=1)

        # 创建月份选项
        self.month = tk.StringVar(root)
        self.month.set("3")
        month_label = tk.Label(root, text="选择月份:")
        month_label.grid(row=1, column=0)
        month_entry = tk.Entry(root, textvariable=self.month)
        month_entry.grid(row=1, column=1)

        
        # 创建文件选择按钮
        self.file_path = tk.StringVar(root)
        file_label = tk.Label(root, text="选择文件:")
        file_label.grid(row=2, column=0)
        file_button = tk.Button(root, text="浏览", command=self.browse_file)
        file_button.grid(row=2, column=1)
        file_display = tk.Label(root, textvariable=self.file_path)
        file_display.grid(row=2, column=2)
        self.folder_path = tk.StringVar(root)

        # 创建sheet名称选项
        self.sheet_name = tk.StringVar(root)
        sheet_label = tk.Label(root, text="选择sheet:")
        sheet_label.grid(row=3, column=0)
        self.sheet_combobox = ttk.Combobox(root, textvariable=self.sheet_name)
        self.sheet_combobox.grid(row=3, column=1)

        # 创建开始数据处理按钮
        start_button = tk.Button(root, text="开始数据处理", command=self.process_data)
        start_button.grid(row=4, column=0, columnspan=2)

        # 创建进度条
        self.progress_var = tk.DoubleVar(root)
        self.progress_bar = ttk.Progressbar(root, variable=self.progress_var, maximum=100)
        self.progress_bar.grid(row=5, column=0, columnspan=2, sticky="ew")

        # 创建输出框
        self.output_text = tk.Text(root, wrap=tk.WORD, height=10)
        self.output_text.grid(row=6, column=0, columnspan=2)

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        self.file_path.set(file_path)
        folder_path = os.path.dirname(file_path)
        self.folder_path.set(folder_path)
        self.load_sheets(file_path)


    def load_sheets(self, file_path):
        if not file_path:
            return

        xls = pd.ExcelFile(file_path)
        sheets = xls.sheet_names
        self.sheet_combobox["values"] = sheets

    def process_data(self):
        year = int(self.year.get())
        month = int(self.month.get())
        file_path = self.file_path.get()
        sheet_name = self.sheet_name.get()
        folder_path = self.folder_path.get()
        self.process_data_func(year, month, file_path, sheet_name, folder_path, self.update_progress)

    def update_progress(self, progress, message):
        self.progress_var.set(progress)
        self.output_text.insert(tk.END, message)
        self.output_text.see(tk.END)
        self.root.update_idletasks()
