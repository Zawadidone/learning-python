from sys import getrefcount
from matplotlib import pyplot as plt

string = "xyz"

refs = [getrefcount(x) for x in string]

y_pos = range(len(string))

plt.bar(y_pos, refs, align='center')

plt.xticks(y_pos, string)

# set label for x axis
plt.xlabel("letter")

# set label for y axis
plt.ylabel('sys.getrefcount(strings)')

plt.show()
