import json
import pandas as pd
import matplotlib.pyplot as plt
import math
import csv
import copy, numpy as np
from builtins import dir
import tensorflow as tf
def add_layer(inputs, in_size, out_size, activation_function=None):
    # add one more layer and return the output of this layer
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs
XX = []
yy = []
def sigmoid(x):  
    output = 1/(1+np.exp(-x))  
    return output 
def sigmoid_output_to_derivative(output):  
    return output*(1-output) 
def AddTrainingInput(name,Input):
    a=len(Input)
    Traininginput=np.array(np.zeros((a+600,57)))
    Traininginput[0:a]=Input
    for i in range(0,600):
        for j in range(-2,3):
            if i+j>=0 and i+j<600:
                Traininginput[i+a][j+2]=name.GyroX[i+j]
                Traininginput[i+a][j+7]=name.GyroY[i+j]
                Traininginput[i+a][j+12]=name.GyroZ[i+j]
                Traininginput[i+a][j+17]=name.AcceX[i+j]
                Traininginput[i+a][j+22]=name.AcceY[i+j]
                Traininginput[i+a][j+27]=name.AcceZ[i+j]
                Traininginput[i+a][j+32]=name.MagnX[i+j]
                Traininginput[i+a][j+37]=name.MagnY[i+j]
                Traininginput[i+a][j+42]=name.MagnZ[i+j]
    for i in range(a,a+600):
        for j in range(0,4):
            Traininginput[i][45+j]=Traininginput[i][31+j]-Traininginput[i][30+j]
            Traininginput[i][49+j]=Traininginput[i][36+j]-Traininginput[i][35+j]
            Traininginput[i][53+j]=Traininginput[i][41+j]-Traininginput[i][40+j]
    return Traininginput
def AddTrainingResult(name,Result):
    a=len(Result)
    Trainingresult=np.array(np.zeros((a+600,1)))
    Trainingresult[0:a]=Result
    for i in range(0,600):
        Trainingresult[i+a][0]=name.TrueResult[i]
    return Trainingresult
    
qj=pd.read_csv('data4\data_qj.csv',encoding='latin1')
xk=pd.read_csv('data4\data_xk.csv',encoding='latin1')
lyf=pd.read_csv('data4\data_lyf.csv',encoding='latin1')
czk=pd.read_csv('data4\data_czk.csv',encoding='latin1')
cl=pd.read_csv('data4\data_cl.csv',encoding='latin1')
yyh=pd.read_csv('data4\data_yyh.csv',encoding='latin1')
db=pd.read_csv('data4\data_db.csv',encoding='latin1')
gwc=pd.read_csv('data4\data_gwc.csv',encoding='latin1')
syp=pd.read_csv('data4\data_syp.csv',encoding='latin1')
txr=pd.read_csv('data4\data_txr.csv',encoding='latin1')
cjq=pd.read_csv('data4\data_cjq.csv',encoding='latin1')
yyt=pd.read_csv('data4\data_yyt.csv',encoding='latin1')
TrainingInput=np.array(np.zeros((600,57)))
TrainingResult=np.array(np.zeros((600,1)))
TestingInput=np.array(np.zeros((600,57)))
TestingResult=np.array(np.zeros((600,1)))
for i in range(len(qj.Time)):
    for j in range(-2,3):
        if i+j>=0 and i+j<600:
            TrainingInput[i][j+2]=qj.GyroX[i+j]
            TrainingInput[i][j+7]=qj.GyroY[i+j]
            TrainingInput[i][j+12]=qj.GyroZ[i+j]
            TrainingInput[i][j+17]=qj.AcceX[i+j]
            TrainingInput[i][j+22]=qj.AcceY[i+j]
            TrainingInput[i][j+27]=qj.AcceZ[i+j]
            TrainingInput[i][j+32]=qj.MagnX[i+j]
            TrainingInput[i][j+37]=qj.MagnY[i+j]
            TrainingInput[i][j+42]=qj.MagnZ[i+j]
    TrainingResult[i][0]=qj.TrueResult[i]
for i in range(len(qj.Time)):
    for j in range(0,4):
        TrainingInput[i][45+j]=TrainingInput[i][31+j]-TrainingInput[i][30+j]
        TrainingInput[i][49+j]=TrainingInput[i][36+j]-TrainingInput[i][35+j]
        TrainingInput[i][53+j]=TrainingInput[i][41+j]-TrainingInput[i][40+j]
