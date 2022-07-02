#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
from curses import keyname
import sys

if __name__ == '__main__':

    Keyname = None
    ttl = 0


    for line in sys.stdin:

        key, valor = line.split('\t')
        valor = int(valor)

        if key == Keyname:
            ttl += valor
        else:
            if Keyname is not None:
                
                sys.stdout.write('{},{}\n'.format(Keyname, ttl))

            Keyname = key
            ttl = valor   

    sys.stdout.write('{},{}\n'.format(Keyname, ttl))
