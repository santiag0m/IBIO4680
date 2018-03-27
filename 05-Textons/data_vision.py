import os
import random
import numpy as np
import cv2
import ipdb
import pickle

folderspath = os.listdir(os.path.join('data_vision', 'data_textons', 'train'))
train = []
label = 1

for folder in folderspath:
    images = os.listdir(os.path.join('data_vision', 'data_textons', 'train', folder))
    for image in images:
        im = cv2.imread(os.path.join('data_vision', 'data_textons', 'train', folder, image))
        im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        temp = {'image':im,'label':label}
        train.append(temp) 
    label += 1

folderspath = os.listdir(os.path.join('data_vision', 'data_textons', 'test'))
test = []
label = 1

for folder in folderspath:
    images = os.listdir(os.path.join('data_vision', 'data_textons', 'test', folder))
    for image in images:
        im = cv2.imread(os.path.join('data_vision', 'data_textons', 'test', folder, image))
        im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        temp = {'image':im,'label':label}
        test.append(temp) 
    label += 1

f = open(os.path.join(os.getcwd(),'trainset'),'wb')
pickle.dump(train, f)
f.close()

f = open(os.path.join(os.getcwd(),'testset'),'wb')
pickle.dump(test, f)
f.close()
