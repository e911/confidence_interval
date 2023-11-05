import numpy as np

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

def sample_normal_clipped(N, sig, mu):
    samples = np.random.randn(N, 1) * sig + mu
    samples = np.clip(samples, 0, 1)
    clipped_N = np.sum((samples >= 0) & (samples <= 1))
    while clipped_N < N:
        additional_samples = np.random.randn(N - clipped_N, 1) * sig + mu
        additional_samples = np.clip(additional_samples, 0, 1)
        samples = np.concatenate((samples, additional_samples), axis=0)
        clipped_N = np.sum((samples >= 0) & (samples <= 1))
    return samples[:N]

def sample_bernoulli(N, theta):
    return np.double(np.random.rand(N, 1) < theta)

def sample_uniform_clipped(N, a, b):
    samples = a + (b - a) * np.random.rand(N, 1)
    samples = np.clip(samples, 0, 1)
    clipped_N = np.sum((samples >= 0) & (samples <= 1))
    while clipped_N < N:
        additional_samples = a + (b - a) * np.random.rand(N - clipped_N, 1)
        additional_samples = np.clip(additional_samples, 0, 1)
        samples = np.concatenate((samples, additional_samples), axis=0)
        clipped_N = np.sum((samples >= 0) & (samples <= 1))
    return samples[:N]


def ci_test(num):
    for alpha in [0.05, 0.25]:
        for N in [10, 100, 1000, 10000]:
            hits = 0
            for reps in range(10000):
                X = sample_normal_clipped(N, 1, 0)
                a, b = ci(X, num)
                Xbar = np.mean(X)
                if a <= Xbar <=b :
                    hits = hits + 1
                # print(Xbar-ep, Xbar+ep)
            print(f"{num} alpha: {alpha:.3f} N: {N:5d} frac missed: {1 - hits/10000:.3f}")


for i in range(1,11):
    print("For function:", i)
    ci_test(i)