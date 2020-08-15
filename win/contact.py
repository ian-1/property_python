import win.widget as Widget
from lib.contact import Contact

class ContactWin:
    def see_window_left(window, user, number):
        row = 0

        insert = user.contact_list[number].type
        entry_type = Widget.drop_down(window, user, 'Type', ['Address', 'Phone Number', 'Email'], row, 2, insert)
        Widget.update_button(window, user, 'contact', number, 'type', entry_type, row, 2)
        row += 2

        insert = user.contact_list[number].address
        text = 'Address'
        if user.contact_list[number].type == 'phone': text = 'Number'
        entry_address = Widget.entry(window, user, text, row, 2, insert)
        Widget.update_button(window, user, 'contact', number, 'address', entry_address, row, 2)
        row += 2

        insert = user.contact_list[number].note
        entry_note = Widget.entry(window, user, 'Note:', row, 2, insert)
        Widget.update_button(window, user, 'contact', number, 'note', entry_note, row, 2)
        row += 2

        return row

    def see_window_right(window, user, number):
        row = 0
        column = 5
        Widget.line(window, user, '', row, column)
        column += 1

        break_line = '------------------------------------------------------------------------------------------------------'

        text = 'Address: '
        if user.contact_list[number].type == 'Email': text = 'Email: '
        if user.contact_list[number].type == 'Phone Number': text = 'Number: '
        line1 = text + user.contact_list[number].address
        Widget.title(window, user, line1, row, column)
        row += 1
        Widget.line(window, user, break_line, row, column)
        row += 1

        text = user.contact_list[number].note
        Widget.content(window, user, text, row, column)

    def see_window(user, number):
        # Set up window
        window =  Widget.window(user.root, user, 'See Contact', 'medium')

        # Left side entries/update
        row = ContactWin.see_window_left(window, user, number)

        # Left Side Buttons
        Widget.close_button(window, 'see', window, user, 'contact', row, 2)

        # Right Side
        ContactWin.see_window_right(window, user, number)

        # Add window and number to user so see_window_right can be called from outside of method
        user.contact_see_windows.insert(0, [window, number])
        # Close window sent through method so can be removed from user
        window.protocol("WM_DELETE_WINDOW", lambda: Widget.close_window(window, 'see', user, 'contact'))

    def confirm_window(add_window, user, entries):
        # Set up window
        window =  Widget.window(add_window, user, 'Confirm Contact', 'small')
        row = 0

        # open entries array
        type = entries.get('type', '').get()
        address = entries.get('enter', '').get()
        note = entries.get('note', '').get()
        number = entries.get('number', '')

        text = 'Check and confirm contact:'
        Widget.title(window, user, text)
        row += 1

        text = type + ' - ' + address
        Widget.content(window, user, text, row)
        row += 1

        text = note
        Widget.content(window, user, text, row)
        row += 1

        text = 'CONFIRM (as ' + user.name + ')'
        data = {'type': type, 'address': address, 'note': note, 'number': number}
        Widget.add_button(add_window, window, user, 'contact', text, data, row)
        text = "Cancel (don't confirm)"
        Widget.close_button(window, False, window, user, False, row, 1, text)
