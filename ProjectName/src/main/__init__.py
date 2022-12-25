"""
NeuralNetworkModule
----------------------
This is our Network model
"""

import numpy as np
from numpy import save
import math as m
import matplotlib.pyplot as plt
import torch.nn as nn
import torch.nn.functional as F
import cv2

class MyNet(object):
    """Network Class made of several conv layers followed by RelU activation function"""
    def __init__(self, first_layer, last_layer):
        """
        This is creating the network model based on parameters
        :param in_channels: int
        :param out_channels: int
        :param kernel_size: int
        :param padding: int
        """
        super(MyNet, self).__init__()
        self.layers = nn.Sequential(
            nn.Conv2d(in_channels=first_layer, out_channels=8,kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=8, out_channels=8,kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=8, out_channels=8,kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=8, out_channels=8,kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=8, out_channels=8,kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=8, out_channels=last_layer,kernel_size=3, padding=1),
        )
        self.id = nn.Identity()

    def forward(self, x):
        """
        This method will return the output of the network after we passed an input
        :return: torch.tensor
        """
        return self.layers(x)

  