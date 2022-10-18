#!/usr/bin/env python
# encoding: utf-8

import torch
import torch.nn as nn
import torch.nn.functional as F


class music_net(nn.Module):
    def __init__(self):
        """Intitalize neural net layers"""
        super(music_net, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=8, kernel_size=3, stride=1, padding=0)
        self.conv2 = nn.Conv2d(in_channels=8, out_channels=16, kernel_size=3, stride=1, padding=0)
        self.conv3 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=0)
        self.conv4 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=0)
        self.conv5 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=0)
        self.fc1 = nn.Linear(in_features=29952, out_features=28)

        self.batchnorm1 = nn.BatchNorm2d(num_features=8)
        self.batchnorm2 = nn.BatchNorm2d(num_features=16)
        self.batchnorm3 = nn.BatchNorm2d(num_features=32)
        self.batchnorm4 = nn.BatchNorm2d(num_features=64)
        self.batchnorm5 = nn.BatchNorm2d(num_features=128)

        self.dropout = nn.Dropout(p=0.3, inplace=False)

    def forward(self, feed_dict):
        x = feed_dict['image']
        # Conv layer 1.
        x = self.conv1(x)
        x = self.batchnorm1(x)
        x = F.relu(x)
        x = F.max_pool2d(x, kernel_size=2)

        # Conv layer 2.
        x = self.conv2(x)
        x = self.batchnorm2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, kernel_size=2)

        # Conv layer 3.
        x = self.conv3(x)
        x = self.batchnorm3(x)
        x = F.relu(x)
        x = F.max_pool2d(x, kernel_size=2)

        # Conv layer 4.
        x = self.conv4(x)
        x = self.batchnorm4(x)
        x = F.relu(x)
        x = F.max_pool2d(x, kernel_size=2)

        # Conv layer 5.
        x = self.conv5(x)
        x = self.batchnorm5(x)
        x = F.relu(x)
        x = F.max_pool2d(x, kernel_size=2)

        # Fully connected layer 1.
        x = torch.flatten(x, 1)
        x = self.dropout(x)
        x = self.fc1(x)
        pred = F.softmax(x, dim=-1)

        monitors = {}
        output_dict = {'pred': pred}

        pred_class = torch.argmax(pred, 1)
        accuracy = (pred_class == feed_dict['target'].argmax()).float().mean()
        monitors['accuracy-1'] = accuracy

        if self.training:
            loss = F.cross_entropy(x, feed_dict['target'])
            return loss, monitors, output_dict
        else:
            output_dict['monitors'] = monitors
            return output_dict
