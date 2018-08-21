import numpy.random as nr
import string

def gen_lab(n, m=1):
    nr.seed(0)
    '''generate a m number of n-length random labels from string.ascii_lowercase'''
    labels = []
    nr.seed(0)
    for i in range(m):
        out = nr.choice(list(string.ascii_lowercase), 2)
        labels.append(''.join(out))
    return labels