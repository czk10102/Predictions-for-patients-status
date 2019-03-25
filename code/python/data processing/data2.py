import json
import pandas as pd
import matplotlib.pyplot as plt
import math
import csv
import numpy as np
from builtins import dir

# JSONObject jpath = new JSONObject()
# from asn1crypto.core import range
wendang = open("seconddata.json", encoding='utf-8')
data = json.load(wendang)
Aair=np.array([1009.33,1008.91,1009.68])
Bair=np.array([1009.85,1009.36,1010.07])
height=np.array([0.0,3.5,-3.5])
A='546c0e531afa'
B='546c0e52ff05'
start_time='16:28:30'
end_time='16:38:30'
name='CZK'
Ad=np.polyfit(Aair, height, 1)
Bd=np.polyfit(Bair, height, 1)
def SelectTime(time):
    t0=time.split('T')
    t1=t0[1].split('+')
    t=t1[0]
    return t
def time_period(time,start_time,end_time):
    e_time=end_time.split(':')
    s_time=start_time.split(':')
    t=time.split(':')
    e_time[0]=int(e_time[0])
    e_time[1]=int(e_time[1])
    e_time[2]=int(e_time[2])
    s_time[0]=int(s_time[0])
    s_time[1]=int(s_time[1])
    s_time[2]=int(s_time[2])
    t[0]=int(t[0])
    t[1]=int(t[1])
    t[2]=float(t[2])
    time=t[0]*3600+t[1]*60+t[2]
    start_time=s_time[0]*3600+s_time[1]*60+s_time[2]
    end_time=e_time[0]*3600+e_time[1]*60+e_time[2]
    if end_time<=start_time:
        return False
    else:
        if time>=start_time and time<=end_time:
            return True
        else:
            return False
def regenerateTime(time):
    newtime=[]
    for k in range(len(time)):
        t=time[k].split(':')
        t[0]=int(t[0])
        t[1]=int(t[1])
        t[2]=float(t[2])
        T=t[0]*3600+t[1]*60+t[2]
        newtime.append(T)
    return newtime
def if_Android(doc,i):
    if doc['rows'][i].__contains__('doc'):
        if doc['rows'][i]['doc'].__contains__('data'):
            if doc['rows'][i]['doc']['data'].__contains__('d'):
                if doc['rows'][i]['doc']['data']['d'].__contains__('acc_z'):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
def if_IOS(doc,i):
    if doc['rows'][i].__contains__('doc'):
        if doc['rows'][i]['doc'].__contains__('data'):
            if doc['rows'][i]['doc']['data'].__contains__('d'):
                if doc['rows'][i]['doc']['data']['d'].__contains__('myName'):
                    if doc['rows'][i]['doc']['data']['d']['myName']=='ti-sensortag2':
                        if doc['rows'][i]['doc']['data']['d'].__contains__('pressure'):
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
def of_others(doc,i):
    if doc['rows'][i]['key']=='_design/iotp':
        return True
    else:
        return False               
def IOS_find_deviceId(doc,i):
    a=doc['rows'][i]['doc']['deviceId']
    return a
def Android_find_deviceId(doc,i):
    a=doc['rows'][i]['doc']['deviceId']
    return a
def IOS_find_time(doc,i):
    a=doc['rows'][i]['doc']['timestamp']
    return a
def Android_find_time(doc,i):
    a=doc['rows'][i]['doc']['timestamp']
    return a
def IOS_find_baro(doc,i):
    a=doc['rows'][i]['doc']['data']['d']['pressure']
    return a
def Android_find_baro(doc,i):
    a=doc['rows'][i]['doc']['data']['d']['air_pressure']
    return a
def IOS_find_gyro_X(doc,i):
    a=doc['rows'][i]['doc']['data']['d']['gyroX']
    return a
def Android_find_gyro_X(doc,i):
    a=doc['rows'][i]['doc']['data']['d']['gyro_x']
    return a
def IOS_find_gyro_Y(doc,i):
    a=doc['rows'][i]['doc']['data']['d']['gyroY']
    return a
def Android_find_gyro_Y(doc,i):
    a=doc['rows'][i]['doc']['data']['d']['gyro_y']
    return a
