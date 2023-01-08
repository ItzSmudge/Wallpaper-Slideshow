from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import ctypes
import time
import os

index = 0
default_dir = os.path.join(os.path.expanduser("~"), "Pictures")

interval_text = ["1 minute ",
                 "10 minutes",
                 "1 hour",
                 "6 hours"
                 ]

interval_list = [1, 600, 3600, 21600]

bg_color = "#292626"
obj_bg_color = "#383736"
fg_color = "#c9bab9"
font = ("Roboto Mono", 16, "bold")

def change_wallpaper():
    try:
        duration = interval_list[interval_text.index(interval.get())]
        if len(image_files) > 0:
            while True:
                for i in image_files:
                    ctypes.windll.user32.SystemParametersInfoW(20, 0, i, 0)
                    time.sleep(duration)
        elif not image_files:
            pass
            tkinter.messagebox.showerror("Error", "Selected folder cannot be used")
    except NameError:
        tkinter.messagebox.showerror("Error", "A folder has not been selected")


def browseFiles():
    global image_files
    image_files = []

    try:
        folder = filedialog.askdirectory(initialdir=default_dir,
                                         title="Select a Folder")
        folder_path.set(folder)
        path["text"] = folder

        image_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".jfif")]

    except FileNotFoundError:
        pass

def custom_duration():
    window = Tk()
    window.resizable(False, False)
    custom_interval = StringVar()

    sub_title = Label(root, text="Enter custom duration (minutes)", font=("Roboto Mono", 10, "bold"), width=30, fg=fg_color,bg=bg_color)
    sub_title.pack()

    duration_entry = Entry(window, textvariable=custom_interval, font=font, width=20)
    duration_entry.pack()

    confirm_button = Button(text="Confirm", command=lambda: change_wallpaper(),
                            bg=obj_bg_color, fg=fg_color, font=font, width=20)
    confirm_button.pack()

    window.mainloop()


root = Tk()

root.geometry("300x160")
root.resizable(False, False)
root.configure(bg=bg_color)
root.title("Dynamic Wallpaper")
root.iconbitmap("icon.ico")

folder = StringVar()
folder_path = StringVar()
interval = StringVar()

interval.set(interval_text[0])
interval_menu = OptionMenu(root, interval, *interval_text)
interval_menu.configure(bg=obj_bg_color, fg=fg_color, font=font, width=30)
interval_menu["menu"].config(bg=obj_bg_color, fg=fg_color, font=("Roboto Mono", 16, "bold"))
interval_menu.grid(padx=100, pady=0, sticky=S+N+E+W)
interval_menu.pack()

confirm_button = Button(text="Confirm", command=lambda : change_wallpaper(),
                        bg=obj_bg_color, fg=fg_color, font=font, width=30)
confirm_button.pack()

open_explorer = Button(text="Select Folder", command=lambda : browseFiles(),
                       bg=obj_bg_color, fg=fg_color, font=font, width=30)
open_explorer.pack()

path_title = Label(root, text="Selected Folder:", font=("Roboto Mono", 10, "bold"),
                   width=30, fg=fg_color, bg=bg_color)
path_title.pack()

path = Label(root, text="", font=("Roboto Mono", 10, "bold"),
             width=30, fg=fg_color, bg=bg_color)
path.pack()

root.mainloop()