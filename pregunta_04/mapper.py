#
# >>> Escriba el codigo del mapper a partir de este punto <<<
import sys

if __name__ == '__main__':

    for row in sys.stdin:
        data= row.strip().split('   ')
        c1=data[0]

        sys.stdout.write(f'{c1}\t1\n')#
