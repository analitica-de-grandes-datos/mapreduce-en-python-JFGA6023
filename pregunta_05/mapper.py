#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for row in sys.stdin:
    sys.stdout.write("{}\t1\n".format(row.split("   ")[1].split('-')[1]))
