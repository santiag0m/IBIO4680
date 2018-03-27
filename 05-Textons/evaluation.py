import os
import pickle
import numpy as np
import time
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

f = open(os.path.join(os.getcwd(),'trainhgrams'),'rb')
trainhgrams = pickle.load(f)
f.close()

f = open(os.path.join(os.getcwd(),'trainlabels'),'rb')
trainlabels = pickle.load(f)
f.close()

f = open(os.path.join(os.getcwd(),'hgrams'),'rb')
hgrams = pickle.load(f)
f.close()

f = open(os.path.join(os.getcwd(),'labels'),'rb')
labels = pickle.load(f)
f.close()

def chi_squared(X, Y):
    distance = np.sum(((X-Y)**2))
    return distance

def kernel(X, Y):
    distance = 1-np.sum(np.minimum(X,Y))
    return distance
idx = np.arange(40)
for i in idx:
    kn = i+1
    print('K', kn)
    t = time.time()
    neigh = KNeighborsClassifier(n_neighbors=kn, metric=kernel)
    neigh.fit(trainhgrams, trainlabels)
    prlabels = neigh.predict(hgrams)
    confusion_matrix_KNN = confusion_matrix(labels, prlabels)
    aca_neigh = accuracy_score(labels, prlabels)
    print('ACA_KNN', aca_neigh)
    print(time.time()-t)

rf = RandomForestClassifier(n_estimators=700 , max_depth=6, random_state=0)
rf.fit(trainhgrams, trainlabels)
rflabels = rf.predict(hgrams)
confusion_matrix_KNN = confusion_matrix(labels, rflabels)
aca_rf = accuracy_score(labels, rflabels)
print('ACA_RF', aca_rf)
