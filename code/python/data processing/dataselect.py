import json
import pandas as pd
import matplotlib.pyplot as plt
import math
import csv
import numpy as np
from builtins import dir

def regenerateTime(time):
    newtime=[]
    for k in range(len(time)):
        t=time[k].split(':')
        t[0]=int(t[0])
        t[1]=float(t[1])
#         t[2]=float(t[2])
        T=t[0]*3600+t[1]*60
        newtime.append(T)
    return newtime

xk=pd.read_csv('data2\data_xk.csv',encoding='latin1')
Aair=np.array([1009.33,1008.91,1009.68])
Bair=np.array([1009.85,1009.36,1010.07])
height=np.array([0.0,3.5,-3.5])
Ad=np.polyfit(Aair, height, 1)
Bd=np.polyfit(Bair, height, 1)
Aheight=[]
Bheight=[]
result=[]
Height=[]
print(xk.Time[3])
Atime=regenerateTime(xk.Time)
Btime=regenerateTime(xk.TimeB)
for i in range(len(Atime)):
    height=Atime[i]*Ad[0]+Ad[1]
    Aheight.append(height)
for i in range(len(Btime)):
    height=Btime[i]*Bd[0]+Bd[1]
    Bheight.append(height)
for k in range(0,len(Atime)):
    LeftTime=Btime[0]
    left=0
    RightTime=Btime[len(xk.TimeB)-1]
    right=len(Btime)
    height=None
    for i in range(0,len(Btime)):
        if Btime[i]<Atime[k]:
            if Btime[i]>=LeftTime:
                LeftTime=Btime[i]
                left=i
        elif Btime[i]>Atime[k]:
            if Btime[i]<=RightTime:
                RightTime=Btime[i]
                right=i
        else:
            height=Bheight[i]
    if right==len(Btime):
        pressure=float(xk.BaroB[right-1])
        height=pressure*Bd[0]+Bd[1]
    if left==0:
        pressure=float(xk.BaroB[left])
        height=pressure*Bd[0]+Bd[1]
    if height==None:
        LeftPressure=float(xk.BaroB[left])
        RightPressure=float(xk.BaroB[right])
        pressure=LeftPressure-(Atime[k]-LeftTime)*(LeftPressure-RightPressure)/(RightTime-LeftTime)
        height=pressure*Bd[0]+Bd[1]
    Height.append(Aheight[k]-height)
    if (height-0.10)>=Aheight[k]:
        result.append(-1)
    elif (height+0.10)<=Aheight[k]:
        result.append(1)
    else:
        result.append(0)
print(result)
RHeight=[]
result2=[]
for j in range(0,len(Height)):
    bb=0
    cc=0.0
    for i in range(0,5):
        if j-2+i>=0 and j-2+i<len(Height):
            bb+=1
            cc+=Height[j-2+i]
    newheight=cc/bb
    RHeight.append(newheight)
    if RHeight[j]>0:
        result2.append(1)
    elif RHeight[j]<0:
        result2.append(-1)
    else:
        result2.append(0)
TrueResult=[]
for i in range(len(result2)):
    if i <240:
        TrueResult.append(1)
    elif i>280 and i<480:
        TrueResult.append(-1)
    elif i>480:
        for j in range(480,i):
            if result2[j]==1:
                TrueResult.append(1)
                break
        if len(TrueResult)==i:
            pass
        else:
            TrueResult.append(-1)
    else:
        TrueResult.append(result2[i])
TrueResult.append(1)
fig1, =plt.plot(result2)
# fig2, =plt.plot(RHeight)
print(len(result2))
print(xk.Time[0])
print(xk.Time[len(xk.Time)-1])
print(xk.TimeB[0])
print(xk.TimeB[len(xk.TimeB)-1])
print(len(xk.Time))
print(len(xk.TimeB))
fig3, =plt.plot(TrueResult)
plt.show()
with open('new_xk.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerows([xk.Time,xk.GyroX,xk.GyroY,xk.GyroZ,xk.AcceX,xk.AcceY,xk.AcceZ,xk.MagnX,xk.MagnY,xk.MagnZ,xk.Baro,result2,TrueResult])