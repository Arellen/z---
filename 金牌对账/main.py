import pandas as pd
from tqdm import tqdm
from process_3782data import process_3782data
import tkinter as tk
from gui import App




def process_data(year, month, file_path, sheet_name, folder_path, progress_callback):
    # 使用获取的年份、月份、文件路径和工作表名称执行数据处理逻辑
    year = year
    month = month
    file_path = file_path
    sheet_name = sheet_name
    folder_path = folder_path
    
    # 读取广州金之桔客户资料对照表.xlsx 文件
    control_file_path = f"{folder_path}/广州金之桔客户资料对照表.xlsx"
    control_df = pd.read_excel(control_file_path)
    
    # 使用 tqdm 循环执行 process_data
    for _, row in tqdm(control_df.iterrows(), total=len(control_df)):
        id = row.iloc[0]
        erp_code = row.iloc[4]
        if erp_code == 3780:
            # process_3780data(id, erp_code, year, month, folder_path, file_path, sheet_name)
            continue
        if erp_code == 3782:
            process_3782data(id, erp_code, year, month, folder_path, file_path, sheet_name)

        # 示范代码：
        import time

        for progress in range(0, 101, 10):
            time.sleep(0.5)
            progress_callback(progress, f"完成进度：{progress}%\n")

def main():
    root = tk.Tk()
    root.title("数据处理工具")
    app = App(root, process_data)
    root.mainloop()

if __name__ == "__main__":
    main()