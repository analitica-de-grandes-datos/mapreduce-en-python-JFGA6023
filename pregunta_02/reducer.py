#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    actkey = None
    total = 0
    max = 0

    for line in sys.stdin:

        key, val = line.split('\t')
        val = int(val)


        if key == actkey:
            if val > max:
                max = val
                total = val
            else:
                val = max 
                total = val
        else:
            if actkey is not None:
                sys.stdout.write('{}\t{}\n'.format(actkey, total))

            actkey = key
            total = val
            max = val

    sys.stdout.write("{}\t{}\n".format(actkey, total))
