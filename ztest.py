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
numerator = 0
denominator = 0
s2p = 0
s2m1 = 0
s2m2 = 0
standarddeviation1 = 0
standarddeviation2 = 0
zvalue = 0

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
    x1count = []
    xmonth = []
    x2value = []
    x2mean = []
    x2xm = []
    x2xm2 = []
    x2count = []

    # Obtain data of specific column
    for row in reader:
        if (row[0] == ''):
            break
        else:
            if (row[5] == '2017'):
                x1count.append(row[4])
                if (row[6] == 'Yes'):
                    #if (row[1] == 'LVL'):
                        x1value.append(row[4])
            elif (row[5] == '2018'):
                x2count.append(row[4])
                if (row[6] == 'Yes'):
                    #if (row[1] == 'LVL'):
                        x2value.append(row[4])
            continue
counter1 = collections.Counter(x1value)
counter2 = collections.Counter(x2value)
x1mean = list(counter1.values())
x2mean = list(counter2.values())
for value in x1mean:
    x1meanvalue = x1meanvalue + value;
for value in x2mean:
    x2meanvalue = x2meanvalue + value;
x1meantotal = x1meanvalue/len(x1mean)
x2meantotal = x2meanvalue/len(x2mean)
print (x1meantotal)
print (x2meantotal)
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
standarddeviation1 = math.sqrt(samplevariance1)
standarddeviation2 = math.sqrt(samplevariance2)
print (standarddeviation1)
print (standarddeviation2)
print(len(x1value))
print(len(x2value))
numerator = x1meantotal-x2meantotal
denominator = math.sqrt(((standarddeviation1*standarddeviation1)/len(x1value)) + ((standarddeviation2*standarddeviation2)/len(x2value)))
zvalue = numerator/denominator
print (zvalue)