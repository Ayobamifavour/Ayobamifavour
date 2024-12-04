import matplotlib.pyplot as plt

with_music = [304,257,174,214,69,317,387,47,157,0,332,308,317,286,236,299,206,278,188,43,0,0,0,0,0]
without_music = [292,270,47,288,324,292,364,316,287,75,282,149,274,319,213,3,324,2,128,219,94,164,0,0,0]

plt.plot(with_music, [0] * len(with_music), 'o', color='blue', label='With Music')
plt.plot(without_music, [1] * len(without_music), 'o', color='Black', label='Without Music')

plt.title('Growth with and without music')
plt.yticks([0,1], ['With music', 'Without music'])
plt.legend(loc='best')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

with_music = [304,257,174,214,69,317,387,47,157,0,332,308,317,286,236,299,206,278,188,43,0,0,0,0,0]
without_music = [292,270,47,288,324,292,364,316,287,75,282,149,274,319,213,3,324,2,128,219,94,164,0,0,0]

xpos = np.arange(len(with_music))

plt.hist(with_music, bins=10, edgecolor='blue', color='black', alpha=0.6, label='with music')
plt.hist(without_music, bins=10, edgecolor='blue', color='black', alpha=0.6, label='without music')
plt.title('Histogram of the growth with both music and without music')
plt.xlabel('Growth')
plt.ylabel('Frequency')
plt.legend(loc='best')
plt.show()