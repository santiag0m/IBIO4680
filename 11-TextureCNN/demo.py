import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import numpy as np

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 50, 3) # One input channel - grayscale
        self.conv2 = nn.Conv2d(50, 90, 6)
        self.conv3 = nn.Conv2d(90, 120, 5)
        self.conv4 = nn.Conv2d(120, 250, 5, stride=(5,5)) 
        self.fc1 = nn.Linear(250, 80)
        self.fc2 = nn.Linear(80, 25)#25 classes
        self.pool = nn.MaxPool2d(2, 2)
        self.bn1 = nn.BatchNorm2d(50)
        self.bn2 = nn.BatchNorm2d(90)
        self.bn3 = nn.BatchNorm2d(120)
        self.bn4 = nn.BatchNorm2d(250)
        self.bn5 = nn.BatchNorm2d(80)
        self.dp = nn.Dropout()

    def forward(self, x, verbose=True):#128x128
        if verbose: print('Input size: {}'.format(x.size()))
        x = self.pool(F.relu(self.conv1(x)))#63x63
        x = self.bn1(x)
        if verbose: print('Conv. Block 1 size: {}'.format(x.size()))
        x = self.pool(F.relu(self.conv2(x)))#29x29
        x = self.bn2(x)
        if verbose: print('Conv. Block 2 size: {}'.format(x.size()))
        x = self.pool(F.relu(self.conv3(x)))#12x12
        x = self.bn3(x)
        if verbose: print('Conv. Block 3 size: {}'.format(x.size()))
        x = self.pool(F.relu(self.conv4(x)))#1x1
        x = self.bn4(x)
        if verbose: print('Conv. Block 4 size: {}'.format(x.size()))
        x = x.view(-1, 250)
        x = F.relu(self.fc1(x))
        if verbose: print('FC1 size: {}'.format(x.size()))
        x = self.bn5(x)
        x = self.dp(x)
        if verbose: print('FC2 size: {}'.format(x.size()))
        x = self.fc2(x)
        if verbose: print('Output size: {}'.format(x.size()))
        x = F.softmax(x,dim=1)
        return x

x = Variable(torch.randn(1,3,128,128))
model = Net()
print('------------------Net architecture------------------')
print('\n')
print(model)
print('\n')
model.eval()
print('---------------------Outputs------------------------')
print('\n')
y = model(x)
d = model.state_dict()
print('\n')
print('---------------------Parameters---------------------')
print('\n')
cum = 0
for key in list(d.keys()):
    pnum = np.prod(d[key].numpy().shape)
    cum += pnum
    print('Name:\t'+key+'\tNum_Params:\t{}'.format(pnum))
print('Total parameters: \t {}'.format(cum))
print('\n')
