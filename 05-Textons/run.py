import sys
sys.path.append('lib/python')

#Create a filter bank with deafult params
from fbCreate import fbCreate
fb = fbCreate()

import pickle
import os
f = open(os.path.join(os.getcwd(),'trainset'),'rb')
train = pickle.load(f)
f.close()

f = open(os.path.join(os.getcwd(),'testset'),'rb')
test = pickle.load(f)
f.close()

#Set number of clusters
k = 16*8

#Apply filterbank to sample image
from fbRun import fbRun
import numpy as np


for idx, data in enumerate(train):
    fr = fbRun(fb,data['image'][:64,:64])
    print('filtering training image {}'.format(idx))
    for i in range(np.array(fb).shape[0]):
        for j in range(np.array(fb).shape[1]):
            if idx>0:
                tfim[i][j] = np.hstack((tfim[i][j],fr[i][j]))
            else:
                tfim = fr

#Computer textons from filter
from computeTextons import computeTextons
print('computing textons ...')
map, textons = computeTextons(tfim, k)

#Calculate texton representation with current texton dictionary

from assignTextons import assignTextons

trainmaps = []
trainlabels = []

for idx, data in enumerate(train):
    print('texton map for train image {}'.format(idx))
    trainmaps.append(assignTextons(fbRun(fb,data['image'][:64,:64]),textons.transpose()))
    trainlabels.append(data['label'])

tmaps = []
labels = []

for idx, data in enumerate(test):
    print('texton map for test image {}'.format(idx))
    tmaps.append(assignTextons(fbRun(fb,data['image'][:64,:64]),textons.transpose()))
    labels.append(data['label'])


def histc(X, bins):
    import numpy as np
    map_to_bins = np.digitize(X,bins)
    r = np.zeros(bins.shape)
    for i in map_to_bins:
        r[i-1] += 1
    return np.array(r)

trainhgrams = np.zeros((len(trainmaps),k))

for idx, tmap in enumerate(trainmaps):
    print('histogram for train image {}'.format(idx))
    trainhgrams[idx,:]=(histc(tmap.flatten(), np.arange(k)))/tmap.size



hgrams = np.zeros((len(tmaps),k))

for idx, tmap in enumerate(tmaps):
    print('histogram for test image {}'.format(idx))
    hgrams[idx,:]=(histc(tmap.flatten(), np.arange(k)))/tmap.size


from sklearn.metrics.pairwise import chi2_kernel
from sklearn.neighbors import KNeighborsClassifier

kn = 5

print('training KNN classifier ...')

'''neigh = KNeighborsClassifier(n_neighbors=kn,algorithm='brute',metric='precomputed')
neigh.fit(trainchsq, trainlabels)

prlabels = neigh.predict(chsq)'''

def chi_squared(X, Y):
    distance = chi2_kernel(X.reshape(1,-1),Y.reshape(1,-1))
    #distance = np.sum(((X-Y)**2))
    return distance

neigh = KNeighborsClassifier(n_neighbors=kn, metric=chi_squared)
neigh.fit(trainhgrams, trainlabels)
prlabels = neigh.predict(hgrams)

from sklearn.metrics import accuracy_score

aca_neigh = accuracy_score(labels, prlabels)


def kernel(X, Y):
    distance = 1-np.sum(np.minimum(X,Y))
    return distance

neigh = KNeighborsClassifier(n_neighbors=kn, metric=kernel)
neigh.fit(trainhgrams, trainlabels)
prlabels = neigh.predict(hgrams)
aca_neigh = accuracy_score(labels, prlabels)
print('ACA_KNN',aca_neigh)


from sklearn.ensemble import RandomForestClassifier

print('training RF classifier ...')

rf = RandomForestClassifier(n_estimators=700 , max_depth=6, random_state=0)
rf.fit(trainhgrams, trainlabels)
rflabels = rf.predict(hgrams)
aca_rf = accuracy_score(trainlabels, rflabels)
print('ACA_RF',aca_rf)

print('Done!')
