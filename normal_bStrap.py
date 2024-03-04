import mathplotlib.plotly as plt
import torch
# number of random variables X_i




torch.set_default_dtype(torch.float64)

torch.manual_seed(59)#reproducability
n = 1000

# number of experiments Y_j = (X_1^*,...,X_n^*)
B = 10000

# probability of success which we hope to estimate
p = 0.7

# draw X_i ∼ Bernoulli(p)
X = torch.distributions.Bernoulli(p).sample(n)

# draw B sets of n random variables X_i^* from the empirical CDF
X_empirical = X[torch.randint(low=0, high=n-1,B)]

# compute T_{n,b} for sample mean T_n := sum(X_i^*)/n
T = 1/n *   X_empirical.sum(1)

# compute mean of T_{n,b}
T_mean = T.mean()

# compute bootstrap variance
#v_boot = sum((T .- T_mean).^2) / B

# compute true variance of sample mean T_n for comparison
v_true = p*(1-p) / n