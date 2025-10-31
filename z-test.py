from scipy import stats
import numpy as np

# Example data:
# A company claims the average weight of their product is 500g.
# You take a sample of 30 products to test the claim.

population_mean = 500    # Claimed mean
sample = [490, 505, 498, 502, 495, 510, 499, 503, 497, 492,
          501, 507, 496, 494, 508, 493, 500, 504, 499, 506,
          495, 502, 498, 503, 497, 500, 501, 499, 496, 505]

sample_mean = np.mean(sample)
sample_std = np.std(sample, ddof=1)  # sample standard deviation
n = len(sample)

# Perform one-sample Z-test
z_score = (sample_mean - population_mean) / (sample_std / np.sqrt(n))

# Two-tailed p-value
p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))

print("Sample Mean:", sample_mean)
print("Z-Score:", z_score)
print("P-Value:", p_value)

# Interpretation
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference.")
else:
    print("Fail to reject the null hypothesis: No significant difference.")
