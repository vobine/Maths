#! /usr/bin/env python3

def partitions(n: int) -> tuple:
    return tuple(pp for pp in partmax(n, n))

def partmax(nn: int, mm: int) -> tuple:
    # yield min(mm, nn)
    # yield (mm,)
    if nn == mm:
        yield (nn,)
        mm -= 1
    for ii in range(mm, 1, -1):
        for jj in range(ii, nn, ii):
            prefix = (ii,) * (jj // ii)
            for subpart in partmax(nn - jj, min(nn - jj, ii - 1)):
                # print(nn, mm, ii, jj, prefix, subpart)
                yield prefix + subpart
    if mm > 0 and nn % mm == 0:
        yield (mm,) * (nn // mm)
    # if nn > 1:
    #    yield (1,) * nn

if '__main__' == __name__:
    print(str(partitions(5)))
