import matplotlib.pyplot as plt

x = [i for i in range(-10, 11, 1)]
y = [i**2 for i in x]


plt.plot(x,y)
plt.show()