#import mathplotlib.plotly as plt
import torch
# number of random variables X_i




torch.set_default_dtype(torch.float64)

torch.manual_seed(59)#reproducability
n = 1000

# number of experiments Y_j = (X_1^*,...,X_n^*)
b = 10000

# probability of success which we hope to estimate
p = 0.7

# draw X_i ∼ Bernoulli(p)
rvX = torch.distributions.Bernoulli(p).sample((n,))
#print(rvX)

# draw B sets of n random variables X_i^* from the empirical CDF
rvX_empirical = rvX[torch.randint(0, n,(n,b))]
# T_1,1 ... T_1,b
# ...
# T_n, 1 ... T_n,b
#

# compute T_{n,b} for sample mean T_n,1...b := sum(X_i^*)/n
T = 1/n *   rvX_empirical.sum(0)

# compute mean of T_{n,b}
T_mean = T.mean()

v_boot  =   torch.mean((T   -   T_mean)**2)
v_true  =   p(1-p)/n
def norm_pdf(data, mean, std):

# compute bootstrap variance
#v_boot = sum((T .- T_mean).^2) / B

# compute true variance of sample mean T_n for comparison
v_true = p*(1-p) / n