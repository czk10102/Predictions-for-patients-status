# Predictions-for-patients-status
This is my Msc Project

About this project:
------------------------------------------
The objective of this project is to design useful algorithms which can detect if the injured ankle of orthopaedic is higher than the heart by only using one IMU attached to the injured ankle. There are two sorts of different results. The first one is the prediction whether the patient put his injured ankle higher than his heart in each time, which can make the doctors know the actions of patients. Therefore, SVM and RNN were used to make the predictions in this project. 

The project contains the steps of data collection, signal processing, algorithm design, programming and result analysis. All the resources in each step which needs coding have been uploaded here.

About the codes:
-------------------------------------------
The original data in the step of data collection have been uploaded into the file "original data". All of these files are equivalent, so the file name can be changed in the codes of data processing.

In the step of data processing, Python was used to pre-process the data into matrices and MATLAB was used to process the matrices into trainable data by the low-pass filter after that.

The trainable data were saved in the file "trainable data", the data in different files were processed by the low-pass filter with different parameters. The best data which performed best are in the file "data7".

the codes for SVM and RNN are saved in different files. You can choose different groups of data as the testing data by changing the parameters inside.

Others:
-------------------------------------------
The names or paths of some files may be different in the workspace so the codes are not completely accurate. I am sorry if that happened.

The parameters for air pressure were just suitable for a specific sensor. Therefore, they need to be changed when they are applied to other tests.
