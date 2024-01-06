import os
import shutil
import tkinter as tk
from difflib import SequenceMatcher

class FileOrganizerGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File Organizer")
        self.root.geometry("500x200")

        self.label = tk.Label(self.root, text="Enter path to organize:", font=("Arial", 12))
        self.label.pack(pady=10)

        self.textBox = tk.Entry(self.root, width=50, font=("Arial", 10))
        self.textBox.pack(pady=10)

        self.button = tk.Button(self.root, text="Organize", font=("Arial", 14), command=self.fileOrganize)
        self.button.pack(pady=20)

        self.root.mainloop()

    def similar(a, b):
        return SequenceMatcher(None, a, b).ratio()

    def fileOrganize(self):
        path = self.textBox.get().strip()
        if not path:
            print("Please enter a valid path.")
            return

        files = os.listdir(path)

        for file in files:
            filename, extension = os.path.splitext(file)
            extension = extension[1:]
            destination_folder = os.path.join(path, extension)

            if os.path.exists(destination_folder):
                shutil.move(os.path.join(path, file), os.path.join(destination_folder, file))
            else:
                os.makedirs(destination_folder)
                shutil.move(os.path.join(path, file), os.path.join(destination_folder, file))

        print("Organized!")
        return
    
file_organizer = FileOrganizerGUI()