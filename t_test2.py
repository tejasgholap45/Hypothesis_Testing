from scipy import stats

# Example data: scores before and after training
before = [45, 50, 55, 60, 65, 70]
after = [48, 52, 58, 63, 68, 74]

# Perform paired t-test
t_stat, p_value = stats.ttest_rel(before, after)

print("T-statistic:", t_stat)
print("P-value:", p_value)

# Interpretation
if p_value < 0.05:
    print("Result: Training had a significant effect.")
else:
    print("Result: No significant change after training.")
