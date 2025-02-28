import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--count', action="store_const", const=True, dest="count", default=False)
parser.add_argument('--num', action="store_const", const=True, dest="num", default=False)
parser.add_argument('--sort', action="store_const", const=True, dest="sort", default=False)
parser.add_argument('source', type=str)

try:
    args = parser.parse_args()
    file = [i.replace('\n', '') for i in open(args.source).readlines()]
    if args.sort:
        file = sorted(file)
    for i in range(len(file)):
        if args.num:
            file[i] = str(i) + ' ' + file[i]
        print(file[i])
    if args.count:
        print(f'rows count: {len(file)}')
except Exception:
    print('ERROR')
