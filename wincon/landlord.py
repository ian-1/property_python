from tkinter import Button
import win.landlord
import win.property
import win.contact
from lib.landlord import Landlord

class WinConLandlord():

    def add(add_window, user, title, first_names, surname, note):
        user.add_landlord(user, title, first_names, surname, note)
        add_window.destroy()
        user.save_all_class_type('landlord')
        WinConLandlord.refresh(user)

    def update(user, number, type, new):
        user.landlord_list[number].update(type, new)
        user.save_all_class_type('landlord')
        WinConLandlord.refresh(user)

    # Window refresh management

    def refresh(user):
        import win.widget as Widget
        for win_frame in user.landlord_win.see_windows:
            win.landlord.LandlordWin.see_window_right(win_frame[0], user, win_frame[1])
        for win_frame in user.landlord_win.show_windows:
            Widget.scroll_button_list(win_frame[0], win_frame[1], user, 'landlord')
        # properties
        for win_frame in user.property_win.see_windows:
            win.property.PropertyWin.see_window_right(win_frame[0], user, win_frame[1])

    # Action Buttons

    def add_button(add_window, confirm_window, user, text, title, first_names, surname, note, row):
        button = Button(confirm_window, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: WinConLandlord.add(add_window, user, title, first_names, surname, note))
        button.grid(row=row, column=0, sticky='nsew', padx=user.padx, pady=user.pady)

    def update_button(frame, user, number, type, entry, row, rowspan, insert):
        bg = 'white'
        if entry.get() != insert:
            bg = 'red'
        button = Button(frame, text='update', font=user.standard_font, bg=bg,
                             command=lambda: WinConLandlord.update(user, number, type, entry.get()))
        button.grid(row=row, column=3, rowspan=rowspan, padx=user.padx, pady=user.pady)
