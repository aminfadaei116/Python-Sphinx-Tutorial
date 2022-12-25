"""
DatabaseSetingsModule
----------------------
This is a Module which has Class for Database and database Settings
"""

import numpy as np
from numpy import save
import math as m
import matplotlib.pyplot as plt
import torch.nn as nn
import torch
import torch.nn.functional as F
import cv2


def createMask(keys, height, width, img=None):
    
    if img != None:
      newImg = img.clone().detach().to(DEVICE)
      newImg[:, (height*keys[:, 1]).long(), (width*keys[:, 0]).long()] = 255.0
      return newImg
    else: 
      mask = torch.zeros((height, width), device=DEVICE)
      mask[(height*keys[:, 1]).long(), (width*keys[:, 0]).long()] = 1
      return mask



def TransformKeys(keys, euler, T):
    R = torch.linalg.multi_dot((Rx(euler[0]), Ry(euler[1]), Rz(euler[2])))
    center = torch.mean(keys, dim=0)
    keys = keys - center
    out = torch.matmul(keys, R)
    return out + center + T
    
def Rx(theta):
    return torch.tensor([[ 1, 0           , 0           ],
                   [ 0, torch.cos(theta),-torch.sin(theta)],
                   [ 0, torch.sin(theta), torch.cos(theta)]], device=DEVICE, dtype=torch.double)
  
def Ry(theta):
    return torch.tensor([[ torch.cos(theta), 0, torch.sin(theta)],
                   [ 0           , 1, 0           ],
                   [-torch.sin(theta), 0, torch.cos(theta)]], device=DEVICE, dtype=torch.double)
  
def Rz(theta):
    return torch.tensor([[ torch.cos(theta), -torch.sin(theta), 0 ],
                   [ torch.sin(theta), torch.cos(theta) , 0 ],
                   [ 0           , 0            , 1 ]], device=DEVICE, dtype=torch.double)