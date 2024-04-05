#! /usr/bin/env python3

from math import prod

def partitions(n: int) -> tuple:
    return tuple(pp for pp in partmax(n, n))

def prodmax(n:int) -> tuple:
    value = 0
    big = ()
    for part in partitions(n):
        partval = prod(part)
        if partval > value:
            value = partval
            big = part
    return big

def partmax(nn: int, mm: int) -> tuple:
    if mm < 1:
        return
    elif mm == 1:
        yield (1,) * nn
        return
    elif nn == mm:
        yield (nn,)
    for ii in range(mm, 0, -1):
        for jj in range(ii, nn, ii):
            prefix = (ii,) * (jj // ii)
            for subpart in partmax(nn-jj, min(nn-jj, ii-1)):
                yield prefix + subpart
        if nn > ii and nn % ii == 0:
            yield (ii,) * (nn // ii)

if '__main__' == __name__:
    print(str(partitions(5)))
