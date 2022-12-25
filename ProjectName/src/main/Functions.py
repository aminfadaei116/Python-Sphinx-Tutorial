"""
Functions Script
----------------------
This is the needed function for our process
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
    """
    This will create a mask which only has value at the keypoint locations
    :param keys: torch.tensor
    :param height: int
    :param width: int
    :param img: torch.tensor
    """
    if img != None:
      newImg = img.clone().detach().to(DEVICE)
      newImg[:, (height*keys[:, 1]).long(), (width*keys[:, 0]).long()] = 255.0
      return newImg
    else: 
      mask = torch.zeros((height, width), device=DEVICE)
      mask[(height*keys[:, 1]).long(), (width*keys[:, 0]).long()] = 1
      return mask



def TransformKeys(keys, euler, T):
    """
    This function will apply 3D transformation over the keypoints
    :param keys: torch.tensor
    :param euler: torch.tensor
    :param T: torch.tensor
    """
    R = torch.linalg.multi_dot((Rx(euler[0]), Ry(euler[1]), Rz(euler[2])))
    center = torch.mean(keys, dim=0)
    keys = keys - center
    out = torch.matmul(keys, R)
    return out + center + T
    
