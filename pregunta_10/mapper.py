#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    for row in sys.stdin:
        campo = row.strip().split('\t')
        clave = campo[0]
        letr = campo[1]
        

        sys.stdout.write(f'{clave}\t{letr}\n')
