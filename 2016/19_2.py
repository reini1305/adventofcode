#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 08:31:42 2016

@author: root
"""

def winner(n):
    w = 1;
    for i in range(1,n):
        w = w % i + 1;
        if (w > (i + 1)/2):
            w = w + 1
    return w


print winner(3014387)