import matplotlib.pyplot as plt

products = ['spinach','sausage','prawns','pineapple','mushroom']
y = [40,20,10,44,23]

plt.barh(products,y,0.5, color='blue')
plt.show()