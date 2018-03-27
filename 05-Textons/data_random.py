import os
import random
import numpy as np
import cv2
import ipdb 
import pickle

folderspath = os.listdir(os.path.join(os.getenv('HOME'),'texture'))
ind = np.arange(20)

train = []
#train.setdefault('image', [])
#train.setdefault('label', [])

test = []
#test.setdefault('image', [])
#test.setdefault('label', [])

label = 1

for folder in folderspath:
    images = os.listdir(os.path.join(os.getenv('HOME'),'texture',folder))
    random.shuffle(images)
    for i in ind:
        if i<10:
            im = cv2.imread(os.path.join(os.getenv('HOME'),'texture', folder, images[i])) 
            im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            temp = {'image':im,'label':label}
            train.append(temp)
            #train['image'].append(im)
            #train['label'].append(label)
        else:
            im = cv2.imread(os.path.join(os.getenv('HOME'),'texture', folder, images[i])) 
            im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            temp = {'image':im,'label':label}
            test.append(temp)
            #test['image'].append(im)
            #test['label'].append(label)
    label += 1
            
f = open(os.path.join(os.getcwd(),'trainset'),'wb')
pickle.dump(train, f)
f.close()

f = open(os.path.join(os.getcwd(),'testset'),'wb')
pickle.dump(test, f)
f.close()

