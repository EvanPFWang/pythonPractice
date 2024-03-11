import torch
import numpy as np
import matplotlib.pyplot as plt

# Function to compute confidence interval
def compute_confidence_interval(estimates, confidence_level):
    lower_percentile = ((1.0 - confidence_level) / 2) * 100
    upper_percentile = (confidence_level + ((1.0 - confidence_level) / 2)) * 100
    lower_bound = np.percentile(estimates, lower_percentile)
    upper_bound = np.percentile(estimates, upper_percentile)
    return lower_bound, upper_bound

# Set the parameters
n = 100  # Number of random variables X_i
B_values = [500, 2000, 10000]  # Number of bootstrap samples
mu = 5.0  # Mean of the normal distribution
confidence_level = 0.95  # Confidence level for the intervals

# Initialize lists to store results
confidence_intervals = []
biases = []
variances = []
theta_hat_distributions = []

# Run simulations for different B values
for B in B_values:
    # Draw X_i ~ Normal(mu, 1)
    X = torch.normal(mu, 1, size=(B, n))

    # Compute sample mean x_bar_n
    x_bar_n = torch.mean(X, axis=1)

    # Compute the estimator theta_hat_n
    theta_hat_n = torch.exp(x_bar_n)

    # Collect the distribution of theta_hat_n
    theta_hat_distributions.append(theta_hat_n.numpy())

    # Compute the true parameter theta
    theta = torch.exp(torch.tensor(mu))

    # Compute the bias and variance of the estimator
    bias = torch.mean(theta_hat_n) - theta
    variance = torch.mean((theta_hat_n - torch.mean(theta_hat_n))**2)

    # Store bias and variance
    biases.append(bias.item())
    variances.append(variance.item())

    # Compute and store the confidence interval
    confidence_interval = compute_confidence_interval(theta_hat_n.numpy(), confidence_level)
    confidence_intervals.append(confidence_interval)

# Plot histogram of estimator theta_hat_n for each B value
plt.figure(figsize=(18, 6))
for i, B in enumerate(B_values):
    plt.subplot(1, len(B_values), i + 1)
    plt.hist(theta_hat_distributions[i], bins=50, density=True, color='blue', alpha=0.7,
             label=f'$B={B}$\nBias: {biases[i]:.4f}\nVariance: {variances[i]:.4f}\nCI: [{confidence_intervals[i][0]:.4f}, {confidence_intervals[i][1]:.4f}]')
    plt.axvline(theta.numpy(), color='red', linestyle='--', label='True $\\theta$')
    plt.title(f'Histogram of $\\hat{{\\theta}}_n$ with $n={n}$')
    plt.xlabel('$\\hat{\\theta}_n$')
    plt.ylabel('Density')
    plt.legend(loc='upper right')

plt.tight_layout()
plt.show()

# Output the confidence intervals
for i, B in enumerate(B_values):
    print(f"For B_{i+1} = {B}, the 95% confidence interval is approximately ({confidence_intervals[i][0]:.4f}, {confidence_intervals[i][1]:.4f}).")
