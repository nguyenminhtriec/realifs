# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 10:09:17 2024

@author: Nguyen Minh Triec
"""


import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image



def rand_discrete(a):
    sum = 0.0
    i = 0
    r = np.random.random()
    for i in range(len(a)):
        sum += a[i]
        
        if r < sum:
            # print (r, sum, i)
            return i
        
        
def create_ifs(discrete, cx, cy):
    x, y = (0.0, 0.0)
    X = []
    Y = []
       
    for i in range(20000):
        r = rand_discrete(discrete)
        try:
            x0 = cx[r][0]*x + cx[r][1]*y + cx[r][2]
            y0 = cy[r][0]*x + cy[r][1]*y + cy[r][2] 
        except OverflowError:           
            continue
        x = x0
        y = y0
        X.append(x)
        Y.append(y)
    
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.axis('off') # not showing x-axis and y-axis
    ax.scatter(X, Y, linewidth=0, s=.7)
       
    bio = BytesIO()
    fig.savefig(bio, dpi=100, facecolor='#FFDDFF')  
    img_created = Image.open(bio)

    plt.close()
    return img_created     


def get_demo():
    fp = open("assets/vase.png", "rb")        
    return Image.open(fp)