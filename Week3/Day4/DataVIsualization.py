import matplotlib.pyplot as plt

x = [1,2,3]
y=[1,3,7]
plt.plot(x,y)
plt.show()


""" 1. Line Plot Exercise:

Create a line plot for the function y = x^2 for x ranging from 0 to 10. Add appropriate labels and a title.

2. Bar Chart Exercise:

Visualize the sales of five products (e.g., Product A, Product B, etc.) in a bar chart. Customize the chart with different colors and patterns.

3. Histogram Exercise:

Generate a dataset of 500 random numbers following a normal distribution. Plot the histogram and experiment with different bin sizes and colors.

4. Pie Chart Exercise:

Create a pie chart showing the percentage distribution of time spent on different daily activities (e.g., work, sleep, leisure, exercise, etc.). Use custom colors and add a shadow effect. """

import numpy as np
x = np.linspace(0,10,1000)
y = x**2
""" fig2, ax1 = plt.subplots(x,y)


ax1.set_ylabel("y")
ax1.set_xlabel("x")
 """

products = ["Product A", "Product B", "Product C" ,"Product D" ,"Product E"]
values = [20, 35, 30, 15, 13]

fig2, ax2 = plt.bar(products, values)
ax2.set_.title('Fruit Sales Data')
ax2.set_.xlabel('Fruit')
ax2.set_.ylabel('Sales')




data = np.random.normal(0, 1, 1000)
plt.hist(data, bins=30, edgecolor='black')
plt.title("Histogram of Normally Distributed Data")
plt.xlabel("Value")
plt.ylabel("Frequency")


brands = ['Apple', 'Samsung', 'Huawei', 'Xiaomi', 'Others']
market_share = [40, 30, 15, 10, 5]

plt.pie(market_share, labels=brands, autopct='%1.1f%%')
plt.title('Smartphone Market Share 2023')
plt.show()
