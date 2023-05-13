import argparse
# ## 命令行处理

# 计算输入整数sum, substraction, multiple, divide，包含3个标志参数、3个选项参数和位置参数。

# ### 标志参数

# - `v` 或 `-verbose`：保留2位小数还是只保留整数
# - `q` 或 `-quiet`：是否识别通配符
# - `h` 或 `-help`：输出帮助信息并退出。

# ### 选项参数

# - `—sum` 或 `-sum`：参数求和。
# - `—sub` 或 `-substract`：参数相减，多参数时从第一个参数开始减，一直减到最后一个参数。
# - `—mul` 或 `-multiple`：指定输出文件的格式类型。
# - `—div`或`—divide`:参数相除，多参数时从第一个参数开始除，一直除到最后一个参数。

# ### 位置参数

# - `int`：输入的整数，或者带有通配符的整数。
parser = argparse.ArgumentParser(description='Process Integer')

# 添加positional argument
parser.add_argument('integers', 
                    metavar = 'N',
                    type = int, 
                    nargs='+',
                    help='111')
# 添加option，--sum
parser.add_argument('--sum',
                    dest='accumulate',
                    action='store_const',
                    const=sum,
                    default=max,
                    help='将参数相加,默认为最大值')

args = parser.parse_args()
print(args.accumulate(args.integers))

