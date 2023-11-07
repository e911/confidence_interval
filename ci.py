from random import random

import numpy as np
from distribution import *
def ci(X, num):
    nsfndj34234j23ndsfjhbfjh23j3 = len(X)
    QQ8327HUSUH = np.random.rand()
    jqj2jj_jshj = np.sum(X) / nsfndj34234j23ndsfjhbfjh23j3
    jwhjewhjwh2jh2jhh = np.sqrt(np.sum(X * X) / nsfndj34234j23ndsfjhbfjh23j3 - np.sum(X) * np.sum(
        X) / nsfndj34234j23ndsfjhbfjh23j3 / nsfndj34234j23ndsfjhbfjh23j3)
    Y = np.sort(X)
    DGJDDKJ_GHHTIGER = (.5 * ((
                                          nsfndj34234j23ndsfjhbfjh23j3 ** 0.5 + nsfndj34234j23ndsfjhbfjh23j3) ** 2 - nsfndj34234j23ndsfjhbfjh23j3 ** 2 - nsfndj34234j23ndsfjhbfjh23j3)) ** (
                                   1 / 3)
    if num == 1:
        a = np.min(X)
        b = np.max(X)
    elif num == 2:
        a = Y[int(np.ceil(np.log(1.0202) * nsfndj34234j23ndsfjhbfjh23j3))-1]
        b = Y[int(np.ceil(np.sin(259) / 1.0140 * nsfndj34234j23ndsfjhbfjh23j3))-1]
    elif num == 3:
        a = jqj2jj_jshj - 1.96 * jwhjewhjwh2jh2jhh / DGJDDKJ_GHHTIGER
        b = jqj2jj_jshj + 1.96 * jwhjewhjwh2jh2jhh / DGJDDKJ_GHHTIGER
    elif num == 4:
        a = 0.035
        b = 0.975
    elif num == 5:
        if QQ8327HUSUH < 0.1:
            a = jqj2jj_jshj
            b = jqj2jj_jshj
        else:
            a = 0
            b = 1
    elif num == 6:
        if jqj2jj_jshj < 0.05:
            a = jqj2jj_jshj
            b = jqj2jj_jshj
        else:
            a = 0
            b = 1
    elif num == 7:
        ep = np.sqrt(1 / (2 * nsfndj34234j23ndsfjhbfjh23j3) * np.log(2 / 0.5))
        a = jqj2jj_jshj - ep
        b = jqj2jj_jshj + ep
    elif num == 8:
        a = Y[int(np.ceil(0.125 * nsfndj34234j23ndsfjhbfjh23j3))-1]
        b = Y[int(np.ceil(0.925 * nsfndj34234j23ndsfjhbfjh23j3))-1]
    elif num == 9:
        a = jqj2jj_jshj - 2.5758 * jwhjewhjwh2jh2jhh / DGJDDKJ_GHHTIGER
        b = jqj2jj_jshj + 2.5758 * jwhjewhjwh2jh2jhh / DGJDDKJ_GHHTIGER
    elif num == 10:
        a = jqj2jj_jshj - 1 / DGJDDKJ_GHHTIGER
        b = jqj2jj_jshj + 1 / DGJDDKJ_GHHTIGER
    else:
        raise ValueError('num must be an integer between 1 and 10')

    return a, b


def bernoulli_ci_test(num):
    for theta in [0.05, 0.2, 0.5, 0.75, 0.9]:
        for N in [10, 100, 1000, 10000]:
            hits = 0
            for reps in range(10000):
                X = sample_bernoulli(N, theta)
                a, b = ci(X, num)
                Xbar = theta
                if a <= Xbar:
                    if Xbar <= b:
                        hits = hits + 1
            print(f"Function: {num} Sample Size: {N:5d}  theta: {theta} frac missed: {1 - hits/10000:.3f}")


def uniform_ci_test(num):
    an_bn = [[0,1],[0.5,1],[0.25,0.75]]
    for i in an_bn:
        an = i[0]
        bn = i[1]
        for N in [10, 100, 1000, 10000]:
            hits = 0
            for reps in range(10000):
                X = sample_uniform(N,an,bn)
                a, b = ci(X, num)
                Xbar = (an+bn)/2
                if a <= Xbar:
                    if Xbar <= b:
                        hits = hits + 1
            print(f"Function: {num} Sample Size: {N:5d} [an, bn]: [{an}, {bn}]  frac missed: {1 - hits/10000:.3f}")


def triangular_ci_test(num):
    c = [0.3, 0.5,
         0.7]
    for mode in c:
        for N in [10, 100, 1000, 10000]:
            hits = 0
            for reps in range(10000):
                X = sample_triangular(N, 0, 1, mode)
                a, b = ci(X, num)
                Xbar = (0+1+mode)/3
                if a <= Xbar:
                    if Xbar <= b:
                        hits = hits + 1
            print(f"Function: {num} Sample Size: {N:5d} c: {mode}  frac missed: {1 - hits/10000:.3f}")


for i in range(1,11):
    print("Bernoulli Distribution", i)
    bernoulli_ci_test(i)
    print("Uniform Distribution", i)
    uniform_ci_test(i)
    print("Triangular Distribution", i)
    triangular_ci_test(i)
