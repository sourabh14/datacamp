# matplotlib demo
import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
'''
# line plot
# useful when x axis represents time
plt.plot(year, pop)

# point plot
plt.scatter(year, pop)

# scale the plot (by log)
plt.xscale('log')

# show plot
plt.show()

# Histogram
# arguments
# $1 - list of values 
# $2 - bins (values are divided into bins)
'''

values = [0, 0.6, 1.4, 1.6, 2.2, 2.5, 2.6, 3.2, 3.5, 3.9, 4.2, 6]
plt.hist(values, bins=3)
plt.show()