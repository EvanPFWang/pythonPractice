import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

import matplotlib.pyplot as plt
import torch
# number of random variables X_i




torch.set_default_dtype(torch.float64)

torch.manual_seed(59)#reproducability
n = 1000

# number of experiments Y_j = (X_1^*,...,X_n^*)
b = 10000

# probability of success which we hope to estimate
p = 0.7

# draw X_i ∼ Bernoulli(p) observations
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

# compute bootstrap variance
v_boot  =   torch.mean((T   -   T_mean)**2)
v_true  =   p*(1-p)/n

def norm_pdf(data, mean, std):
    const   =   (1 / (std * torch.sqrt(torch.tensor(2 * torch.pi))))
    return const    *   torch.exp(-0.5 * ((data - mean) / std) ** 2)

standard_err    =   torch.sqrt(torch.tensor(v_true))
dom  =   torch.linspace(p-5*standard_err,p+5*standard_err,n)


v_boot_pdf = norm_pdf(dom,T_mean,torch.sqrt(v_boot))
v_true_pdf = norm_pdf(dom, T_mean,  torch.sqrt(torch.tensor(v_true)))


plt.figure(figsize  =   (12,9))
plt.title(f"n = {n}, B = {b}, True Var(T_n) = {v_true:.2e}, Bootstrap Var(T_n) = {v_boot:.2e}'")
plt.hist(T.numpy(), bins = 50, density = True,alpha    =   0.1, label  =   "Bootstrap Samples")
plt.plot(dom, v_boot_pdf, "b--",    label = "Boot Var PDF")
plt.plot(dom,v_true_pdf,"r--",  label = "True Var PDF")
plt.xlabel("Sample Mean")
plt.ylabel("Density")
plt.legend()
plt.show()











plt.plot(dom,v_true_pdf,label = "True Var PDF")