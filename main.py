"""
main.py
Description: Python script to create a GUI application for resizing images using the Tkinter library.
Author: Giulia Valvano
Data: 29/05/2026
Version: 1.0
"""

# libraries
from tkinter import *
from colour import Color
from window import create_window
from image_resizer import abrir_imagem

# calling the function to create the window layout
window, frame_bottom, label_info, input_new_width, input_new_height = create_window()

# button to open the file dialog to select an image
start_button = Button(frame_bottom, text="Upload Image", font=("Bahnschrift 14"), bg=Color("#6761FF"), fg=Color("white"),
                          command=lambda: abrir_imagem(window, frame_bottom, label_info, start_button, input_new_width, input_new_height), width=31)
start_button.place(x=0, y=0)

window.mainloop()