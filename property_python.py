# ~~~~~~~~~~~~~~~~~~~~~~ import modules ~~~~~~~~~~~~~~~~~~~~~~

from tkinter import Tk
from views.main_page import MainPage
from lib.user import User

# ~~~~~~~~~~~~~~~~~~~~~~ globsl variables ~~~~~~~~~~~~~~~~~~~~~~

monospaced_font = 'Consolas'
font = 'Helvetica'

# ~~~~~~~~~~~~~~~~~~~~~~ main programme ~~~~~~~~~~~~~~~~~~~~~~

# TEMP SETTING THE User

user = User()

# creating tkinter window
root = Tk()

# setting the minimun size of the root window
root.minsize(950, 150)

# adding menu bar to the roof window
MainPage.standard_menubar(root, user)

root.mainloop()
