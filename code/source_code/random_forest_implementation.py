# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 18:02:07 2018

@author: Shyam
"""

#random forest example
import os
#os.chdir('C:\stuff\Studies\Fall 18\HPC Big Data\Project\Cython')

from memory_profiler import profile
#from sklearn.datasets import load_iris
import forest_modified
from forest_modified import RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier as RandomForestClassifier_original
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import time

#data_hpc_protocol_csv = os.path.join('C:\stuff\Studies\Fall 18\HPC Big Data\Project\PAMAP2_Dataset\Protocol','csv_files')
data_hpc_protocol_csv = './csv_files'

"""We are importing the data using Pandas"""

start = time.time()
for idx, patient_file in enumerate(os.listdir(data_hpc_protocol_csv)):
    if idx == 0:
        df = pd.read_csv(os.path.join(data_hpc_protocol_csv,patient_file)
                                                                  , header = None)
        patient_all_pd = df
    else:
        df = pd.read_csv(os.path.join(data_hpc_protocol_csv,patient_file)
                                                                  , header = None)
        patient_all_pd = patient_all_pd.append(df)

end = time.time()
reading_time = end - start
print("Reading time is " + str(reading_time))

"""Here, we are preprocessing the data"""
                                   
patient_all_pd.drop(columns = [0,2], axis =1, inplace = True)
patient_all_pd.dropna(inplace = True)
train_data_pd, test_data_pd = train_test_split(patient_all_pd,train_size = 0.7,test_size = 0.3)
columns = list(range(3,54))
print("Dataframe ")
print(train_data_pd.head())

"""This is the function we call to train the model and whose memory we are going to profile"""

@profile
def train_model(x,y):
    clf = RandomForestClassifier(n_estimators = 20,n_jobs = -1, random_state=0)
    clf.fit(x, y)
    return clf

print("Going to train the model now")
start = time.time()
clf = train_model(train_data_pd[columns],train_data_pd[1])
#clf.predict(test[features])
end = time.time()
fitting_time = end - start
print("Fitting time is " + str(fitting_time))

#preds = clf.predict(test_data_pd[columns])
#print(accuracy_score(test_data_pd[1], clf))

#print(pd.crosstab(test['species'], preds, rownames=['Actual Species'], colnames=['Predicted Species']))

#list(zip(train[features], clf.feature_importances_))