import matplotlib.pyplot as plt

time_of_breath_held = [22.22,30.57,17.47,22.39,26.90,36.85,27.33,29.55,13.87,34.66,60.75,67.41,42.19,59.74,52.64,43.37,73.27,59.09,51.15,58.32]
plt.figure(figsize=(12,6))
plt.hist(time_of_breath_held, bins=10,color='blue', edgecolor='black')
plt.xlabel('Time of Breath Held')
plt.ylabel('Frequency')
plt.title('The histogram of breath held')
plt.show()

import matplotlib.pyplot as plt

male = [60.75,67.41,42.19,59.74,52.64,43.37,73.27,59.09,51.15,58.32]
female = [22.22,30.57,17.47,22.39,26.90,36.85,27.33,29.55,13.87,34.66]

plt.plot(male, [0] * len(male), 'o', label='Male', color='blue')
plt.plot(female, [1] * len(female), 'o', label='Female', color='black')

plt.title('Side by side plot of Time for breath held by gender')
plt.xlabel('Time of Breath held')
plt.yticks([0,1], ['Male', 'Female'])
plt.legend()
plt.show()