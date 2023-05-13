import pandas as pd
import os
from tqdm import tqdm

# 在/Users/chenxukun/同步空间/3-华联电子/8-报价文件中创建一个total.xls
filename = "/Users/chenxukun/同步空间/3-华联电子/8-报价文件/total.xlsx"
writer = pd.ExcelWriter(filename)
writer._save()

# 读取所有sheet的指定列
excel_file = pd.ExcelFile('/Users/chenxukun/同步空间/3-华联电子/8-报价文件/ProductSalesSummary2022-2023.xlsx')
df_list = []
for sheet_name in excel_file.sheet_names:
    df = pd.read_excel(excel_file, sheet_name=sheet_name, usecols=[3, 4, 7, 8, 9, 13])
    month = sheet_name[-6:]
    df['月份'] = month
    df_list.append(df)

# 合并所有的数据到一个DataFrame
df_merged = pd.concat(df_list)
print(df_merged.columns)
# 删除D列包含"小计："和"合计："的行
df = df_merged[~df_merged["客户名称"].astype(str).str.contains("小计：|合计：|nan", na=False)]

# 保存到新的Excel文件
df.to_excel('/Users/chenxukun/同步空间/3-华联电子/8-报价文件/total.xlsx', index=False)

df = pd.read_excel('/Users/chenxukun/同步空间/3-华联电子/8-报价文件/total.xlsx')

# 获取客户名称列的所有唯一值
customer_names = df['客户名称'].unique()
path = "/Users/chenxukun/同步空间/3-华联电子/8-报价文件"
folder_name = "客户分类"
folder_path = os.path.join(path, folder_name)

if not os.path.exists(folder_path):
    os.mkdir(folder_path)
    print(f"Folder {folder_name} created successfully!")
else:
    print(f"Folder {folder_name} already exists.")

# 遍历每个客户名称，将相应的数据保存到一个新的Excel文件
for customer_name in tqdm(customer_names, total=len(customer_names)):
    # 从原DataFrame中选择客户名称为当前客户的行
    customer_data = df[df['客户名称'] == customer_name]
    
    # 创建一个新的ExcelWriter对象，并将数据保存到一个新的Excel文件
    filename = f'/Users/chenxukun/同步空间/3-华联电子/8-报价文件/客户分类/{customer_name}.xlsx'
    writer = pd.ExcelWriter(filename)
    customer_data.to_excel(writer, index=False, header=list(df.columns))
    writer._save()
    tqdm.write(f"{customer_name} done.")