import torch
import numpy as np
import matplotlib.pyplot as plt

# Set the parameters
n = 100  # Number of random variables X_i
B_1 =   500  # Number of experiments Y_j = (X_1^*,...,X_n^*)
B_2 =   2000
B_3 =   10000
mu = 5.0  # Mean of the normal distribution

# Draw X_i ~ Normal(mu, 1)
X   =   torch.normal(mu, 1, size=(B_1, n))
X_2 =   torch.normal(mu, 1, size=(B_2, n))
X_3 =   torch.normal(mu, 1, size=(B_3, n))

# Compute sample mean x_bar_n
x_bar_n     =   torch.mean(X, axis=1)
x_bar_n_2   =   torch.mean(X_2, axis=1)
x_bar_n_3   =   torch.mean(X_3, axis=1)

# Compute the estimator theta_hat_n
theta_hat_n = torch.exp(x_bar_n)
theta_hat_n = torch.exp(x_bar_n_2)
theta_hat_n = torch.exp(x_bar_n_3)


# Compute the true parameter theta
theta = torch.exp(torch.tensor(mu))

# Compute the bias and variance of the estimator
bias = torch.mean(theta_hat_n) - theta
variance = torch.mean((theta_hat_n - torch.mean(theta_hat_n))**2)
conf_int    =
bias_2 = torch.mean(theta_hat_n_2) - theta
variance_2 = torch.mean((theta_hat_n_2 - torch.mean(theta_hat_n_2))**2)
bias_3 = torch.mean(theta_hat_n_3) - theta
variance_3 = torch.mean((theta_hat_n_3 - torch.mean(theta_hat_n_3))**2)

# Print bias and variance
print(f"Bias: {bias:.4f}")
print(f"Variance: {variance:.4f}")


# Plot histogram of estimator theta_hat_n
plt.figure(figsize=(8, 6))
plt.hist(theta_hat_n.numpy(), bins=50, density=True, color='blue', alpha=0.7, label='Estimator $\\hat{\\theta}_n$')
plt.axvline(theta.numpy(), color='red', linestyle='--', label='True parameter $\\theta$')
plt.title(f'$n={n}, B={B_1}$ \n Bias: {bias:.4f}, Variance: {variance:.4f}')
plt.xlabel('$\\theta$')
plt.ylabel('Density')
plt.legend(loc='upper right')
plt.show()


print(f"Bias: {bias:.4f}")
print(f"Variance: {variance:.4f}")
print(f"Bias: {bias:.4f}")
print(f"Variance: {variance:.4f}")