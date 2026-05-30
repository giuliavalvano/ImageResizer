"""
image_resizer.py
Description: script to handle the image resizing functionality of the application.
    It contains the functions to open the image, resize it and save it.
Author: Giulia Valvano
Data: 29/05/2026
Version: 1.0
"""

# libraries
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import *
from colour import Color
from PIL import Image

def resize(image_resize, new_width, new_height, window, label_info, start_button, input_new_width, input_new_height, resize_button):
    # function to resize the image
    image_resized = image_resize.resize((new_width, new_height))

    # save the resized image
    image_resized_dir = asksaveasfilename()

    # if the user selects a directory, save the image and show a success message
    # at the end, reset the interface to allow the user to upload another image
    if image_resized_dir:
        image_resized.save(image_resized_dir + ".png")

        # success window
        success_window = Toplevel(window)

        # set the title and size of the success window
        success_window.title("Success")

        # set the size of the success window
        success_window.geometry("300x100")

        # make the success window not resizable
        success_window.resizable(False, False)

        # add a label to the success window
        Label(success_window, text="Image saved successfully!", font=("Bahnschrift 14")).pack(pady=30)

        # reset interface
        reset_interface(window, label_info, start_button, input_new_width, input_new_height, resize_button)


# function to open the image and show its dimensions
def abrir_imagem(window, frame_bottom, label_info, start_button, input_new_width, input_new_height):
    # open the file dialog to select an image
    dir_image = askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])

    # if an image is selected, open it and show its dimensions
    if dir_image:
        image_resize = Image.open(dir_image)
        width, height = image_resize.size

        # change the size of the window to show the dimensions
        window.geometry("350x270")

        # change the position of the button to show the dimensions
        start_button.place(x=0, y=145)
        start_button.config(text="Upload Another Image", bg=Color("#DBDBDB"), fg=Color("black"))

        # update the label to show the dimensions of the image
        label_info.config(text=f"Uploaded Image: {width}x{height}", font=("Bahnschrift 14"), fg=Color("black"), anchor="center", justify="center")
        label_info.place(x=10, y=5)

        # button to resize the image
        resize_button = Button(frame_bottom, text="Resize Image", font=("Bahnschrift 14"), bg=Color("#6761FF"), fg=Color("white"), 
                               command=lambda: resize(image_resize, int(input_new_width.get()), int(input_new_height.get()), 
                               window, label_info, start_button, input_new_width, input_new_height, resize_button)) 
        resize_button.place(x=100, y=98)


def reset_interface(window, label_info, start_button, input_new_width, input_new_height, resize_button):
    # restore original window size
    window.geometry("350x122")

    # clear label
    label_info.config(text="")

    # clear inputs
    input_new_width.delete(0, END)
    input_new_height.delete(0, END)

    # remove resize button
    resize_button.destroy()

    # restore upload button
    start_button.place(x=0, y=0)

    start_button.config(text="Upload Image", bg=Color("#6761FF"), fg=Color("white"))