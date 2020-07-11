from tkinter import Button
import win.property
import win.action
from lib.property import Property

class WinConProperty():

    def add(add_window, user, code, address):
        user.add_property(code, address)
        add_window.destroy()
        Property.save(user)
        WinConProperty.refresh(user)
        number = Property.number_from_code(user, code)
        win.property.PropertyWin.see_window(user, number)

    def update(user, number, type, new):
        user.properties[number].update(type, new)
        Property.save(user)
        WinConProperty.refresh(user)

    def add_landlord(user, number, landlord_code):
        user.properties[number].add_landlord(user, landlord_code)
        Property.save(user)
        WinConProperty.refresh(user)

    # Window refresh management

    def refresh(user):
        for win_frame in user.property_win.see_windows:
            win.property.PropertyWin.see_window_right(win_frame[0], user, win_frame[1])
        for win_frame in user.property_win.show_windows:
            WinConProperty.scroll_button_list(win_frame[0], win_frame[1], user)
        # Actions
        for win_frame in user.action_win.see_windows:
            win.action.ActionWin.see_window_right(win_frame[0], user, win_frame[1])

    def close_see_window(window, user):
        for win_frame in user.property_win.see_windows[:]:
            if win_frame[0] == window:
                user.property_win.see_windows.remove(win_frame)
        window.destroy()

    def close_show_window(window, user):
        for win_frame in user.property_win.show_windows[:]:
            if win_frame[0] == window:
                user.property_win.show_windows.remove(win_frame)
        window.destroy()

    # Action Buttons

    def add_button(add_window, confirm_window, user, text, code, address, row):
        button = Button(confirm_window, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: WinConProperty.add(add_window, user, code, address))
        button.grid(row=row, column=0, sticky='nsew', padx=user.padx, pady=user.pady)

    def update_button(frame, user, number, type, entry, row, rowspan=1):
        button_date = Button(frame, text='update', font=user.standard_font,
                             command=lambda: WinConProperty.update(user, number, type, entry.get()))
        button_date.grid(row=row, column=3, rowspan=rowspan, padx=user.padx, pady=user.pady)

    def add_landlord_button(frame, user, number, entry, row, rowspan=1):
        button_date = Button(frame, text='add', font=user.standard_font,
                             command=lambda: WinConProperty.add_landlord(user, number, entry.get()))
        button_date.grid(row=row, column=3, rowspan=rowspan, padx=user.padx, pady=user.pady)

    # Window Buttons

    # See Window

    def scroll_button_list(window, frame, user):
        width = int(user.medium_window_width/7)
        counter = 0
        for property in user.properties:
            text = property.code + ' - ' + property.address
            button = Button(frame.interior, relief='flat', bg="gray99",
                font=user.standard_font, text=text, width=width, anchor='w',
                command=lambda number=counter: win.property.PropertyWin.see_window(user, number))
            button.grid(row=counter, column = 0, sticky='nsew', padx=user.padx, pady=user.pady)
            counter += 1

    def see_window_button(window, user, code, row=0, rowspan=1):
        property_number = Property.number_from_code(user, code)
        if property_number != False:
            property_button = Button(window, text='Open Property', font=user.large_font, bg=user.button_bg_colour,
                                     command=lambda: win.property.PropertyWin.see_window(user, property_number))
            property_button.grid(row=row, column=0, rowspan=rowspan, padx=user.padx, pady=user.pady)

    def close_see_window_button(window, frame, user, row=0, column=1, text='Close Window'):
        button = Button(frame, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: WinConProperty.close_see_window(window, user))
        button.grid(row=row, column=column, sticky='nsew', padx=user.padx, pady=user.pady)

    # Show Window

    def close_show_window_button(window, frame, user, row=0, column=1, text='Close Window'):
        button = Button(frame, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: WinConProperty.close_show_window(window, user))
        button.grid(row=row, column=column, sticky='nsew', padx=user.padx, pady=user.pady)

    # Add & Confirm windows

    def add_window_button(frame, user):
        add_button = Button(frame, text='Add Property', font=user.large_font, bg=user.button_bg_colour,
                            command=lambda: win.property.PropertyWin.add_window(user))
        add_button.grid(row=0, column=0, sticky='nsew', padx=user.padx, pady=user.pady)

    def confirm_window_button(window, user, text, entry_code, entry_address, row):
        button = Button(window, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: win.property.PropertyWin.confirm_window(window, user, entry_code.get(), entry_address.get()))
        button.bind('<Return>', lambda e: win.property.PropertyWin.confirm_window(window, user, entry_code.get(), entry_address.get()))
        button.grid(row=row, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)
