from tkinter import Button
import win.contact
import win.landlord
from lib.contact import Contact

class WinConContact():

    def add(add_window, user, type, address, note, number):
        user.add_contact(user, type, address, note, number)
        add_window.destroy()
        user.save_group('contact')
        WinConContact.refresh(user)

    def update(user, number, type, new):
        user.contact_list[number].update(type, new)
        user.save_group('contact')
        WinConContact.refresh(user)

    # Window refresh management

    def refresh(user):
        for win_frame in user.contact_win.see_windows:
            win.contact.ContactWin.see_window_right(win_frame[0], user, win_frame[1])
        for win_frame in user.contact_win.show_windows:
            WinConContact.scroll_button_list(win_frame[0], win_frame[1], user)
        # landlords
        for win_frame in user.landlord_win.see_windows:
            win.landlord.LandlordWin.see_window_right(win_frame[0], user, win_frame[1])

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

    # Window Buttons

    # Add & Confirm windows

    def confirm_window_button(window, user, text,entry_type, entry_address, entry_note, number, row):
        button = Button(window, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: win.contact.ContactWin.confirm_window(window, user, entry_type.get(), entry_address.get(), entry_note.get(), number))
        button.bind('<Return>', lambda e: win.contact.ContactWin.confirm_window(window, user, entry_type.get(), entry_address.get(), entry_note.get(), number))
        button.grid(row=row, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)