def IOS_find_gyro_Z(doc,i):
    a=doc['rows'][i]['doc']['data']['d']['gyroZ']
    return a
def Android_find_gyro_Z(doc,i):
    a=doc['rows'][i]['doc']['data']['d']['gyro_z']
    return a
def IOS_find_acce_X(doc,i):
    a=doc['rows'][i]['doc']['data']['d']['accelX']
    return a
def Android_find_acce_X(doc,i):
    a=doc['rows'][i]['doc']['data']['d']['acc_x']
    return a
def IOS_find_acce_Y(doc,i):
    a=doc['rows'][i]['doc']['data']['d']['accelY']
    return a
def Android_find_acce_Y(doc,i):
    a=doc['rows'][i]['doc']['data']['d']['acc_y']
    return a
def IOS_find_acce_Z(doc,i):
    a=doc['rows'][i]['doc']['data']['d']['accelZ']
    return a
def Android_find_acce_Z(doc,i):
    a=doc['rows'][i]['doc']['data']['d']['acc_z']
    return a
def IOS_find_magn_X(doc,i):
    a=doc['rows'][i]['doc']['data']['d']['magX']
    return a
def Android_find_magn_X(doc,i):
    a=doc['rows'][i]['doc']['data']['d']['compass_x']
    return a
def IOS_find_magn_Y(doc,i):
    a=doc['rows'][i]['doc']['data']['d']['magY']
    return a
def Android_find_magn_Y(doc,i):
    a=doc['rows'][i]['doc']['data']['d']['compass_y']
    return a
def IOS_find_magn_Z(doc,i):
    a=doc['rows'][i]['doc']['data']['d']['magZ']
    return a
def Android_find_magn_Z(doc,i):
    a=doc['rows'][i]['doc']['data']['d']['compass_z']
    return a
A_time=[]
B_time=[]
A_baro=[]
B_baro=[]
A_gyro_X=[]
A_gyro_Y=[]
A_gyro_Z=[]
B_gyro_X=[]
B_gyro_Y=[]
B_gyro_Z=[]
A_acce_X=[]
A_acce_Y=[]
A_acce_Z=[]
B_acce_X=[]
B_acce_Y=[]
B_acce_Z=[]
A_magn_X=[]
A_magn_Y=[]
A_magn_Z=[]
B_magn_X=[]
B_magn_Y=[]
B_magn_Z=[]
l=len(data['rows'])
b=0
c=0
d=0
for k in range(0,l):
    if if_IOS(data, k):
        deviceId=IOS_find_deviceId(data, k)
        if deviceId==A:
            time=IOS_find_time(data, k)
            time=SelectTime(time)
            if time_period(time, start_time, end_time):
                A_time.append(time)
                A_acce_X.append(IOS_find_acce_X(data, k))
                A_acce_Y.append(IOS_find_acce_Y(data, k))
                A_acce_Z.append(IOS_find_acce_Z(data, k))
                A_gyro_X.append(IOS_find_gyro_X(data, k))
                A_gyro_Y.append(IOS_find_gyro_Y(data, k))
                A_gyro_Z.append(IOS_find_gyro_Z(data, k))
                A_magn_X.append(IOS_find_magn_X(data, k))
                A_magn_Y.append(IOS_find_magn_Y(data, k))
                A_magn_Z.append(IOS_find_magn_Z(data, k))
                A_baro.append(IOS_find_baro(data, k))
        elif deviceId==B:
            time=IOS_find_time(data, k)
            time=SelectTime(time)
            if time_period(time, start_time, end_time):
                B_time.append(time)
                B_acce_X.append(IOS_find_acce_X(data, k))
                B_acce_Y.append(IOS_find_acce_Y(data, k))
                B_acce_Z.append(IOS_find_acce_Z(data, k))
                B_gyro_X.append(IOS_find_gyro_X(data, k))
                B_gyro_Y.append(IOS_find_gyro_Y(data, k))
                B_gyro_Z.append(IOS_find_gyro_Z(data, k))
                B_magn_X.append(IOS_find_magn_X(data, k))
                B_magn_Y.append(IOS_find_magn_Y(data, k))
                B_magn_Z.append(IOS_find_magn_Z(data, k))
                B_baro.append(IOS_find_baro(data, k))
        else:
            print('error ID!')
    elif if_Android(data, k):
        deviceId=Android_find_deviceId(data, k)
        if deviceId==A:
            time=Android_find_time(data, k)
            time=SelectTime(time)
            if time_period(time, start_time, end_time):
                A_time.append(time)
                A_acce_X.append(Android_find_acce_X(data, k))
                A_acce_Y.append(Android_find_acce_Y(data, k))
                A_acce_Z.append(Android_find_acce_Z(data, k))
                A_gyro_X.append(Android_find_gyro_X(data, k))
                A_gyro_Y.append(Android_find_gyro_Y(data, k))
                A_gyro_Z.append(Android_find_gyro_Z(data, k))
                A_magn_X.append(Android_find_magn_X(data, k))
                A_magn_Y.append(Android_find_magn_Y(data, k))
                A_magn_Z.append(Android_find_magn_Z(data, k))
                A_baro.append(Android_find_baro(data, k))
        elif deviceId==B:
            time=Android_find_time(data, k)
            time=SelectTime(time)
            if time_period(time, start_time, end_time):
                B_time.append(time)
                B_acce_X.append(Android_find_acce_X(data, k))
                B_acce_Y.append(Android_find_acce_Y(data, k))
                B_acce_Z.append(Android_find_acce_Z(data, k))
                B_gyro_X.append(Android_find_gyro_X(data, k))
                B_gyro_Y.append(Android_find_gyro_Y(data, k))
                B_gyro_Z.append(Android_find_gyro_Z(data, k))
                B_magn_X.append(Android_find_magn_X(data, k))
                B_magn_Y.append(Android_find_magn_Y(data, k))
                B_magn_Z.append(Android_find_magn_Z(data, k))
                B_baro.append(Android_find_baro(data, k))
        else:
            print('error ID!')
    else:
        pass
