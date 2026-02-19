# --- BASIC PLOT ---

import matplotlib.pyplot as plt

year = [1950, 1951, 1952, 1953,1954,1955]
pop= [2.538, 2.57, 2.62, 2.85,2.95,2.98]


plt.plot(year, pop)

# naming the axis
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projection')
plt.yticks([0,2,3,6,8,10],
            ['0','2B','4B','6B','8B','10B',])
plt.show()