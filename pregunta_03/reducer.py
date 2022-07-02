#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import operator
import sys

if __name__ == '__main__':

    dict = {}
    

    for line in sys.stdin:

        key, val = line.split('\t')
        val = int(val)
        dict[key] = val

    sDict = sorted(dict.items(), key = operator.itemgetter(1))
    for line in sDict:
              

        sys.stdout.write('{},{}\n'.format(line[0], line[1]))
