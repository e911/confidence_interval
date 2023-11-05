import numpy as np

def sample_uniform(N, a, b):
    return a + (b - a) * np.random.rand(N, 1)

def sample_normal(N, sig, mu):
    return np.random.randn(N, 1) * sig + mu

def sample_bernoulli(N, theta):
    return np.double(np.random.rand(N, 1) < theta)


