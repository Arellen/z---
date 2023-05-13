import pandas as pd
import os
from tqdm import tqdm

# 在/Users/chenxukun/同步空间/3-华联电子/8-报价文件中创建一个total.xls
filename = "/Users/chenxukun/同步空间/3-华联电子/8-报价文件/ProductSalesSummary2023Q1.xlsx"
writer = pd.ExcelWriter(filename)
writer._save()

# 读取所有sheet的指定列
excel_file = pd.ExcelFile('/Users/chenxukun/同步空间/3-华联电子/8-报价文件/ProductSalesSummary2022-2023.xlsx')
df_list = []
for sheet_name in excel_file.sheet_names:
    if "2023" in sheet_name:
        df = pd.read_excel(excel_file, sheet_name=sheet_name, usecols=[3, 4, 7, 8, 9, 10, 11, 12, 13])
        df_list.append(df)
# for sheet_name in excel_file.sheet_names:
    # df = pd.read_excel(excel_file, sheet_name=sheet_name, usecols=[3, 4, 7, 8, 9, 10, 11, 12, 13])
    # df_list.append(df)

# 合并所有的数据到一个DataFrame
df_merged = pd.concat(df_list)
print(df_merged.columns)
# 删除D列包含"小计："和"合计："的行
df = df_merged[~df_merged["客户名称"].astype(str).str.contains("小计：|合计：|nan", na=False)]
df['毛利'] = df['销售收入'] - df['销售数量']*df['核算价']
# 保存到新的Excel文件
df.to_excel(filename, index=False)


# 读取原始文件
excel_file = pd.ExcelFile('/Users/chenxukun/同步空间/3-华联电子/8-报价文件/ProductSalesSummary2023Q1.xlsx')


# 读取原始数据
df = pd.read_excel('/Users/chenxukun/同步空间/3-华联电子/8-报价文件/ProductSalesSummary2023Q1.xlsx', sheet_name='Sheet1')

customer_names = df['客户名称'].unique()
# 按客户名称分组计算毛利率和销售收入总额
grouped = df.groupby(['客户名称'], as_index=False).agg({'毛利': 'sum', '销售收入': 'sum'})

# 计算毛利率
grouped['毛利率'] = grouped['毛利'] / grouped['销售收入']

# 重命名列名
grouped.columns = ['客户名称', '总毛利', '总销售收入', '毛利率']

# 将数据写入新的 sheet2
with pd.ExcelWriter('/Users/chenxukun/同步空间/3-华联电子/8-报价文件/ProductSalesSummary2023Q1.xlsx', mode='a', engine='openpyxl') as writer:
    grouped.to_excel(writer, sheet_name='sheet2', index=False)


