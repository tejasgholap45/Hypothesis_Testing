from scipy import stats

class_A = [88, 92, 85, 90, 87, 78, 85, 91]
class_B = [84, 79, 88, 92, 76, 81, 83, 77]

t_stat, p_value = stats.ttest_ind(class_A, class_B)

print("T-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("Result: Significant difference between the two classes.")
else:
    print("Result: No significant difference between the two classes.")
