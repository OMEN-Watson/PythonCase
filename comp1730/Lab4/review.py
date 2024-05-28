myList=[1,2,3]
print(type(myList))
myList=[1,2+1,3*2]
# print(type(myList))
# print(myList)
# n=0

# myList=[1,2,3,'4']
# myList=[1,2,3]
# while n<len(myList):
#   print(myList[n])
#   n+=1
# print(sum(myList))
str="Immaterium"
testlist=list("Immaterium")
print(testlist)
# number=0
# for one in testlist:
#   number=max(number, testlist.count(one))
# print(number)
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import colors
from matplotlib.ticker import PercentFormatter

# Create a random number generator with a fixed seed for reproducibility
rng = np.random.default_rng(100)
N_points = 10
n_bins =5

# Generate two normal distributions
dist1 = rng.standard_normal(N_points)
dist2 = 0.4 * rng.standard_normal(N_points) + 5
dist1=[1,2,3,4,5,6,7,8,9,10]
fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

# We can set the number of bins with the *bins* keyword argument.
axs[0].hist(dist1, bins=n_bins)
# axs[1].hist(dist2, bins=n_bins)

plt.show()