# CLI (command -Line -interface)
from argparse import ArgumentParser

args = ArgumentParser()

args.add_argument('name')
args.add_argument('age', type=int, nargs='?', default=0)
# args.parse_args('--test', type=int, nargs='?', default=0)

args = vars(args.parse_args())
print(args)

name = args['name']
age = args['age'] * 2

print(name, age)