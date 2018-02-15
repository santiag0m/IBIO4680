import numpy as np # Numeric arrays
import scipy.io # Import mat files
import cv2 # Image manipulation
import os # Directory listing
import fnmatch # Find extension files
import pickle
from subprocess import call # Run shell commands


# Dataset download

if not os.path.isdir(os.path.join(os.getcwd(),'BSR')):
    call(['wget','http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/BSR/BSR_bsds500.tgz'])
    call(['tar','-xf','BSR_bsds500.tgz'])

# Begin timer

tini = time.time()

# Dataset path

imagepath = os.path.join(os.getcwd(),'BSR','BSDS500','data','images','train')
truthpath = os.path.join(os.getcwd(),'BSR','BSDS500','data','groundTruth','train')

matches = []
for file in os.listdir(imagepath):
    if fnmatch.fnmatch(file,'*jpg'):
        matches.append(file)
images = matches

matches = []
for file in os.listdir(truthpath):
    if fnmatch.fnmatch(file,'*mat'):
        matches.append(file)
truth = matches

if len(images) != len(truth):
    error('Hay una cantidad distinta de etiquetas e imagenes')

# Random sampling

n = len(images)
idx = np.random.randint(0,n-1,7) # 7 random images

selected = []

for iidx in idx:
    img = cv2.imread(os.path.join(imagepath,images[iidx]))
    img = cv2.resize(img,(256,256))
    matvar = scipy.io.loadmat(os.path.join(truthpath,truth[iidx]))
    label = matvar['groundTruth']
    mdict = ['images':img,'truth':label]
    selected.append(mdict)

f = open('myimages','wb')
pickle.dump(selected,f)
f.close()

# End timer

print(time.time()-tini)
