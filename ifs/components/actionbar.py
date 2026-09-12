# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:19:00 2024

@author: Nguyen Minh Triec
"""

import reflex as rx
from .. import styles
from .menu import drop_down_menu
from reflex.style import toggle_color_mode


def actionbar() -> rx.Component:
    """Action bar.

    Returns:
        The Action bar component.
    """
    return rx.hstack(
        
        rx.hstack(
            # The logo.
            rx.color_mode_cond(
                rx.image(src="/reflex_black.svg"),
                rx.image(src="/reflex_white.svg"),
            ),
            
            rx.link(                
                rx.icon(
                    "home",
                    color=rx.color('mauve', 10)
                ),
                box_shadow=styles.box_shadow,
                bg="transparent",
                border_radius=styles.border_radius,
                _hover={
                    "bg": styles.accent_color,
                },                
                href="/",
            ),
            spacing='5',
            align='center',
            
        ),
        
        rx.hstack(
            rx.link(
                rx.button(
                    rx.icon(tag="images", color=rx.color("accent", 10)),                
                    variant='soft',
                    size='1',
                ),
                href='/show_all'
            ),
            rx.link(
                rx.button(
                    rx.icon(tag="messages-square", color=rx.color("accent", 10)),                
                    variant='soft',
                    size='1',
                ),
                href='#'
            ),
            rx.button(
                # rx.icon('sun-moon', color=rx.color('accent', 10)),
                rx.color_mode.icon(),
                variant='soft',
                size='1',
                on_click=toggle_color_mode,
            ),
            drop_down_menu(
                rx.button(
                    rx.icon(
                        tag="menu",
                        color=rx.color("accent", 10),
                    ),
                    size='1',
                    variant='soft',
                ),    
            ),          
            align='center',
            spacing='3',            
        ),
        position='fixed',
        top='0',
        width="100%",
        height='5vh',
        align="center",
        justify='between',        
        padding_x='1em',                
        background_color=rx.color('accent', 2),
        z_index="100"
    )
        
    
def bottombar() -> rx.Component:
    """Bottom bar or Footer.

    Returns: 
        Bottom bar or Footer component.
    """
    return rx.hstack(
        rx.hstack(
            rx.text("*Pictures created using IFS", size='1', color_scheme='gray'),            
        ),
        rx.hstack(
            rx.icon("circle", size=7),
            rx.link(
                rx.text("About us", size='1'), 
                href="https://nguyenminhtriec.github.io", style=styles.link_style)
        ),
        position='fixed',
        bottom='0',
        width="100%",
        height='5vh',        
        padding_x=".5em",
        align='center',
        justify='between',
        background_color=rx.color('accent', 2),
        z_index='100' 
    )