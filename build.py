import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split

df=pd.read_csv('breast_cancer.csv')

x = df.drop('class', axis=1)  #selecting all the attributes except the class attribute
y = df['class'] #selecting class attribute


#splitting the dataset
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test= train_test_split(x,y, test_size=0.3, random_state=1)


from sklearn.neighbors import KNeighborsClassifier

knn_model=KNeighborsClassifier(n_neighbors=5,weights="distance")
knn_model.fit(x_train,y_train)

y_predknn=knn_model.predict(x_test)

#Use pickle to save our model so that we can use it later

import pickle
# Saving model 

pickle.dump(knn_model, open("model.pkl","wb"))
loaded_model=pickle.load(open("model.pkl","rb"))
