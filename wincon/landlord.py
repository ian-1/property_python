from tkinter import Button
import win.landlord
from lib.landlord import Landlord

class WinConLandlord():

    def add(add_window, user, property, message):
        user.add_landlord(property, message)
        add_window.destroy()
        Landlord.save_landlords(user)
        WinConLandlord.refresh(user)

    def update(user, number, type, new):
        user.landlords[number].update_landlord(type, new)
        Landlord.save_landlords(user)
        WinConLandlord.refresh(user)

    # Window refresh management

    def refresh(user):
        for win_frame in user.landlord_win.see_windows:
            win.landlord.LandlordWin.see_window_right(win_frame[0], user, win_frame[1])
        for win_frame in user.landlord_win.show_windows:
            WinConLandlord.scroll_button_list(win_frame[0], win_frame[1], user, win_frame[2])

    def close_see_window(window, user):
        for win_frame in user.landlord_win.see_windows[:]:
            if win_frame[0] == window:
                user.landlord_win.see_windows.remove(win_frame)
        window.destroy()

    def close_show_window(window, user):
        for win_frame in user.landlord_win.show_windows[:]:
            if win_frame[0] == window:
                user.landlord_win.show_windows.remove(win_frame)
        window.destroy()

    # Action Buttons

    def add_button(add_window, confirm_window, user, text, property, message, row):
        button = Button(confirm_window, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: WinConLandlord.add(add_window, user, property, message))
        button.grid(row=row, column=0, sticky='nsew', padx=user.padx, pady=user.pady)

    def update_button(frame, user, number, type, entry, row, rowspan, insert):
        bg = 'white'
        if entry.get() != insert:
            bg = 'red'
        button_date = Button(frame, text='update', font=user.standard_font, bg=bg,
                             command=lambda: WinConLandlord.update(user, number, type, entry.get()))
        button_date.grid(row=row, column=3, rowspan=rowspan, padx=user.padx, pady=user.pady)

    # Window Buttons

    # See Window

    def scroll_button_list(window, frame, user, code):
        width = int(user.medium_window_width/7)
        counter = 0
        for landlord in user.landlords:
            text = landlord.date + ' - ' + landlord.property + ' - ' + landlord.message
            # if show all or property code matches
            if code in (False, landlord.property):
                button = Button(frame.interior, relief='flat', bg="gray99",
                    font=user.standard_font, text=text, width=width, anchor='w',
                    command=lambda number=counter: win.landlord.LandlordWin.see_window(user, number))
                button.grid(row=counter, column = 0, sticky='nsew', padx=user.padx, pady=user.pady)
            counter += 1

    def close_see_window_button(window, frame, user, row=0, column=1, text='Close Window'):
        button = Button(frame, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: WinConLandlord.close_see_window(window, user))
        button.grid(row=row, column=column, sticky='nsew', padx=user.padx, pady=user.pady)

    # Show Window

    def show_window_button(window, user, code, row, rowspan=1):
        landlords_button = Button(window, text='View Landlords', font=user.large_font, bg=user.button_bg_colour,
                                command=lambda: win.landlord.LandlordWin.show_window(user, code))
        landlords_button.grid(row=row, column=0, rowspan=rowspan, sticky='nsew', padx=user.padx, pady=user.pady)

    def close_show_window_button(window, frame, user, row=0, column=1, text='Close Window'):
        button = Button(frame, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: WinConLandlord.close_show_window(window, user))
        button.grid(row=row, column=column, sticky='nsew', padx=user.padx, pady=user.pady)

    # Add & Confirm windows

    def add_window_button(frame, user):
        add_button = Button(frame, text='Add Landlord', font=user.large_font, bg=user.button_bg_colour,
                            command=lambda: win.landlord.LandlordWin.add_window(user))
        add_button.grid(row=0, column=0, sticky='nsew', padx=user.padx, pady=user.pady)

    def confirm_window_button(window, user, text, entry_property, entry_message, row):
        button = Button(window, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: win.landlord.LandlordWin.confirm_window(window, user, entry_property.get(), entry_message.get()))
        button.bind('<Return>', lambda e: win.landlord.LandlordWin.confirm_window(window, user, entry_property.get(), entry_message.get()))
        button.grid(row=row, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)