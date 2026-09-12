# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 11:10:47 2024

@author: Nguyen Minh Triec
"""

import reflex as rx
from .components.actionbar import actionbar, bottombar
from .ifsstate import IfsState
from reflex.page import page


@page(route="/", title="IFS Home")
def index() -> rx.Component:
    
    return rx.center(
        # rx.color_mode.button(position="top-right"),
        actionbar(),
        
        rx.vstack(
            rx.image(IfsState.images[-1], max_width="71%"),
            # rx.text(IfsState.images[-1]),
            rx.hstack(
                rx.button(
                    "New Picture", 
                    variant="soft",
                    on_click=IfsState.show_ifs                    
                ),
                rx.button(
                    "Clear All",
                    variant='soft',
                    on_click=IfsState.clear_all
                )
            ),

                
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
        ),
        bottombar()
    )