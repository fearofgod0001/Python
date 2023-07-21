import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]

y = [10, 20, 15, 30, 25]



plt.bar(x, y)



x_ticks_values = [1, 2, 3, 4, 5]  

x_ticks_labels = ['A', 'B', 'C', 'D', 'E'] 

plt.xticks(x_ticks_values, x_ticks_labels)



y_ticks_values = [0, 10, 20, 30, 40]

y_ticks_labels = ['0', '10', '20', '30', '40']  

plt.yticks(y_ticks_values, y_ticks_labels)



plt.show()





