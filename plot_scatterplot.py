#!/usr/bin/env python

import numpy as np
import sys
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import random 

data1 = np.genfromtxt(sys.argv[1],dtype=str, delimiter='\t', usecols = (int(sys.argv[2])))
data2 = np.genfromtxt(sys.argv[3], dtype=str, delimiter='\t', usecols = (int(sys.argv[4])))


def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def is_nan(string):
        if str(string) == 'nan':
                return True
        else:
                return False

cleandata1 = []
cleandata2 = []
deltas = []
for i in range(0, len(data1)): 
        if isFloat(data1[i]) == True and is_nan(data1[i]) == False and isFloat(data2[i]) == True and is_nan(data2[i]) == False:
                cleandata1.append(float(data1[i]))
		cleandata2.append(float(data2[i]))
		deltas.append(abs(float(data1[i])-float(data2[i])))
print 'Sample of data1: ', cleandata1[0:10]
print 'Sample of data2: ', cleandata2[0:10]

rand1 = random.sample(cleandata1, len(cleandata1))

plt.scatter(cleandata1, cleandata2, c='blue')
plt.xlabel(sys.argv[1])
plt.ylabel(sys.argv[2])
plt.show()


plt.scatter(cleandata1, cleandata2, c='blue', label='real', alpha=0.2)
plt.scatter(rand1, cleandata2, c='orange', label='randomized', alpha=0.2)
plt.legend()
plt.xlabel(sys.argv[1])
plt.ylabel(sys.argv[2])
plt.show()

plt.hist(cleandata1)
plt.title(sys.argv[1])
plt.show()

plt.hist(cleandata2)
plt.title(sys.argv[2])
plt.show()


corr, p_value = pearsonr(cleandata1, cleandata2)

print 'Average delta: ', np.mean(deltas)
print 'Number of points: ', len(cleandata1)
print 'Pearson correlation: ', corr
print 'P-value: ', p_value

plt.hist(deltas)
plt.xlabel('Differences between data1 and data2')
plt.show()
