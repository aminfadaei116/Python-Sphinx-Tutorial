"""
NeuralNetworkModule
----------------------
This is a Module which has the network model in it
"""

import numpy as np
from numpy import save
import math as m
import matplotlib.pyplot as plt
import torch.nn as nn
import torch.nn.functional as F
import cv2

class MyNet(object):
    """Database Class which is responsile for connecting to databse """
    def __init__(self, first_layer, last_layer):
        """
        This is connection string o connect to sql server
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
        This method is the output of the network
        :return: torch.tensor
        """
        return self.layers(x)

  