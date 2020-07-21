from wincon.general import WinConGeneral
from wincon.landlord import WinConLandlord as WinCon
from lib.landlord import Landlord

import win.contact
import win.property
from tkinter import Button

class LandlordWin:
    def __init__(self):
        self.see_windows = []
        self.show_windows = []

    def see_window_left(window, user, number):
        row = 0

        insert = user.landlord_list[number].title
        entry_title = WinConGeneral.entry(window, user, 'Title', row, 2, insert)
        WinCon.update_button(window, user, number, 'title', entry_title, row, 2, insert)
        row += 2

        insert = user.landlord_list[number].first_names
        entry_first_names = WinConGeneral.entry(window, user, 'First name(s)', row, 2, insert)
        WinCon.update_button(window, user, number, 'first_names', entry_first_names, row, 2, insert)
        row += 2

        insert = user.landlord_list[number].surname
        entry_surname = WinConGeneral.entry(window, user, 'Surname', row, 2, insert)
        WinCon.update_button(window, user, number, 'surname', entry_surname, row, 2, insert)
        row += 2

        insert = user.landlord_list[number].note
        entry_note = WinConGeneral.entry(window, user, 'Note:', row, 2, insert)
        WinCon.update_button(window, user, number, 'note', entry_note, row, 2, insert)
        row += 2

        return row

    def see_window_right(window, user, number):
        row = 0
        column = 5
        WinConGeneral.line(window, user, '', row, column)
        column += 1

        break_line = '------------------------------------------------------------------------------------------------------'

        line = 'Landlord code: ' + user.landlord_list[number].code
        WinConGeneral.line(window, user, line, row, column)
        row += 1
        WinConGeneral.line(window, user, break_line, row, column)
        row += 1

        line = 'Name: ' + user.landlord_list[number].title + ' ' + user.landlord_list[number].first_names + ' ' + user.landlord_list[number].surname
        WinConGeneral.title(window, user, line, row, column)
        row += 1

        line = 'Properties: '
        WinConGeneral.line(window, user, line, row, column)
        row += 1
        counter = 0
        for property in user.property_list:
            for code in property.landlords:
                if code == user.landlord_list[number].code:
                    text =  property.address
                    pp_number = 0
                    for pp in user.property_list:
                        if property == pp: break
                        pp_number += 1
                    button = Button(window, relief='flat', bg="gray99",
                                    font=user.standard_font, text=text, anchor='w',
                                    command=lambda pp_number=pp_number: win.property.PropertyWin.see_window(user, pp_number))
                    button.grid(row=row, column=column,  columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)
                    row += 1
                counter += 1

        line = 'Notes: '
        WinConGeneral.line(window, user, line, row, column)
        row += 1
        text = user.landlord_list[number].note
        WinConGeneral.content(window, user, text, row, column)
        row += 1

        line = 'Contact details: '
        WinConGeneral.line(window, user, line, row, column)
        row += 1
        for code in user.landlord_list[number].contacts:
            counter = 0
            for contact in user.contact_list:
                if code == contact.code:
                    note = ' (' + contact.note + ')'
                    if len(contact.note) > 38:
                        note = ' (' + contact.note[0:35] + '...)'
                    text =  contact.type + ' - ' + contact.address + note
                    button = Button(window, relief='flat', bg="gray99",
                                    font=user.standard_font, text=text, anchor='w',
                                    command=lambda number=counter: win.contact.ContactWin.see_window(user, number))
                    button.grid(row=row, column=column,  columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)
                    row += 1
                counter += 1

        # Buttons
        WinCon.add_contact_window_button(window, user, number, row, column)
        column += 1
        WinCon.close_see_window_button(window, window, user, row, column)



    def see_window(user, number):
        # Set up window
        window =  WinConGeneral.window(user.root, user, 'See Landlord', 'medium')

        # Left side entries/update
        row = LandlordWin.see_window_left(window, user, number)

        # Right Side
        LandlordWin.see_window_right(window, user, number)

        # Add window and number to user so see_window_right can be called from outside of method
        user.landlord_win.see_windows.insert(0, [window, number])
        # Close window sent through method so can be removed from user
        window.protocol("WM_DELETE_WINDOW", lambda: WinCon.close_see_window(window, user))

    def confirm_window(add_window, user, title, first_names, surname, note):
        # Set up window
        window =  WinConGeneral.window(add_window, user, 'Confirm Landlord', 'small')
        row = 0

        text = 'Check and confirm landlord:'
        WinConGeneral.title(window, user, text)
        row += 1

        text = title + ' ' + first_names + ' ' + surname + ' - ' + note
        WinConGeneral.content(window, user, text)
        row += 1

        text = 'CONFIRM (as ' + user.name + ')'
        WinCon.add_button(add_window, window, user, text, title, first_names, surname, note, row)
        text = "Cancel (don't confirm)"
        WinConGeneral.close_button(window, window, user, row, 1, text)

    def add_window(user):
        # Set up window
        window =  WinConGeneral.window(user.root, user, 'Add Landlord', 'small')
        row = 0

        text = 'Add landlord as ' + user.name
        WinConGeneral.title(window, user, text)
        row += 1

        entry_title = WinConGeneral.entry(window, user, 'Title:', row)
        row += 1
        entry_first_names = WinConGeneral.entry(window, user, 'First name(s):', row)
        row += 1
        entry_surname = WinConGeneral.entry(window, user, 'Surname:', row)
        row += 1
        entry_note = WinConGeneral.entry(window, user, 'Note:', row)
        row += 1

        text = 'SUBMIT (as ' + user.name + ')'
        WinCon.confirm_window_button(window, user, text, entry_title, entry_first_names, entry_surname, entry_note, row)
        WinConGeneral.close_button(window, window, user, row, 2)

    def print_temp():
        print('closed')

    def show_window(user):
        # Set up window
        window =  WinConGeneral.window(user.root, user, 'Show Landlords', 'medium')

        # Set up frames
        top_frame = WinConGeneral.side_frame(window, user, 'top')
        scroll_frame = WinConGeneral.scroll_frame(window, user)
        bottom_frame = WinConGeneral.side_frame(window, user, 'bottom')

        # Top Frame
        text = 'Landlords for ' + user.name + ':'
        WinConGeneral.title(top_frame, user, text)

        # Scroll Frame
        WinCon.scroll_button_list(window, scroll_frame, user)

        # Bottom Frame
        WinConGeneral.add_window_button(bottom_frame, user, 'landlord')
        WinCon.close_show_window_button(window, bottom_frame, user)

        # Add window and scroll frame to user so can be refreshed from outside of method
        user.landlord_win.show_windows.insert(0, [window, scroll_frame])
        # Close window sent through method so can be removed from user
        window.protocol("WM_DELETE_WINDOW", lambda: WinCon.close_show_window(window, user))
