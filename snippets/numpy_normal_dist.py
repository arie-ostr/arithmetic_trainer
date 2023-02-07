import numpy as np
import matplotlib.pyplot as plt

np.random.seed(34)
data = np.random.normal(20,10,100)
plt.hist(data, bins=25,
          label='Original',density=True)

u = np.mean(data)
std_d = np.std(data)
t_data = (data - u) /std_d

plt.hist(t_data, bins=20,
          density=True)



plt.legend()
plt.show()