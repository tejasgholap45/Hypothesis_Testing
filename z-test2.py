import math
from scipy.stats import norm

# Given data
population_mean = 170
population_std = 10
sample_mean = 173
sample_size = 50

# Step 1: Calculate Z-score
z = (sample_mean - population_mean) / (population_std / math.sqrt(sample_size))

# Step 2: Find p-value (right-tailed test)
p_value = 1 - norm.cdf(z)

# Step 3: Print results
print("Z-score:", round(z, 2))
print("P-value:", round(p_value, 4))

# Step 4: Check significance at alpha = 0.05
alpha = 0.05
if p_value < alpha:
    print("✅ Reject Null Hypothesis: Sample mean is significantly higher.")
else:
    print("❌ Fail to Reject Null Hypothesis: No significant difference.")