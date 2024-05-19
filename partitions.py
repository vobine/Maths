#! /usr/bin/env python3

from math import prod
from collections import Counter
from copy import copy

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

class Partition:
    def __init__(self, base=None, value=None):
        "Make a new Partition, modified to partition a larger integer."
        if None == base:
            # Root partition, 1, has only one part.
            self._mset = Counter()
            self._mset[1] = 1
        else:
            self._mset = copy(base.mset)
            if base.mset[value]:
                self._mset[value] -= 1
                self._mset[value + 1] += 1
            elif None == value:
                self._mset[1] += 1
            else:
                raise KeyError

        strings = []
        for kk in sorted(self._mset.keys()):
            if 1 > self._mset[kk]:
                # Invalid
                pass
            elif 1 < self._mset[kk]:
                strings.append('{0:d}({1:d})'.format(kk, self._mset[kk]))
            else:
                # Singleton
                strings.append('{0:d}'.format(kk))
        self._string = ' + '.join(strings)

        self._parent = self._right = self._left = None

    @property
    def string(self) -> str:
        "Get canonical, hashable string representation of Partition."
        return self._string

    @property
    def mset(self) -> Counter:
        "Get underlying multiset representation."
        return self._mset

if '__main__' == __name__:
    print(str(partitions(5)))
