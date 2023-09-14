#importing required libraries
import pandas as pd
import numpy as np
import gradio as gr
#importing the dataset
data=pd.read_csv("Fraud.csv")
#viewing the dataset
#print(data.shape)
#print(data.head())
#print(data.info())
#print(data.describe())
#checking for missing or null values in dataset
#print(data.isna().sum())
#itseems there are no null values in dataset
#checking for duplicated values in dataset
#print(data.duplicated())
#print(data.corr())
#dropping unwanted columns and performing one hot encoding on required columns
data.drop(['nameOrig','nameDest'],inplace=True,axis=1)
data=pd.get_dummies(data,columns=['type'],drop_first=True)
#print(data.columns)
#selecting the independent(input) and dependent(output) variables
x=data.drop(['isFraud'],axis=1)
y=data['isFraud']
#print(x)
#print(y)
#model building
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
#checking the accuracy,f1score,precision,recall and support of the model
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
#print(accuracy_score(y_test,y_pred))
#print(classification_report(y_test,y_pred))
#print(confusion_matrix(y_test,y_pred))
#the model accuracy looks good enough we can further on deploy the model and predict the fraudulent transactions



