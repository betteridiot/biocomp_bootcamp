import sys

def main(arg1, arg2 = None):
    with open(arg1) as dat_file:
        for line in dat_file:
            if line.startswith('#'):
                continue
            line = line.strip().split(',')
            print('LINE\n',line)
        if isinstance(arg2, int):
            print('arg2\n', arg2**arg2)

if __name__ == '__main__':
    arg1 = sys.argv[1]
    try:
        arg2 = sys.argv[2]
    except:
        arg2 = None
    main(arg1, arg2)