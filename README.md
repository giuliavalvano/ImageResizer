# Image Resizer
This project builds a simple desktop application to resize images using Python and Tkinter.
The application allows users to upload an image, view its dimensions, define new dimensions, and save the resized image through a simple graphical interface.

---

## Features
* Upload image files
* Display uploaded image dimensions
* Resize images using custom width and height
* Save resized images
* Success popup after saving
* Dynamic interface updates
* Simple and lightweight GUI
* Modular project structure

---

## Technologies Used
* Python 3.14.5
* Tkinter
* Pillow
* Colour

---

## Project Structure
```text
ImageResizer/
│
├── main.py
├── window.py
├── image_resizer.py
│
├── img/
│   └── icons8-resize-50.png
│
└── README.md
```

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/giuliavalvano/ImageResizer.git
```

---

### 2. Enter the project folder
```bash
cd ImageResizer
```

---

### 3. Install dependencies
```bash
pip install pillow
pip install colour
```

---

## Running the Project
```bash
python main.py
```

---

## How It Works
The application:
1. Opens a graphical interface using Tkinter
2. Allows the user to upload an image
3. Displays the uploaded image dimensions
4. Receives new width and height values
5. Resizes the image using Pillow
6. Saves the resized image
7. Displays a success message and resets the interface

---

## Image Processing
The project uses the Pillow library to:
* Open images
* Read image dimensions
* Resize images
* Save resized files

---

## Interface Behavior
The interface dynamically changes during execution:
* The window expands after an image is uploaded
* Buttons change position and style
* Input fields appear for resizing
* The interface resets after saving the image
