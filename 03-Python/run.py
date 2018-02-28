import numpy as np # Numeric arrays
import scipy.io # Import mat files
import cv2 # Image manipulation
import os # Directory listing
import fnmatch # Find extension files
import pickle # File IO
import time # Time ...
import matplotlib.pyplot as plt
from subprocess import call # Run shell commands
from imutils import build_montages
from shutil import copyfile

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
for imp in images:
    trp = imp[:-3]+'mat'
    matches.append(trp)
truth = matches

if len(images) != len(truth):
    error('Hay una cantidad distinta de etiquetas e imagenes')

# Random sampling

n = len(images)
idx = np.random.randint(0,n-1,7) # 7 random images

if not os.path.isdir(os.path.join(os.getcwd(),'Image_selected')):
   call(['mkdir','Image_selected'])



selected = []
dictionary = {}
dictionary.setdefault('Original', [])
for iidx in idx:
    img = cv2.imread(os.path.join(imagepath,images[iidx]))
    img = cv2.resize(img,(256,256))
    copyfile(os.path.join(imagepath,images[iidx]), os.path.join(os.getcwd(),'Image_selected',images[iidx]))
    selected.append(img)
    dictionary['Original'].append(img)

dictionary.setdefault('Annotation', [])
for iidx in idx:
    matvar = scipy.io.loadmat(os.path.join(truthpath,truth[iidx]))
    label = matvar['groundTruth']
    annotation = label[0][0][0][0][0]
    annotation = np.round(annotation - np.min(annotation))*(255/(np.max(annotation)-np.min(annotation)))
    annotation = cv2.applyColorMap(np.uint8(annotation), cv2.COLORMAP_HSV)
    selected.append(annotation)
    dictionary['Annotation'].append(annotation)

montages = build_montages(selected, (256, 256), (7, 2))


for montage in montages:
    plt.imshow(cv2.cvtColor(montage, cv2.COLOR_BGR2RGB))
    plt.show()
       
f = open(os.path.join(os.getcwd(),'Image_selected','dictionary'),'wb')
pickle.dump(dictionary,f)
f.close()

# End timer

print(time.time()-tini)
