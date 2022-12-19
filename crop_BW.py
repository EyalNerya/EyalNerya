import tkinter as tk
import os
from tkinter import filedialog
from PIL import Image, ImageTk

# Create the main window
window = tk.Tk()
window.title("Picture Cropper")

# Function to open a folder with pictures
def open_folder():
  # Ask the user to select a folder
  folder_path = filedialog.askdirectory()

  # Iterate through all the files in the folder
  for file in os.listdir(folder_path):
    # Check if the file is a picture
    if file.endswith(".jpg") or file.endswith(".png"):
      # Open the picture
      image = Image.open(os.path.join(folder_path, file))

      # Crop the picture to a square
      width, height = image.size
      if width > height:
        image = image.crop(((width - height) // 2, 0, (width + height) // 2, height))
      elif height > width:
        image = image.crop((0, (height - width) // 2, width, (height + width) // 2))

      # Convert the picture to black and white
      image = image.convert("L")

      # Save the modified picture
      image.save(os.path.join(folder_path, file))

# Create a button to open a folder with pictures
button = tk.Button(window, text="Open Folder", command=open_folder)
button.pack()

# Run the main loop
window.mainloop()
