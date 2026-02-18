# --- To import matplotlib we need sub package pyplot ---

import matplotlib.pyplot as plt

#  creating a list as an example (insight on evolution of population)

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

#here the first argument represents the horizontal axis and the second argument represents the vertical axis 
# plt.plot(year, pop)

# to display the plot function 
# plt.show() 


#1. Scatter plot
plt.scatter(year, pop)
plt.show()