from distribution import *


theta = 0.5
def normal_ci_test():
    for alpha in [0.05, 0.25]:
        if alpha == 0.05:
            ep0 = 1.95996
        elif alpha == 0.25:
            ep0 = 1.150349
        for N in [10, 100, 1000, 100000]:
            hits = 0
            mean_ep = 0
            for reps in range(10000):
                X = sample_bernoulli(N, theta)
                Xbar = np.mean(X)
                sig = np.std(X)
                ep = sig*ep0/np.sqrt(N)
                mean_ep = mean_ep+ep/10000
                if np.abs(Xbar - theta) <= ep:
                    hits = hits + 1
                # print(Xbar-ep, Xbar+ep)
            print(f"alpha: {alpha:.3f} N: {N:5d} ep: {mean_ep:.3f} frac missed: {1 - hits/10000:.3f}")
normal_ci_test()