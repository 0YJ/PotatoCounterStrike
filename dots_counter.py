import cv2
import os
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from matplotlib import pyplot as plt
import webbrowser

class PotatoDotsCounterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Automatic Potato Dots Counter")
        self.root.configure(bg="pink")

        self.folder_path = ''
        self.output_folder = ''
        self.threshold_step = 1
        self.blob_color = 0
        self.inertia_ratio = 0.2

        self.create_widgets()
        self.add_logo()
        self.add_author_link()

    def create_widgets(self):
        # Buttons
        self.open_folder_button = tk.Button(self.root, text="Show me your Potatos", command=self.open_folder)
        self.open_folder_button.pack()

        self.choose_output_folder_button = tk.Button(self.root, text="Where u wanna save?", command=self.choose_output_folder)
        self.choose_output_folder_button.pack()

        self.run_button = tk.Button(self.root, text="Do magic!", command=self.run_detection)
        self.run_button.pack()

        self.exit_button = tk.Button(self.root, text="See you next time!", command=self.root.quit)
        self.exit_button.pack()

        # ThresholdStep slider
        self.threshold_step_label = tk.Label(self.root, text="smaller = more dots!:")
        self.threshold_step_label.pack()
        self.threshold_step_slider = ttk.Scale(self.root, from_=1, to=10, orient=tk.HORIZONTAL, command=self.update_threshold_step)
        self.threshold_step_slider.pack()

        # BlobColor entry
        self.blob_color_label = tk.Label(self.root, text="which color of your potato? (0=black, 255=white):")
        self.blob_color_label.pack()
        self.blob_color_entry = tk.Entry(self.root)
        self.blob_color_entry.pack()

        # InertiaRatio slider
        self.inertia_ratio_label = tk.Label(self.root, text="How round your dots are?:")
        self.inertia_ratio_label.pack()
        self.inertia_ratio_slider = ttk.Scale(self.root, from_=0, to=1, orient=tk.HORIZONTAL, command=self.update_inertia_ratio)
        self.inertia_ratio_slider.pack()
    def add_logo(self):
        logo_path = "/home/luna/pota/saved.png"
        if os.path.exists(logo_path):
            self.logo_img = tk.PhotoImage(file=logo_path)
            self.logo_label = tk.Label(self.root, image=self.logo_img, bg="pink")
            self.logo_label.pack()
    def add_author_link(self):
        author_label = tk.Label(self.root, text="AUTHOR: Yujie Zhang", fg="purple", cursor="hand2")
        author_label.pack()
        author_label.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/0yj"))

    def open_folder(self):
        self.folder_path = filedialog.askdirectory()
        messagebox.showinfo("Folder Selected", f"Selected folder: {self.folder_path}")

    def choose_output_folder(self):
        self.output_folder = filedialog.askdirectory()
        messagebox.showinfo("Output Folder Selected", f"Selected output folder: {self.output_folder}")

    def update_threshold_step(self, val):
        self.threshold_step = float(val)

    def update_inertia_ratio(self, val):
        self.inertia_ratio = float(val)

    def run_detection(self):
        if not self.folder_path or not self.output_folder:
            messagebox.showerror("Error", "Please select input and output folders.")
            return

        image_files = [os.path.join(self.folder_path, f) for f in os.listdir(self.folder_path) if os.path.isfile(os.path.join(self.folder_path, f))]

        for image_file in image_files:
            image = cv2.imread(image_file)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gauss = cv2.GaussianBlur(gray, (9,9), 0)

            params = cv2.SimpleBlobDetector_Params()
            params.minThreshold= 10
            params.maxThreshold = 255
            params.thresholdStep = self.threshold_step

            params.filterByColor = True
            params.blobColor = int(self.blob_color_entry.get()) if self.blob_color_entry.get() else 0

            params.filterByArea = True
            params.minArea = 20
            params.maxArea=2000

            params.filterByCircularity = True
            params.minCircularity = 0.3

            params.filterByConvexity = True
            params.minConvexity = 1.0

            params.filterByInertia = True
            params.minInertiaRatio = self.inertia_ratio

            detector = cv2.SimpleBlobDetector_create(params)
            keypoints = detector.detect(gauss)
            print("Detected %d dots in %s" % (len(keypoints), image_file))

            im_with_keypoints = cv2.drawKeypoints(image, keypoints, np.array([]), (0, 0, 255),
                                                   cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

            filename = os.path.splitext(os.path.basename(image_file))[0]
            output_file = os.path.join(self.output_folder, f"{filename}_result.jpg")
            cv2.imwrite(output_file, im_with_keypoints)
            print("Result saved to", output_file)

        messagebox.showinfo("Detection Completed", "All images processed and saved.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = PotatoDotsCounterGUI(root)
    app.run()
