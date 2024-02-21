# -*- coding: utf-8 -*-
"""proj.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MDhm38VcLQM_wY3r-oWW1SvmwLAQ7kH7
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("/content/Book 5.xlsx")
mean=df['temperature'].mean()
print(mean)
min=df['temperature'].min()
print(min)
max=df['temperature'].max()
print(max)
treshold=32
no_days=df[df['temperature']>treshold].shape[0]
print(no_days)
date=df['date']
temperature=df['temperature']
plt.plot(date,temperature,color='black',linewidth='1',marker='.',)
x=np.array([max,min])
p=df.loc[df['temperature'].idxmax(),'date']
m=df.loc[df['temperature'].idxmin(),'date']
y=np.array([p,m])
plt.scatter(y,x,color='red')
plt.show()