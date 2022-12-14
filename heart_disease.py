import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data processing"""

#loading dataset into pandas
heart_data = pd.read_csv('/content/heart.csv')

#print first 5 values of data set
heart_data.head()

#print last 5 values/rows of the data set
heart_data.tail()

#number of coloumns and rows in data set
heart_data.shape

#info about dataset
heart_data.info()

#missing values check
heart_data.isnull().sum()

#statistical measure of the data
heart_data.describe()

#checking distribution of target value
heart_data['target'].value_counts()

"""splitting features from Target"""

x = heart_data.drop(columns ='target', axis =1)
y = heart_data['target']

print(x)

print(y)

"""Training and testing data split"""

X_train,X_test,Y_train,Y_test = train_test_split(x,y, test_size=0.2,stratify=y, random_state=2)

print(x.shape, X_train.shape)

print(y.shape,Y_train.shape)

"""# **Model Training**

Logistic Regression
"""

model = LogisticRegression()

#training model with training data
model.fit(X_train,Y_train)

"""Evaluating the model"""

#accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction,Y_train)

print("Accuracy on training data: ", training_data_accuracy)

#accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction,Y_test)

print("Accuracy on test data: ", test_data_accuracy)

"""Building Predictive System"""

input = (70,1,0,145,174,0,1,125,1,2.6,0,0,3)
#changing user input into numpy array
input_as_numpyarray = np.asarray(input)

#reshaping array
input_reshapped = input_as_numpyarray.reshape(1,-1)

prediction = model.predict(input_reshapped)
print(prediction)

