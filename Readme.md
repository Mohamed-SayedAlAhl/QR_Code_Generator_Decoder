# QR King

## Overview
This project is a Python script that allows users to generate and decode QR codes. It provides a user-friendly graphical user interface that allows users to enter text and generate a QR code, or select a QR code image and decode it to obtain the original text. The script utilizes the `pyqrcode`, `png`, `pyzbar`, `PIL`, `tkinter`, `filedialog`, `sys`, and `os` libraries to perform its functions.

## Getting Started
To get started with this project, you will need to have Python 3 installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

You will also need to install the following libraries:
- pyqrcode
- png
- pyzbar
- PIL
- tkinter

You can install these libraries using the following command:
```
pip install pyqrcode png pyzbar Pillow
```
Alternatively, you can download and use the pre-built executable file for this project, which does not require the installation of Python or any libraries.

## Usage
To use this script, run the `QR_Code_Generator_Decoder.py` file using Python or double-click the executable file. The graphical user interface will appear, allowing you to choose between generating a QR code or decoding a QR code image.

### Generate QR Code
To generate a QR code, enter the desired text into the text entry field and click the "Generate" button. The generated QR code will be saved as a PNG image file named "QR Code.png" in the same directory as the script.

### Decode QR Code
To decode a QR code, click the "Select QR Code Image" button and choose a QR code image file. The decoded text will be displayed in the result label, and you can click the "Copy Result" button to copy the text to the clipboard.

## Functionality
This project provides a simple and user-friendly way to generate and decode QR codes. The GUI allows users to easily enter text or choose an image file, and the QR code is generated or decoded quickly and accurately. The script is also easily customizable, allowing users to modify the code to suit their specific needs.

## Conclusion
In conclusion, this project provides a convenient way to generate and decode QR codes. Whether you are using the Python script or the pre-built executable file, this project is a useful tool for anyone who needs to work with QR codes.