TrainingInput=AddTrainingInput(lyf, TrainingInput)
TrainingResult=AddTrainingResult(lyf, TrainingResult)
TrainingInput=AddTrainingInput(czk, TrainingInput)
TrainingResult=AddTrainingResult(czk, TrainingResult)
TrainingInput=AddTrainingInput(cl, TrainingInput)
TrainingResult=AddTrainingResult(cl, TrainingResult)
TrainingInput=AddTrainingInput(yyh, TrainingInput)
TrainingResult=AddTrainingResult(yyh, TrainingResult)
TrainingInput=AddTrainingInput(db, TrainingInput)
TrainingResult=AddTrainingResult(db, TrainingResult)
TrainingInput=AddTrainingInput(gwc, TrainingInput)
TrainingResult=AddTrainingResult(gwc, TrainingResult)
TrainingInput=AddTrainingInput(syp, TrainingInput)
TrainingResult=AddTrainingResult(syp, TrainingResult)
TrainingInput=AddTrainingInput(txr, TrainingInput)
TrainingResult=AddTrainingResult(txr, TrainingResult)
TrainingInput=AddTrainingInput(cjq, TrainingInput)
TrainingResult=AddTrainingResult(cjq, TrainingResult)
TrainingInput=AddTrainingInput(yyt, TrainingInput)
TrainingResult=AddTrainingResult(yyt, TrainingResult)
for i in range(0,600):
    for j in range(-2,3):
        if i+j>=0 and i+j<600:
            TestingInput[i][j+2]=xk.GyroX[i+j]
            TestingInput[i][j+7]=xk.GyroY[i+j]
            TestingInput[i][j+12]=xk.GyroZ[i+j]
            TestingInput[i][j+17]=xk.AcceX[i+j]
            TestingInput[i][j+22]=xk.AcceY[i+j]
            TestingInput[i][j+27]=xk.AcceZ[i+j]
            TestingInput[i][j+32]=xk.MagnX[i+j]
            TestingInput[i][j+37]=xk.MagnY[i+j]
            TestingInput[i][j+42]=xk.MagnZ[i+j]
    TestingResult[i][0]=xk.TrueResult[i]
for i in range(0,600):
    for j in range(0,4):
        TestingInput[i][45+j]=TestingInput[i][31+j]-TestingInput[i][30+j]
        TestingInput[i][49+j]=TestingInput[i][36+j]-TestingInput[i][35+j]
        TestingInput[i][53+j]=TestingInput[i][41+j]-TestingInput[i][40+j]
# for i in range(len(TrainingInput)):
#     for j in range(30,45):
#         TrainingInput[i][j]=0
# for i in range(len(TestingInput)):
#     for j in range(30,45):
#         TestingInput[i][j]=0
xs = tf.placeholder(tf.float32, [None, 57])
ys = tf.placeholder(tf.float32, [None, 1])
l1 = add_layer(xs, 57, 150, activation_function=tf.nn.sigmoid)
l2 = add_layer(l1, 150, 150, activation_function=tf.nn.sigmoid)
l3 = add_layer(l2, 150, 150, activation_function=tf.nn.sigmoid)
l4 = add_layer(l3, 150, 150, activation_function=tf.nn.sigmoid)
l5 = add_layer(l4, 150, 150, activation_function=tf.nn.sigmoid)
l6 = add_layer(l5, 150, 150, activation_function=tf.nn.sigmoid)
l7 = add_layer(l6, 150, 150, activation_function=tf.nn.sigmoid)
l8 = add_layer(l7, 150, 150, activation_function=tf.nn.sigmoid)
l9 = add_layer(l8, 150, 50, activation_function=tf.nn.sigmoid)
l10 = add_layer(l9, 50, 20, activation_function=tf.nn.sigmoid)
prediction = add_layer(l10, 20, 1, activation_function=None)
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.001).minimize(loss)
init = tf.global_variables_initializer()
saver = tf.train.Saver()
  
with tf.Session() as sess:
    sess.run(init)
    for jj in range(10000):
        sess.run(train_step, feed_dict={xs: TrainingInput, ys: TrainingResult})
        if jj%1000==0:
            print('TrainingTime:')
            print(jj)
    saver.save(sess, "./model4.ckpt")
with tf.Session() as sessss:
    saver.restore(sessss, "./model4.ckpt")
    answer = sessss.run(prediction, feed_dict={xs: TestingInput})
with tf.Session() as sessss:
    saver.restore(sessss, "./model4.ckpt")
    answer2 = sessss.run(prediction, feed_dict={xs: TrainingInput})
Answer=[]
Answer2=[]
Assume=0
Assume2=0
for i in range(len(TestingInput)):
    if answer[i][0]>0:
        Answer.append(1)
    else:
        Answer.append(-1)
    if answer[i][0]>1:
        a=1
    elif answer[i][0]<-1:
        a=-1
    else:
        a=answer[i][0]
    Assume+=0.5+0.5*a
for i in range(len(TrainingInput)):
    if answer2[i][0]>0:
        Answer2.append(1)
    else:
        Answer2.append(-1)
    if answer2[i][0]>1:
        a2=1
    elif answer2[i][0]<-1:
        a2=-1
    else:
        a2=answer2[i][0]
    Assume2+=0.5+0.5*a2
AA1=Assume/len(Answer)
AA2=Assume2/len(Answer2)
right=0
right2=0
B1=0
B2=0
for i in range(len(Answer)):
    if Answer[i]==TestingResult[i]:
        right+=1
    if TestingResult[i]==1:
        B1+=1
for i in range(len(Answer2)):
    if Answer2[i]==TrainingResult[i]:
        right2+=1
    if TrainingResult[i]==1:
        B2+=1
BB1=B1/len(Answer)
BB2=B2/len(Answer2)
D1=abs(BB1-AA1)
D2=abs(BB2-AA2)
totallyaccuracy=right/len(Answer)
tt=right2/len(Answer2)
print('Accuracy:')
print(totallyaccuracy)
print('TrainingAccuracy:')
print(tt)
print('Time Error:')
print(D1)
print('Training Time Error:')
print(D2)
fig1, =plt.plot(Answer)
fig2, =plt.plot(TestingResult)
plt.show()