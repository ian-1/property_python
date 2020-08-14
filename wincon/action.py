from tkinter import Button
import win.action
from lib.action import Action
import win.widget as Widget

class WinConAction():

    def add(add_window, user, property, message):
        user.add_action(user, property, message)
        add_window.destroy()
        user.save_all_class_type('action')
        Widget.refresh(user)

    def update(user, number, type, new):
        user.action_list[number].update(type, new)
        user.save_all_class_type('action')
        Widget.refresh(user)

    # Action Buttons

    def add_button(add_window, confirm_window, user, text, property, message, row):
        button = Button(confirm_window, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: WinConAction.add(add_window, user, property, message))
        button.grid(row=row, column=0, sticky='nsew', padx=user.padx, pady=user.pady)

    def update_button(frame, user, number, type, entry, row, rowspan, insert):
        bg = 'white'
        if entry.get() != insert:
            bg = 'red'
        button = Button(frame, text='update', font=user.standard_font, bg=bg,
                             command=lambda: WinConAction.update(user, number, type, entry.get()))
        button.grid(row=row, column=3, rowspan=rowspan, padx=user.padx, pady=user.pady)
