import csv
import numpy as np
import pandas as pd
import scipy.stats as stats
import plotly.express as px
import matplotlib.pyplot as ply
import seaborn as sns
import collections
import math
from itertools import groupby

x1meanvalue = 0
x2meanvalue = 0
xymeanvalue = 0
xsquarevalue = 0
ysquarevalue = 0
sumofsquare1 = 0
sumofsquare2 = 0
samplevariance1 = 0
samplevariance2 = 0
s2p = 0
s2m1 = 0
s2m2 = 0
tvalue = 0
i = 0
j = 0
k = 0
count = 0
numerator = 0
denominator = 0
correlation = 0

with open('Work.csv', newline = '') as csvfile:
    reader = csv.reader(csvfile)
    unitNumber = []
    location = []
    date = []
    type = []
    month = []
    year = []

    x1value = []
    x1mean = []
    x1xm = []
    x1xm2 = []
    xmonth = []
    x2value = []
    x2mean = []
    x2xm = []
    x2xm2 = []
    xymean = []
    xsquaremean = []
    ysquaremean = []

    # Obtain data of specific column
    for row in reader:
        if (row[0] == ''):
            break
        else:
            if (row[5] == '2017'):
                if (row[6] == 'Yes'):
                    # bottom line can be commented to receive information for all libraries
                    #if (row[1] == 'LVL'):
                        x1value.append(row[4])
            elif (row[5] == '2018'):
                if (row[6] == 'Yes'):
                    # bottom line can be commented to receive information for all libraries
                    #if (row[1] == 'LVL'):
                        x2value.append(row[4])
            continue
counter1 = collections.Counter(x1value)
counter2 = collections.Counter(x2value)
x1mean = list(counter1.values())
x2mean = list(counter2.values())
print(x1mean)
print(x2mean)
for value in x1mean:
    x1meanvalue = x1meanvalue + value;
for value in x2mean:
    x2meanvalue = x2meanvalue + value;
while (i < len(x1mean)):
    xymean.append(x1mean[i] * x2mean[i])
    i = i + 1
while (j < len(x1mean)):
    xsquaremean.append(x1mean[j] * x1mean[j])
    j = j + 1
while (k < len(x1mean)):
    ysquaremean.append(x2mean[k] * x2mean[k])
    k = k + 1
    count = count + 1
for value in xymean:
    xymeanvalue = xymeanvalue + value;
for value in xsquaremean:
    xsquarevalue = xsquarevalue + value;
for value in ysquaremean:
    ysquarevalue = ysquarevalue + value;
print(xymean)
print(xsquaremean)
print(ysquaremean)
print(x1meanvalue)
print(x2meanvalue)
print(xymeanvalue)
print(xsquarevalue)
print(ysquarevalue)
print(count)

numerator = (count*xymeanvalue) - (x1meanvalue*x2meanvalue)
denominator = math.sqrt(((count*xsquarevalue) - (x1meanvalue*x1meanvalue))*((count*ysquarevalue) - (x2meanvalue*x2meanvalue)))
correlation = numerator/denominator
print (correlation)




