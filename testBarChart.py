import numpy as np
import matplotlib.pyplot as plt
import pylab

N = 3
ind = np.arange(N)  # the x locations for the groups
width = 0.27       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

yvals = [4, 9, 2]
rects1 = ax.bar(ind, yvals, width, color='r')
zvals = [1,2,3]
rects2 = ax.bar(ind+width, zvals, width, color='g')
kvals = [11,12,13]
rects3 = ax.bar(ind+width*2, kvals, width, color='b')

ax.set_ylabel('Scores')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('2011-Jan-4', '2011-Jan-5', '2011-Jan-6') )
ax.legend( (rects1[0], rects2[0], rects3[0]), ('y', 'z', 'k') )

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

#plt.show()
pylab.savefig('foo'+str(1)+'.png', bbox_inches='tight')

'''import numpy as np
from matplotlib import pyplot as plt

ind = np.arange(3)

a = [3,6,9]
b = [2,7,1]
c = [0,3,1]
d = [4,0,3]

p1 = plt.bar(ind, a, 1, color='#ff3333')
p2 = plt.bar(ind, b, 1, color='#33ff33', bottom=a)
p3 = plt.bar(ind, c, 1, color='#3333ff', bottom=[a[j] +b[j] for j in range(len(a))])
p4 = plt.bar(ind, d, 1, color='#33ffff', bottom=[a[j] +b[j] +c[j] for j in range(len(a))])

plt.show()

fig = plt.figure()

width = .35
ind = np.arange(len(OY))
plt.bar(ind, OY)
plt.xticks(ind + width / 2, OX)

fig.autofmt_xdate()

plt.savefig("figure.pdf")
'''