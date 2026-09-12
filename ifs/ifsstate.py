# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 10:46:13 2024

@author: Nguyen Minh Triec
"""

import reflex as rx
import numpy as np

import PIL.Image
from .utils import create_ifs, get_demo


class IfsState(rx.State):
    
    dcrt: list[float] = [.6, .3, .1]
    images: list[PIL.Image.Image] = [get_demo()]

    @rx.event  
    def show_ifs(self):
        rng = np.random.default_rng()
        conversion_x = rng.random((3, 3))/1.0
        conversion_y = rng.uniform(-1, 1, (3, 3))/1.5
                      
        img = create_ifs(self.dcrt, conversion_x, conversion_y)
        if len(self.images) == 5: self.images = self.images[1:]
        self.images = self.images + [img]
        
        
    @rx.event    
    def clear_all(self):
        self.images = [get_demo()]
       
        
        