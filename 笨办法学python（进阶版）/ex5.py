import argparse

parser = argparse.ArgumentParser(description='cat')

parser.add_argument('input_file1', nargs="?", type= argparse.FileType('r'))
parser.add_argument('input_file2', nargs="?", type= argparse.FileType('r'), required=False)
parser.add_argument('--cat', dest='cat', action='append')
args = parser.parse_args()
print(args.cat(args.input_file1, args.input_file2))