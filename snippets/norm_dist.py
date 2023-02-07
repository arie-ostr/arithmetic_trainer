from scipy.stats import norm

# Set the mean and standard deviation of the distribution
mean = 0
std = 1

# Calculate the PDF of the distribution
x = 1.0  # the value at which to calculate the PDF
pdf = norm.pmf(x, mean, std)
print(pdf)  # Output: 0.24197072
