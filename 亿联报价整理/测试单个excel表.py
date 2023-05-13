import pandas as pd
import xlrd

# 读取指定sheet中指定列的内容
df = pd.read_excel('/Users/chenxukun/同步空间/3-华联电子/ZZ-ERP导出文件/ProductSalesDetail/ProductSalesDetail_202201.xls', 
                   sheet_name='ProductSalesDetail_202201', 
                   usecols=['D', 'E', 'H', 'I', 'J', 'N'], 
                   engine='xlrd')

print(df.head())  # 打印前5行数据
