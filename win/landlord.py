import win.widget as Widget
from lib.landlord import Landlord
import win.contact
import win.property
from tkinter import Button

class LandlordWin:
    def see_window_left(window, user, number):
        row = 0

        insert = user.landlord_list[number].title
        entry_title = Widget.entry(window, user, 'Title', row, 2, insert)
        Widget.update_button(window, user, 'landlord', number, 'title', entry_title, row, 2)
        row += 2

        insert = user.landlord_list[number].first_names
        entry_first_names = Widget.entry(window, user, 'First name(s)', row, 2, insert)
        Widget.update_button(window, user, 'landlord', number, 'first_names', entry_first_names, row, 2)
        row += 2

        insert = user.landlord_list[number].surname
        entry_surname = Widget.entry(window, user, 'Surname', row, 2, insert)
        Widget.update_button(window, user, 'landlord', number, 'surname', entry_surname, row, 2)
        row += 2

        insert = user.landlord_list[number].note
        entry_note = Widget.entry(window, user, 'Note:', row, 2, insert)
        Widget.update_button(window, user, 'landlord', number, 'note', entry_note, row, 2)
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
