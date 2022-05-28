# Clicker Game
# by xP9nda

# Imports
import tkinter
import customtkinter as ct
import os
from PIL import Image, ImageTk

# Variables
PATH = os.path.dirname(os.path.realpath(__file__))
IMG_SIZE = 22

# Customisation
ct.set_appearance_mode("dark")
ct.set_default_color_theme("blue")

# App Class
class App(ct.CTk):

    # When the app first loads
    def __init__(self):
        super().__init__()

        self.title("Clicker Game by xP9nda")
        self.attributes("-fullscreen", True)

        self.protocol("WM_DELETE_WINDOW", self.stop)

        # Configure the grid layout
        self.grid_columnconfigure(1, weight = 1)
        self.grid_rowconfigure(0, weight = 1)

        # Left sidebar
        self.left_sidebar = ct.CTkFrame(master = self,
                                        width = 200,
                                        corner_radius = 0)
        self.left_sidebar.grid(row = 0, column = 0, stick = "nswe")

        # configure left sidebar grid layout
        self.left_sidebar.grid_rowconfigure(0, minsize = 10)
        # make row 5 the entire size to allow placing things at the bottom
        self.left_sidebar.grid_rowconfigure(5, weight = 1)

        # Text titles on left sidebar
        self.title = ct.CTkLabel(master = self.left_sidebar,
                                 text = "Clicker Game\nby xP9nda",
                                 text_font = ("Verdana", -16))
            # https://stackoverflow.com/questions/23777139/how-to-derive-the-font-size-from-a-height-constraint
        self.title.grid(row = 1, column = 0, padx = 10, pady = 10)

        self.title_version = ct.CTkLabel(master = self.left_sidebar,
                                         text = "v0",
                                         text_font = ("Verdana", -12))
        self.title_version.grid(row = 2, column = 0, padx = 10)

        # Dashboard button on left sidebar
        settings_icon = ImageTk.PhotoImage(Image.open(PATH + "/icons/dashboard.png").resize((IMG_SIZE, IMG_SIZE)).convert("RGBA"))
        self.settings_button = ct.CTkButton(master = self.left_sidebar,
                                            text = "Dashboard",
                                            text_font = ("Verdana", -12),
                                            image = settings_icon,
                                            command = None)
        self.settings_button.grid(row = 3, column = 0, padx = 10, pady = 10)

        # Settings button on left sidebar
        settings_icon = ImageTk.PhotoImage(Image.open(PATH + "/icons/settings.png").resize((IMG_SIZE, IMG_SIZE)).convert("RGBA"))
        self.settings_button = ct.CTkButton(master = self.left_sidebar,
                                            text = "Settings",
                                            text_font = ("Verdana", -12),
                                            image = settings_icon,
                                            command = None)
        self.settings_button.grid(row = 9, column = 0, padx = 10, pady = 10)

        # Close button on left sidebar
        close_icon = ImageTk.PhotoImage(Image.open(PATH + "/icons/close.png").resize((IMG_SIZE, IMG_SIZE)).convert("RGBA"))
        self.close_button = ct.CTkButton(master = self.left_sidebar,
                                         text = "Exit Game",
                                         text_font = ("Verdana", -12),
                                         image = close_icon,
                                         command = self.stop)
        self.close_button.grid(row = 10, column = 0, padx = 10, pady = 10)

        # Right frame
        self.right_frame = ct.CTkFrame(master = self)
        self.right_frame.grid(row = 0, column = 1, sticky = "nswe", padx = 10, pady = 10)

        # Settings menu container
        self.settings_menu = ct.CTkFrame(master = self.right_frame,
                                         bg_color = self['bg'])
        self.settings_menu.grid(row = 0, column = 0, sticky = "nswe")

    def change_theme(self):
        ct.set_default_color_theme("blue")

    def change_mode(self):
        if 0 == 1: ## change 0 to be the switch object .get()
            ct.set_appearance_mode("dark")
        else:
            ct.set_appearance_mode("light")

    def start(self):
        self.mainloop()

    def stop(self, event = 0):
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.start()
