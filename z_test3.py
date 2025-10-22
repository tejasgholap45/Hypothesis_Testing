import math
from scipy import stats

# Given data
population_mean = 170
sample_mean = 172
population_std = 5
sample_size = 30

# Step 1: Calculate Z-statistic
z = (sample_mean - population_mean) / (population_std / math.sqrt(sample_size))

# Step 2: Calculate p-value
p_value = 2 * (1 - stats.norm.cdf(abs(z)))  # two-tailed test

# Step 3: Print results
print("Z-score:", round(z, 2))
print("p-value:", round(p_value, 4))

# Step 4: Decision
alpha = 0.05
if p_value < alpha:
    print("Reject Null Hypothesis (significant difference)")
else:
    print("Fail to Reject Null Hypothesis (no significant difference)")
