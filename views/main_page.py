# ~~~~~~~~~~~~~~~~~~~~~~ import modules ~~~~~~~~~~~~~~~~~~~~~~

from tkinter import Menu

# ~~~~~~~~~~~~~~~~~~~~~~ class ~~~~~~~~~~~~~~~~~~~~~~

class MainPage:
    # view items used on main window

    def donothing():
        print('do nothing')

    def standard_menubar(window):
        menubar = Menu(window)
        window.config(menu=menubar)
        # file menu
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=MainPage.donothing)
        filemenu.add_command(label="Open", command=MainPage.donothing)
        filemenu.add_command(label="Save", command=MainPage.donothing)
        filemenu.add_command(label="Save as...", command=MainPage.donothing)
        filemenu.add_command(label="Close", command=MainPage.donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=window.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        # edit menu
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=MainPage.donothing)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=MainPage.donothing)
        editmenu.add_command(label="Copy", command=MainPage.donothing)
        editmenu.add_command(label="Paste", command=MainPage.donothing)
        editmenu.add_command(label="Delete", command=MainPage.donothing)
        editmenu.add_command(label="Select All", command=MainPage.donothing)
        menubar.add_cascade(label="Edit", menu=editmenu)
        # help menu
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=MainPage.donothing)
        helpmenu.add_command(label="About...", command=MainPage.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)
