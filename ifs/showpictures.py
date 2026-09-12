# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 11:22:34 2024

@author: Nguyen Minh Triec
"""

import reflex as rx
from .components.actionbar import actionbar, bottombar
from reflex.page import page

from .ifsstate import IfsState

@page(route="/show_all", title="IFS Pictures")
def all_pictures() -> rx.Component:
    return rx.center(
        rx.vstack(
            actionbar(),
            
            rx.vstack(
                rx.foreach(
                    IfsState.images, lambda img: rx.image(img)
                )
            ),
            
            bottombar(),
            
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
        )
        
    )

