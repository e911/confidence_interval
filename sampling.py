import numpy as np
from matplotlib import pyplot as plt

N = 10
num_samples = 100000

mean = []
variance = []
entropy = []

def estimate_entropy(X):
    damin = np.min(X)
    damax = np.max(X)
    bins = 25
    rez = (damax - damin) / bins
    hst, _ = np.histogram(X, bins=25,range=(damin, damax))
    hst = hst / len(X) / rez
    good = hst > 0
    h = -rez * np.sum(hst[good] * np.log(hst[good]))
    return h


for n in range(1, N + 1):
    Y_n = []
    for i in range(num_samples):
        X_i = np.random.uniform(-np.sqrt(3), np.sqrt(3), size=n)
        Y = np.sum(X_i) / np.sqrt(n)
        Y_n.append(Y)
    
    mean_i = np.mean(Y_n)
    variance_i = np.var(Y_n)
    mean.append(mean_i) 
    variance.append(variance_i)
    entropy.append(estimate_entropy(Y_n))

print(mean)
print(variance)
print(entropy)
plt.plot(range(1, N + 1), mean, marker='o', linestyle='-', label="Avg[Yn]")
plt.plot(range(1, N + 1), variance, marker='o', linestyle='-', label="Var[Yn]")
plt.plot(range(1, N + 1), entropy, marker='o', linestyle='-', label="Ent[Yn]")
plt.xlabel('Value of N')
plt.legend()
plt.show()
