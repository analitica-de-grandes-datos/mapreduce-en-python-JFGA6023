#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    keyactual = None
    total = 0
    for line in sys.stdin:

        key, val = line.split('\t')
        val = int(val)

        if key == keyactual:
            total += val
        else:
            if keyactual is not None:
                sys.stdout.write('{}\t{}\n'.format(keyactual, total))

            keyactual = key
            total = val

    sys.stdout.write("{}\t{}\n".format(keyactual, total))
