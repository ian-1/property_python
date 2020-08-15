from tkinter import Button
from lib.property import Property
import win.property
import win.action
import win.widget as Widget

class WinConProperty():

    def update(user, number, type, new):
        user.property_list[number].update(type, new)
        user.save_all_class_type('property')
        Widget.refresh(user)

    def add_landlord(user, number, landlord_code):
        user.property_list[number].add_landlord(user, landlord_code)
        user.save_all_class_type('property')
        Widget.refresh(user)

    # Action Buttons

    def add_button(add_window, confirm_window, user, text, data, row):
        button = Button(confirm_window, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: Widget.add(add_window, user, 'property', data, True))
        button.grid(row=row, column=0, sticky='nsew', padx=user.padx, pady=user.pady)

    def update_button(frame, user, number, type, entry, row, rowspan=1):
        button = Button(frame, text='update', font=user.standard_font,
                             command=lambda: WinConProperty.update(user, number, type, entry.get()))
        button.grid(row=row, column=3, rowspan=rowspan, padx=user.padx, pady=user.pady)

    def add_landlord_button(frame, user, number, entry, row, rowspan=1):
        button = Button(frame, text='add', font=user.standard_font,
                             command=lambda: WinConProperty.add_landlord(user, number, entry.get()))
        button.grid(row=row, column=3, rowspan=rowspan, padx=user.padx, pady=user.pady)
