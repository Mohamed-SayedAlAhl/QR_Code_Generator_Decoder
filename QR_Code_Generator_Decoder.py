import pyqrcode
import png
from pyzbar.pyzbar import decode
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import sys
import os

def resource_path(relative_path):
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__))
    )
    return os.path.join(base_path, relative_path)

def generate_qr_code():
    text = text_entry.get()
    if not text.strip():
        result_label.config(text="Please enter a text to generate QR Code.")
        return
    qr_code = pyqrcode.create(text)
    qr_code.png("QR Code.png", scale=5)
    result_label.config(text="QR Code generated successfully!")

def decode_qr_code():
    image_path = filedialog.askopenfilename()
    decoded_qr = decode(Image.open(image_path))
    result_label.config(text=decoded_qr[0].data.decode('ascii'))
    copy_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

def copy_result():
    root.clipboard_clear()
    root.clipboard_append(result_label.cget("text"))

def show_generate_frame():
    decode_frame.grid_forget()
    generate_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

def show_decode_frame():
    generate_frame.grid_forget()
    decode_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create the main window
root = tk.Tk()
root.title("QR King")

# Set the icon for the main window
root.iconbitmap(resource_path('icon.ico'))

# Create and place widgets
choice_label = tk.Label(root, text="Choose an action:")
choice_label.grid(row=0, column=0, padx=10, pady=10)

generate_choice_button = tk.Button(root, text="Generate QR Code", command=show_generate_frame)
generate_choice_button.grid(row=0, column=1, padx=10, pady=10)

decode_choice_button = tk.Button(root, text="Decode QR Code", command=show_decode_frame)
decode_choice_button.grid(row=0, column=2, padx=10, pady=10)

generate_frame = tk.Frame(root)
text_label = tk.Label(generate_frame, text="Enter text to generate QR Code:")
text_label.grid(row=0, column=0, padx=10, pady=10)

text_entry = tk.Entry(generate_frame)
text_entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = tk.Button(generate_frame, text="Generate", command=generate_qr_code)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

decode_frame = tk.Frame(root)
decode_button = tk.Button(decode_frame, text="Select QR Code Image", command=decode_qr_code)
decode_button.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

copy_button = tk.Button(root, text="Copy Result", command=copy_result)

# Start the main loop
root.mainloop()