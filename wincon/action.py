from tkinter import Button
import win.action
from lib.action import Action
import win.widget as Widget

class WinConAction():

    def update_button(frame, user, class_type, number, type, entry, row, rowspan, insert):
        bg = 'white'
        if entry.get() != insert:
            bg = 'red'
        button = Button(frame, text='update', font=user.standard_font, bg=bg,
                             command=lambda: Widget.update(user, class_type, number, type, entry.get()))
        button.grid(row=row, column=3, rowspan=rowspan, padx=user.padx, pady=user.pady)
