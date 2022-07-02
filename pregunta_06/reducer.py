#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
from __future__ import division
from curses import keyname
import sys


if __name__ == '__main__':

    keyname = None
    max = 0
    min = 0
    

    for line in sys.stdin:
        
        key, valor = line.split("\t")
        val = float(valor)
              
        if key == keyname:
        
            if valor > max:
                max = valor
            else:
                valor = max

            if valor < min:
                min = valor
            else:
                valor = min

         
        else:
         
            if keyname is not None:

                sys.stdout.write("{}\t{}\t{}\n".format(keyname, max, min))

            keyname = key
            max = valor
            min = valor

    sys.stdout.write("{}\t{}\t{}\n".format(keyname, max, min))
