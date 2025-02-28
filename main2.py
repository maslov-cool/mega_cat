import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--sort', action="store_const", const=True, dest="sort", default=False)
parser.add_argument('arg', nargs='*')

args = parser.parse_args()
dict_ = dict()
for i in args.arg:
    key, value = i.split('=')
    dict_[key] = value
if args.sort:
    for i in sorted(dict_.keys()):
        print(f'Key: {i}', f'Value: {dict_[i]}', sep='\t')
else:
    for i in dict_.keys():
        print(f'Key: {i}', f'Value: {dict_[i]}', sep='\t')
