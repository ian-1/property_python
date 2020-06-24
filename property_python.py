# ~~~~~~~~~~~~~~~~~~~~~~ import modules ~~~~~~~~~~~~~~~~~~~~~~

from tkinter import Tk
from views.main_page import MainPage

# ~~~~~~~~~~~~~~~~~~~~~~ globsl variables ~~~~~~~~~~~~~~~~~~~~~~

monospaced_font = 'Consolas'
font = 'Helvetica'

# ~~~~~~~~~~~~~~~~~~~~~~ main programme ~~~~~~~~~~~~~~~~~~~~~~

# creating tkinter window
root = Tk()

# setting the minimun size of the root window
root.minsize(950, 150)

# adding menu bar to the roof window
MainPage.standard_menubar(root)

root.mainloop()
