#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import operator
import sys

if __name__ == '__main__':

    lista = []

    for line in sys.stdin: 
        key, fecha, valor = line.split("\t")
        valor = int(valor)
        tupla = key, fecha, valor
        lista.append(tupla)
          
    sortedDict = sorted(lista, key=operator.itemgetter(0, 2))
    
    for linea in sortedDict:
        
        sys.stdout.write("{}   {}   {}\n".format(linea[0], linea[1], linea[2]))
