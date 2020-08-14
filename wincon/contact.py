from tkinter import Button
import win.contact
import win.landlord
from lib.contact import Contact
import win.widget as Widget

class WinConContact():

    def add(add_window, user, type, address, note, number):
        user.add_contact(user, type, address, note, number)
        add_window.destroy()
        user.save_all_class_type('contact')
        Widget.refresh(user)

    def update(user, number, type, new):
        user.contact_list[number].update(type, new)
        user.save_all_class_type('contact')
        Widget.refresh(user)

    # Action Buttons

    def add_button(add_window, confirm_window, user, text, type, address, note, number, row):
        button = Button(confirm_window, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: WinConContact.add(add_window, user, type, address, note, number))
        button.grid(row=row, column=0, sticky='nsew', padx=user.padx, pady=user.pady)

    def update_button(frame, user, number, type, entry, row, rowspan, insert):
        bg = 'white'
        if entry.get() != insert:
            bg = 'red'
        button = Button(frame, text='update', font=user.standard_font, bg=bg,
                             command=lambda: WinConContact.update(user, number, type, entry.get()))
        button.grid(row=row, column=3, rowspan=rowspan, padx=user.padx, pady=user.pady)
