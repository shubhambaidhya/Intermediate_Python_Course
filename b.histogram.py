# Its a type of data visualization as well that helps to analyze and view data 
 
import matplotlib.pyplot as plt 

# Help on function hist in module matplotlib.pyplot:
# hist(x, bins=NONE, range=NONE, density=FALSE, weights=NONE, cumulative=FALSE, bottom=NONE, 
# histtype= 'bar', align='mid', orientation='vertical', rwidth=NONE, log=FALSE, color=NONE, label=NONE, 
# stacked=FALSE, *, data=NONE, **kwargs)

# ---- example -----

values = [0, 0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
plt.hist(values, bins=3, orientation='horizontal')
plt.show()

# for easy understanding 
# Suppose we have exam marks of 10 students:

# 45, 50, 55, 60, 62, 65, 70, 75, 80, 85


# If we create bins:

# 40–50 → 2 students

# 50–60 → 2 students

# 60–70 → 3 students

# 70–80 → 2 students

# 80–90 → 1 student

# The histogram will show bars touching each other (no gaps).