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
sumofsquare1 = 0
sumofsquare2 = 0
samplevariance1 = 0
samplevariance2 = 0
s2p = 0
s2m1 = 0
s2m2 = 0
tvalue = 0

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

    # Obtain data of specific column
    for row in reader:
        if (row[0] == ''):
            break
        else:
            if (row[5] == '2017'):
                if (row[6] == 'Yes'):
                    # bottom line can be commented to receive information for all libraries
                    if (row[1] == 'LVL'):
                        x1value.append(row[4])
            elif (row[5] == '2018'):
                if (row[6] == 'Yes'):
                    # bottom line can be commented to receive information for all libraries
                    if (row[1] == 'LVL'):
                        x2value.append(row[4])
            continue
counter1 = collections.Counter(x1value)
counter2 = collections.Counter(x2value)
x1mean = list(counter1.values())
xmonth = list(counter1.keys())
x2mean = list(counter2.values())
print (x1mean)
print (x2mean)
ply.plot(xmonth, x1mean, label = '2017')
ply.plot(xmonth, x2mean, label = '2018')
ply.legend()
ply.show()
for value in x1mean:
    x1meanvalue = x1meanvalue + value;
for value in x2mean:
    x2meanvalue = x2meanvalue + value;
x1meantotal = x1meanvalue/len(x1mean)
x2meantotal = x2meanvalue/len(x2mean)
print (x1meantotal)
print (x2meantotal)
# print (x2meanvalue/len(x2mean))
for value in x1mean:
    x1xm.append(value - x1meantotal)
for value in x2mean:
    x2xm.append(value - x2meantotal)
for value in x1xm:
    x1xm2.append(value*value)
for value in x2xm:
    x2xm2.append(value*value)
for value in x1xm2:
    sumofsquare1 = sumofsquare1 + value
for value in x2xm2:
    sumofsquare2 = sumofsquare2 + value
samplevariance1 = sumofsquare1/(len(x1mean)-1)
samplevariance2 = sumofsquare2/(len(x2mean)-1)
s2p = ((len(x1mean)/(len(x1mean)+len(x2mean))*samplevariance1))+((len(x1mean)/(len(x1mean)+len(x2mean))*samplevariance2))
s2m1 = s2p/len(x1mean)
s2m2 = s2p/len(x2mean)
tvalue = (x1meanvalue/len(x1mean) - x2meanvalue/len(x2mean))/math.sqrt(s2m1+s2m2)
print (tvalue)



