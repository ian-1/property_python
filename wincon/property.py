from tkinter import Button
import win.property
import win.action

class WinConProperty():

    def add(add_window, user, code, address):
        user.add_property(code, address)
        add_window.destroy()
        user.save_all_class_type('property')
        WinConProperty.refresh(user)
        number = Property.number_from_code(user, code)
        win.property.PropertyWin.see_window(user, number)

    def update(user, number, type, new):
        user.property_list[number].update(type, new)
        user.save_all_class_type('property')
        WinConProperty.refresh(user)

    def add_landlord(user, number, landlord_code):
        user.property_list[number].add_landlord(user, landlord_code)
        user.save_all_class_type('property')
        WinConProperty.refresh(user)

    # Window refresh management

    def refresh(user):
        import win.widget as Widget
        for win_frame in user.property_win.see_windows:
            win.property.PropertyWin.see_window_right(win_frame[0], user, win_frame[1])
        for win_frame in user.property_win.show_windows:
            Widget.scroll_button_list(win_frame[0], win_frame[1], user, 'property')
        # Actions
        for win_frame in user.action_win.see_windows:
            win.action.ActionWin.see_window_right(win_frame[0], user, win_frame[1])
        # Landlords
        for win_frame in user.landlord_win.see_windows:
            win.landlord.LandlordWin.see_window_right(win_frame[0], user, win_frame[1])

    # Action Buttons

    def add_button(add_window, confirm_window, user, text, code, address, row):
        button = Button(confirm_window, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: WinConProperty.add(add_window, user, code, address))
        button.grid(row=row, column=0, sticky='nsew', padx=user.padx, pady=user.pady)

    def update_button(frame, user, number, type, entry, row, rowspan=1):
        button = Button(frame, text='update', font=user.standard_font,
                             command=lambda: WinConProperty.update(user, number, type, entry.get()))
        button.grid(row=row, column=3, rowspan=rowspan, padx=user.padx, pady=user.pady)

    def add_landlord_button(frame, user, number, entry, row, rowspan=1):
        button = Button(frame, text='add', font=user.standard_font,
                             command=lambda: WinConProperty.add_landlord(user, number, entry.get()))
        button.grid(row=row, column=3, rowspan=rowspan, padx=user.padx, pady=user.pady)
