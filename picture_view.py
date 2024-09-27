import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

class Sabrihin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sabrihin")
        self.geometry("800x600")

        # Create a gradient blur background
        self.canvas = tk.Canvas(self, width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        for x in range(800):
            self.canvas.create_rectangle(x, 0, x+1, 600, fill=f"#{hex(int(x/8))[-2:]}{hex(int(x/8))[-2:]}{hex(int(x/8))[-2:]}")

        # Prompt for folder or picture selection
        self.folder_path = None
        self.image_path = None
        self.prompt_label = tk.Label(self, text="Select a folder or image:")
        self.prompt_label.pack(pady=10)
        self.folder_button = tk.Button(self, text="Select Folder", command=self.select_folder)
        self.folder_button.pack(side=tk.LEFT, padx=5)
        self.image_button = tk.Button(self, text="Select Image", command=self.select_image)
        self.image_button.pack(side=tk.LEFT, padx=5)

        # Image display area
        self.image_label = tk.Label(self)
        self.image_label.pack(fill=tk.BOTH, expand=True)

        # Zoom controls
        self.zoom_factor = 1.0
        self.zoom_in_button = tk.Button(self, text="+", command=self.zoom_in)
        self.zoom_in_button.pack(side=tk.LEFT, padx=5)
        self.zoom_out_button = tk.Button(self, text="-", command=self.zoom_out)
        self.zoom_out_button.pack(side=tk.LEFT, padx=5)

    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            self.load_images_from_folder()

    def select_image(self):
        self.image_path = filedialog.askopenfilename()
        if self.image_path:
            self.load_image()

    def load_images_from_folder(self):
        # Implement logic to load images from the selected folder
        # ...

    def load_image(self):
        try:
            image = Image.open(self.image_path)
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo  # Keep a reference to prevent garbage collection
        except Exception as e:
            print("Error loading image:", e)

    def zoom_in(self):
        self.zoom_factor *= 1.1
        self.display_image()

    def zoom_out(self):
        self.zoom_factor *= 0.9
        self.display_image()

    def display_image(self):
        # Implement logic to display the image with the current zoom factor
        # ...

if __name__ == "__main__":
    app = Sabrihin()
    app.mainloop()
