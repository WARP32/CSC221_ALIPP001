import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, cubes, s=40)

ax.set_title("Cubes", fontsize=24)
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Cube of Value', fontsize=12)

ax.tick_params(axis='both', labelsize=12)

plt.show()




x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title("Cubes", fontsize=24)
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Cube of Value', fontsize=12)

ax.tick_params(axis='both', labelsize=12)

plt.show()