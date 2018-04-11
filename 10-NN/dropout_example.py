import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
	super(Net, self).__init__()

    def forward(self, x):
        return F.dropout(x, 0.5, training=self.training)

class Net1(nn.Module):
    def __init__(self):
	super(Net1, self).__init__()
	self.dropout=nn.Dropout()

    def forward(self, x):
        return self.dropout(x)
