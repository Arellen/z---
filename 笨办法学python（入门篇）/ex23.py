# ASCII 是为了将二进制变成数字和英文，8位数encoding 0-255，8位0和1的序列称为1byte,
# 为了存储更多的语言和字符，人们编写出通用编码 universal encoding
import sys
script, encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
# 9-11行是为了防止if语句一直循环下去，因为有可能遇到error ='strict'
# define a function named main there are three arguments

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    # DBES decode bytes, encode strings
    print(raw_bytes, "<===>", cooked_string)

languages = open("ex23_languages.txt", encoding="utf-8")

main(languages, encoding, error)