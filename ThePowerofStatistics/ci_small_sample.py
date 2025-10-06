import scipy.stats as stats
import math


sample_size = 15
sample_mean = 430
sample_standard_deviation = 35
degrees_of_freedom = sample_size -1

confidence_level = 0.95
alpha = 1 - confidence_level
alpha_h = alpha/2

t_score = stats.t.ppf(1-alpha_h,degrees_of_freedom)

print(f"t_score: {t_score:.4f}")

se = sample_standard_deviation / (sample_size**(0.5))
print(f"The Standard Error is: {se:.4f}")

margin_of_error = t_score * se
print(f"The margin of error: {margin_of_error:.2f}")


ci_upper_limit = sample_mean + margin_of_error
ci_lower_limit = sample_mean - margin_of_error

print(f"95% CI: [{ci_lower_limit:.2f} : {ci_upper_limit:.2f}]")
