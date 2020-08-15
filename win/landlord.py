import win.widget as Widget
from wincon.landlord import WinConLandlord as WinCon
from lib.landlord import Landlord

import win.contact
import win.property
from tkinter import Button

class LandlordWin:
    def see_window_left(window, user, number):
        row = 0

        insert = user.landlord_list[number].title
        entry_title = Widget.entry(window, user, 'Title', row, 2, insert)
        WinCon.update_button(window, user, 'landlord', number, 'title', entry_title, row, 2, insert)
        row += 2

        insert = user.landlord_list[number].first_names
        entry_first_names = Widget.entry(window, user, 'First name(s)', row, 2, insert)
        WinCon.update_button(window, user, 'landlord', number, 'first_names', entry_first_names, row, 2, insert)
        row += 2

        insert = user.landlord_list[number].surname
        entry_surname = Widget.entry(window, user, 'Surname', row, 2, insert)
        WinCon.update_button(window, user, 'landlord', number, 'surname', entry_surname, row, 2, insert)
        row += 2

        insert = user.landlord_list[number].note
        entry_note = Widget.entry(window, user, 'Note:', row, 2, insert)
        WinCon.update_button(window, user, 'landlord', number, 'note', entry_note, row, 2, insert)
        row += 2

        return row

    def see_window_right(window, user, number):
        row = 0
        column = 5
        Widget.line(window, user, '', row, column)
        column += 1

        break_line = '------------------------------------------------------------------------------------------------------'

        line = 'Landlord code: ' + user.landlord_list[number].code
        Widget.line(window, user, line, row, column)
        row += 1
        Widget.line(window, user, break_line, row, column)
        row += 1

        line = 'Name: ' + user.landlord_list[number].title + ' ' + user.landlord_list[number].first_names + ' ' + user.landlord_list[number].surname
        Widget.title(window, user, line, row, column)
        row += 1

        line = 'Properties: '
        Widget.line(window, user, line, row, column)
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
        Widget.line(window, user, line, row, column)
        row += 1
        text = user.landlord_list[number].note
        Widget.content(window, user, text, row, column)
        row += 1

        line = 'Contact details: '
        Widget.line(window, user, line, row, column)
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
        Widget.add_window_button(window, user, 'contact', number, row, column)
        column += 1
        Widget.close_button(window, 'see', window, user, 'property', row, column)

    def see_window(user, number):
        # Set up window
        window =  Widget.window(user.root, user, 'See Landlord', 'medium')

        # Left side entries/update
        row = LandlordWin.see_window_left(window, user, number)

        # Right Side
        LandlordWin.see_window_right(window, user, number)

        # Add window and number to user so see_window_right can be called from outside of method
        user.landlord_see_windows.insert(0, [window, number])
        # Close window sent through method so can be removed from user
        window.protocol("WM_DELETE_WINDOW", lambda: Widget.close_window(window, 'see', user, 'landlord'))

    def confirm_window(add_window, user, entries):
        # Set up window
        window =  Widget.window(add_window, user, 'Confirm Landlord', 'small')
        row = 0

        # open entries array
        title = entries[0].get()
        first_names = entries[1].get()
        surname = entries[2].get()
        note = entries[3].get()

        text = 'Check and confirm landlord:'
        Widget.title(window, user, text)
        row += 1

        text = title + ' ' + first_names + ' ' + surname + ' - ' + note
        Widget.content(window, user, text)
        row += 1

        text = 'CONFIRM (as ' + user.name + ')'
        data = {'title': title, 'first_names': first_names, 'surname': surname, 'note': note}
        Widget.add_button(add_window, window, user, 'landlord', text, data, row)
        text = "Cancel (don't confirm)"
        Widget.close_button(window, False, window, user, False, row, 1, text)

    def add_window(user, number=False):
        # Set up window
        window =  Widget.window(user.root, user, 'Add Landlord', 'small')
        row = 0

        text = 'Add landlord as ' + user.name
        Widget.title(window, user, text)
        row += 1

        entry_title = Widget.entry(window, user, 'Title:', row)
        row += 1
        entry_first_names = Widget.entry(window, user, 'First name(s):', row)
        row += 1
        entry_surname = Widget.entry(window, user, 'Surname:', row)
        row += 1
        entry_note = Widget.entry(window, user, 'Note:', row)
        row += 1

        text = 'SUBMIT (as ' + user.name + ')'

        entries = [entry_title, entry_first_names, entry_surname, entry_note]
        Widget.confirm_window_button(window, user, 'landlord', text, entries, row)
        Widget.close_button(window, False, window, user, False, row, 2)

    def print_temp():
        print('closed')

    def show_window(user):
        # Set up window
        window =  Widget.window(user.root, user, 'Show Landlords', 'medium')

        # Set up frames
        top_frame = Widget.side_frame(window, user, 'top')
        scroll_frame = Widget.scroll_frame(window, user)
        bottom_frame = Widget.side_frame(window, user, 'bottom')

        # Top Frame
        text = 'Landlords for ' + user.name + ':'
        Widget.title(top_frame, user, text)

        # Scroll Frame
        Widget.scroll_button_list(window, scroll_frame, user, 'landlord')

        # Bottom Frame
        Widget.add_window_button(bottom_frame, user, 'landlord')
        Widget.close_button(window, 'show', bottom_frame, user, 'landlord')

        # Add window and scroll frame to user so can be refreshed from outside of method
        user.landlord_show_windows.insert(0, [window, scroll_frame, False])
        # Close window sent through method so can be removed from user
        window.protocol("WM_DELETE_WINDOW", lambda: Widget.close_window(window, 'show', user, 'landlord'))