new_A_time=regenerateTime(A_time)
new_B_time=regenerateTime(B_time)
NAtime=sorted(new_A_time)
NBtime=sorted(new_B_time)
Atime=[]
Btime=[]
AacceX=[]
AacceY=[]
AacceZ=[]
AgyroX=[]
AgyroY=[]
AgyroZ=[]
AmagnX=[]
AmagnY=[]
AmagnZ=[]
Abaro=[]
Aheight=[]
BacceX=[]
BacceY=[]
BacceZ=[]
BgyroX=[]
BgyroY=[]
BgyroZ=[]
BmagnX=[]
BmagnY=[]
BmagnZ=[]
Bbaro=[]
Bheight=[]
for k in range(0,len(NAtime)):
    for i in range(0,len(new_A_time)):
        if NAtime[k]==new_A_time[i]:
            Atime.append(A_time[i])
            AacceX.append(A_acce_X[i])
            AacceY.append(A_acce_Y[i])
            AacceZ.append(A_acce_Z[i])
            AgyroX.append(A_gyro_X[i])
            AgyroY.append(A_gyro_Y[i])
            AgyroZ.append(A_gyro_Z[i])
            AmagnX.append(A_magn_X[i])
            AmagnY.append(A_magn_Y[i])
            AmagnZ.append(A_magn_Z[i])
            Abaro.append(A_baro[i])
            height=float(A_baro[i])*Ad[0]+Ad[1]
            Aheight.append(height)
            new_A_time[i]=-1
            break
for k in range(0,len(NBtime)):
    for i in range(0,len(new_B_time)):
        if NBtime[k]==new_B_time[i]:
            Btime.append(B_time[i])
            BacceX.append(B_acce_X[i])
            BacceY.append(B_acce_Y[i])
            BacceZ.append(B_acce_Z[i])
            BgyroX.append(B_gyro_X[i])
            BgyroY.append(B_gyro_Y[i])
            BgyroZ.append(B_gyro_Z[i])
            BmagnX.append(B_magn_X[i])
            BmagnY.append(B_magn_Y[i])
            BmagnZ.append(B_magn_Z[i])
            Bbaro.append(B_baro[i])
            height=float(B_baro[i])*Bd[0]+Bd[1]
            Bheight.append(height)
            new_B_time[i]=-1
            break
