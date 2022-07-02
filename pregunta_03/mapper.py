#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    for row in sys.stdin:
        clean = row.strip()
        ltr, num = clean.split(',')

        sys.stdout.write(f'{ltr}\t{num}\n')
