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

#Apply filterbank to sample image
from fbRun import fbRun
import numpy as np

selected = [] # Sample images for filter visualization
simg = []

import cv2

for idx, data in enumerate(train):
    if idx%50 == 0:
        response = []
        simg.append(data['image'])
    fr = fbRun(fb,data['image'][:64,:64])
    print('filtering training image {}'.format(idx))
    for i in range(np.array(fb).shape[0]):
        for j in range(np.array(fb).shape[1]):
            if idx%50 == 0:
                response.append(fr[i][j])
            if idx>0:
                tfim[i][j] = np.hstack((tfim[i][j],fr[i][j]))
            else:
                tfim = fr
    if idx%50 == 0:
        selected.append(response)

import matplotlib.pyplot as plt

plt.ion()
for resp in selected:
    plt.figure()
    im = np.concatenate(resp,axis=1)
    cv2.imshow("Filter Responses",cv2.applyColorMap(np.uint8(im),cv2.COLORMAP_AUTUMN))



