"""
window.py
Description: script to create the main window of the application and its layout. 
    It contains the function to create the window and its widgets.
Author: Giulia Valvano
Data: 29/05/2026
Version: 1.0
"""

# libraries
from tkinter import *
from colour import Color
from PIL import Image, ImageTk

def create_window():
    # create the main window
    window = Tk()

    # set the title of the window
    window.title("Image Resizer")

    # set the size of the window
    window.geometry("350x122")
    window.resizable(False, False)

    # creating frames for better organization of the widgets
    frame_top = Frame(window, width=350, height=80, bg=Color("#EDEDED"), borderwidth=1, relief="sunken")
    frame_top.grid(row=0, column=0, padx=0, pady=1, sticky="nsew")

    frame_bottom = Frame(window, width=350, height=200, bg=Color("#F5F5F5"), borderwidth=1, relief="sunken")
    frame_bottom.grid(row=1, column=0, padx=0, pady=1, sticky="nsew")

    # setting images icons
    image_resize_icon = Image.open("img/icons8-resize-50.png")
    image_resize_icon = image_resize_icon.resize((50, 50)) 
    image_resize_icon = ImageTk.PhotoImage(image_resize_icon)

    # creating labels for the top frame
    top_image_label = Label(frame_top, height=60, image=image_resize_icon, compound=LEFT, padx=10, anchor="nw", bg=Color("#EDEDED"))
    top_image_label.image = image_resize_icon
    top_image_label.place(x=20, y=15)

    top_title_label = Label(frame_top, height=60, text="Image Resizer", font=("Bahnschrift 26"), anchor=NE, bg=Color("#EDEDED"), fg=Color("black"))
    top_title_label.place(x=90, y=15)

    # label info to show the dimensions of the image
    label_info = Label(frame_bottom, text="",  font=("Bahnschrift 12"), bg=Color("#F5F5F5"))
    label_info.place(x=10, y=40)

    # input new dimensions of the image labels
    # Width 
    label_new_width = Label(frame_bottom, text="Type New Width:", font=("Bahnschrift 12"), bg=Color("#F5F5F5"))
    label_new_width.place(x=10, y=40)

    input_new_width = Entry(frame_bottom, width=13, font=("Bahnschrift 12"), bg=Color("white"))
    input_new_width.place(x=12, y=65)

    # Height
    label_new_height = Label(frame_bottom, text="Type New Height:", font=("Bahnschrift 12"), bg=Color("#F5F5F5"))
    label_new_height.place(x=200, y=40)

    input_new_height = Entry(frame_bottom, width=13, font=("Bahnschrift 12"), bg=Color("white"))
    input_new_height.place(x=203, y=65)

    return window, frame_bottom, label_info, input_new_width, input_new_height