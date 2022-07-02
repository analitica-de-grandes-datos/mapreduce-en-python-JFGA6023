#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
from collections import defaultdict
import operator
from traceback import StackSummary

if __name__ == '__main__':

    Dict = defaultdict(list)

    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)
        Dict[key].append(val)

    for clave, lista in Dict.items():
        suma= round(sum(lista), 1)
        prom = sum(lista)/len(lista)

        valores = [clave, suma, prom]  
           
        sys.stdout.write("{}\t{}\t{}\n".format(valores[0], valores[1], valores[2]))
