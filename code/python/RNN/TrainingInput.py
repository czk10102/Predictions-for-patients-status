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
# np.set_printoptions(threshold='nan')
qj=pd.read_csv('data\data_qj.csv',encoding='latin1')
xk=pd.read_csv('data\data_xk.csv',encoding='latin1')
TrainingInput=np.array(np.zeros((600,45)))
TrainingResult=np.array(np.zeros((600,1)))
TestingInput=np.array(np.zeros((600,45)))
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
xs = tf.placeholder(tf.float32, [None, 45])
ys = tf.placeholder(tf.float32, [None, 1])
l1 = add_layer(xs, 45, 150, activation_function=tf.nn.sigmoid)
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
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
init = tf.global_variables_initializer()
saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(init)
    for jj in range(10000):
        sess.run(train_step, feed_dict={xs: TrainingInput, ys: TrainingResult})
        if jj%1000==0:
            print('TrainingTime:')
            print(jj)
    saver.save(sess, "./model.ckpt")
print('TrainingFinished!')
with tf.Session() as sessss:
    saver.restore(sessss, "./model.ckpt")
    answer = sessss.run(prediction, feed_dict={xs: TestingInput})
with tf.Session() as sessss:
    saver.restore(sessss, "./model.ckpt")
    answer2 = sessss.run(prediction, feed_dict={xs: TrainingInput})
Answer=[]
Answer2=[]
for i in range(0,600):
    if answer[i][0]>0:
        Answer.append(1)
    else:
        Answer.append(-1)
    if answer2[i][0]>0:
        Answer2.append(1)
    else:
        Answer2.append(-1)
        
# fig1, =plt.plot(Answer)
# fig2, =plt.plot(TestingResult)
# plt.show()
right=0
right2=0
for i in range(len(Answer)):
    if Answer[i]==TestingResult[i]:
        right+=1
    if Answer2[i]==TrainingResult[i]:
        right2+=1
totallyaccuracy=right/600
tt=right2/600
print('Accuracy:')
print(totallyaccuracy)
print('TrainingAccuracy:')
print(tt)