import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Step 1: Simulate Z = X / Y
np.random.seed(42)  # For reproducibility
n_samples = 100  # Number of samples
sample_size = 25  # Sample size

means = []
medians = []

for _ in range(n_samples):
    X = np.random.normal(0, 1, sample_size)
    Y = np.random.normal(0, 1, sample_size)

    # Avoid division by zero by removing near-zero values of Y
    Y[Y == 0] = 1e-10  # Replace exact zeros with small value
    Z = X / Y  # Compute Z

    # Step 2: Compute mean and median
    means.append(np.mean(Z))
    medians.append(np.median(Z))

# Convert lists to arrays for easier manipulation
means = np.array(means)
medians = np.array(medians)

# Step 3: Plot distributions
plt.figure(figsize=(12, 6))

# Histogram for Means
plt.subplot(1, 2, 1)
plt.hist(means, bins=15, color='blue', alpha=0.7, density=True, label='Mean')
plt.title("Distribution of Means")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()

# Histogram for Medians
plt.subplot(1, 2, 2)
plt.hist(medians, bins=15, color='orange', alpha=0.7, density=True, label='Median')
plt.title("Distribution of Medians")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()

plt.tight_layout()
plt.show()

# Step 4: Compare Descriptive Statistics
mean_stats = {
    'Mean': np.mean(means),
    'Std Dev': np.std(means),
    'Skewness': stats.skew(means),
    'Kurtosis': stats.kurtosis(means)
}

median_stats = {
    'Mean': np.mean(medians),
    'Std Dev': np.std(medians),
    'Skewness': stats.skew(medians),
    'Kurtosis': stats.kurtosis(medians)
}

print("Descriptive Statistics for Means:")
for k, v in mean_stats.items():
    print(f"{k}: {v:.4f}")

print("\nDescriptive Statistics for Medians:")
for k, v in median_stats.items():
    print(f"{k}: {v:.4f}")
