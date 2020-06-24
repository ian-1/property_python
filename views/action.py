
from tkinter import Toplevel,\
                    Button

class Action:
    # view items used in add action window

    def add_window(window, user):
        filewin = Toplevel(window)
        button = Button(filewin, text='add_action', command=lambda: user.add_action('5 skdhfjksd', 'yweiou ufhuihf sdjk'))
        button.pack()