result=[]
Height=[]
for k in range(0,len(NAtime)):
    LeftTime=NBtime[0]
    left=0
    RightTime=NBtime[len(NBtime)-1]
    right=len(NBtime)
    height=None
    for i in range(0,len(NBtime)):
        if NBtime[i]<NAtime[k]:
            if NBtime[i]>=LeftTime:
                LeftTime=NBtime[i]
                left=i
        elif NBtime[i]>NAtime[k]:
            if NBtime[i]<=RightTime:
                RightTime=NBtime[i]
                right=i
        else:
            height=Bheight[i]
    if right==len(NBtime):
        pressure=float(Bbaro[right-1])
        height=pressure*Bd[0]+Bd[1]
    if left==0:
        pressure=float(Bbaro[left])
        height=pressure*Bd[0]+Bd[1]
    if height==None:
        LeftPressure=float(Bbaro[left])
        RightPressure=float(Bbaro[right])
        pressure=LeftPressure-(NAtime[k]-LeftTime)*(LeftPressure-RightPressure)/(RightTime-LeftTime)
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
    newheight=cc/bb-2.5
    RHeight.append(newheight)
    if RHeight[j]>0:
        result2.append(1)
    elif RHeight[j]<0:
        result2.append(-1)
    else:
        result2.append(0)
# vector=[1,1,1]
# v00=0
# v01=-0.5
# v02=0.5
# v0=[]
# v1=[]
# v2=[]
# x0=[]
# x1=[]
# x2=[]
# v0.append(v00)
# v1.append(v01)
# v2.append(v02)
# x0.append(0)
# x1.append(0)
# x2.append(0)
# for x in range(10):
#     dv=float(AacceX[x])
#     v0.append(v0[x]+dv)
#     v1.append(v1[x]+dv)
#     v2.append(v2[x]+dv)
#     dx0=v0[x]+v0[x+1]
#     dx1=v1[x]+v1[x+1]
#     dx2=v2[x]+v2[x+1]
#     x0.append(x0[x]+dx0)
#     x1.append(x1[x]+dx1)
#     x2.append(x2[x]+dx2)
# fig0, =plt.plot(x0)
# fig1, =plt.plot(x1)
# fig2, =plt.plot(x2)

# av=[0,0,0]
# aa=[0,0,0]
# v=[0,0,0]
# a=[0,0,0]
# comp=[0,1,0]
# position=[0,0,0]
# for i in range(len(Atime)-5):
#     magn=[float(AmagnX[i]),float(AmagnY[i]),float(AmagnZ[i])]
#     mm=math.sqrt(pow(magn[0],2)+pow(magn[1],2)+pow(magn[2],2))
#     direct=[magn[0]/mm,magn[1]/mm,magn[2]/mm]
TrueResult=[]
for i in range(len(result2)):
    if i <240:
        TrueResult.append(1)
    elif i>280 and i<460:
        TrueResult.append(-1)
    elif i>480:
        ee=0
        for j in range(470,i+1):
            if result2[j]==1:
                ee=1
                break
        if ee==1:
            TrueResult.append(1)
        else:
            TrueResult.append(-1)
    else:
        TrueResult.append(result2[i])
# TrueResult.append(1)
fig1, =plt.plot(result2)
fig2, =plt.plot(RHeight)
print(len(result2))
print(Atime[0])
print(Atime[len(Atime)-1])
print(Btime[0])
print(Btime[len(Btime)-1])
print(len(NAtime))
print(len(NBtime))
print(len(Atime))
print(len(Btime))
print(len(TrueResult))
# print(len(new_A_time))
# print(len(new_B_time))
# print(len(A_time))
# print(len(B_time))
# print(NAtime)
# print(new_A_time)
fig3, =plt.plot(TrueResult)
plt.show()
with open('data_cl.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerows([Atime,AgyroX,AgyroY,AgyroZ,AacceX,AacceY,AacceZ,AmagnX,AmagnY,AmagnZ,Abaro,result2,TrueResult,Btime,Bbaro])