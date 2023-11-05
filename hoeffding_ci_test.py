from distribution import *
def hoeffding_ci_test():
    for alpha in [0.05, 0.25]:
        for N in [10, 1000, 10000]:
            hits = 0
            ep = np.sqrt(1 / (2 * N) * np.log(2 / alpha))
            for reps in range(10000):
                X = sample_bernoulli(N, 0.5)
                Xbar = np.mean(X)
                if np.abs(Xbar - 0.5) <= ep:
                    hits = hits + 1
                # print(Xbar-ep, Xbar+ep)
            print(f"alpha: {alpha:.3f} N: {N:5d} ep: {ep:.3f} frac missed: {1 - hits/10000:.3f}")
hoeffding_ci_test()