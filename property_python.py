# ~~~~~~~~~~~~~~~~~~~~~~ import modules ~~~~~~~~~~~~~~~~~~~~~~

from tkinter import Tk
from win.main_page import MainPage
from lib.user import User

# ~~~~~~~~~~~~~~~~~~~~~~ globsl variables ~~~~~~~~~~~~~~~~~~~~~~

monospaced_font = 'Consolas'
font = 'Helvetica'

# ~~~~~~~~~~~~~~~~~~~~~~ main programme ~~~~~~~~~~~~~~~~~~~~~~

# TEMP SETTING UP THE User

user = User('User')

# creating tkinter window
root = Tk()
root.title(user.company_name)
root.iconbitmap(user.company_icon)
root.configure(bg=user.window_bg_colour)
root.minsize(user.root_window_width, user.root_window_height)

# add root to windows
user.root = root

# adding menu bar to the root window
MainPage.standard_menubar(user)

root.mainloop()
