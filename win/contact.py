from wincon.general import WinConGeneral
from wincon.contact import WinConContact as WinCon
from lib.contact import Contact

class ContactWin:
    def __init__(self):
        self.see_windows = []
        self.show_windows = []

    def see_window_left(window, user, number):
        row = 0

        insert = user.contacts[number].type
        entry_type = WinConGeneral.drop_down(window, user, 'Type', ['Address', 'Phone Number', 'Email'], row, 2, insert)
        WinCon.update_button(window, user, number, 'type', entry_type, row, 2, insert)
        row += 2

        insert = user.contacts[number].address
        text = 'Address'
        if user.contacts[number].type == 'phone': text = 'Number'
        entry_address = WinConGeneral.entry(window, user, text, row, 2, insert)
        WinCon.update_button(window, user, number, 'address', entry_address, row, 2, insert)
        row += 2

        insert = user.contacts[number].note
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

        text = 'Address: '
        if user.contacts[number].type == 'Email': text = 'Email: '
        if user.contacts[number].type == 'Phone Number': text = 'Number: '
        line1 = text + user.contacts[number].address
        WinConGeneral.title(window, user, line1, row, column)
        row += 1
        WinConGeneral.line(window, user, break_line, row, column)
        row += 1

        text = user.contacts[number].note
        WinConGeneral.content(window, user, text, row, column)

    def see_window(user, number):
        # Set up window
        window =  WinConGeneral.window(user.root, user, 'See Contact', 'medium')

        # Left side entries/update
        row = ContactWin.see_window_left(window, user, number)

        # Left Side Buttons
        WinCon.close_see_window_button(window, window, user, row, 2)

        # Right Side
        ContactWin.see_window_right(window, user, number)

        # Add window and number to user so see_window_right can be called from outside of method
        user.contact_win.see_windows.insert(0, [window, number])
        # Close window sent through method so can be removed from user
        window.protocol("WM_DELETE_WINDOW", lambda: WinCon.close_see_window(window, user))

    def confirm_window(add_window, user, type, address, note, number):
        # Set up window
        window =  WinConGeneral.window(add_window, user, 'Confirm Contact', 'small')
        row = 0

        text = 'Check and confirm contact:'
        WinConGeneral.title(window, user, text)
        row += 1

        text = type + ' - ' + address
        WinConGeneral.content(window, user, text, row)
        row += 1

        text = note
        WinConGeneral.content(window, user, text, row)
        row += 1

        text = 'CONFIRM (as ' + user.name + ')'
        WinCon.add_button(add_window, window, user, text, type, address, note, number, row)
        text = "Cancel (don't confirm)"
        WinConGeneral.close_button(window, window, user, row, 1, text)

    def add_window(user, number):
        # Set up window
        window =  WinConGeneral.window(user.root, user, 'Add Contact', 'small')
        row = 0

        text = 'Add contact as ' + user.name
        WinConGeneral.title(window, user, text)
        row += 1

        entry_type = WinConGeneral.drop_down(window, user, 'Type:', ['Address', 'Phone Number', 'Email'], row)
        row += 1
        entry_address = WinConGeneral.entry(window, user, 'Enter:', row)
        row += 1
        entry_note = WinConGeneral.entry(window, user, 'Note (optional):', row)
        row += 1

        text = 'SUBMIT (as ' + user.name + ')'
        WinCon.confirm_window_button(window, user, text, entry_type, entry_address, entry_note, number, row)
        WinConGeneral.close_button(window, window, user, row, 2)

    def print_temp():
        print('closed')

    def show_window(user):
        # Set up window
        window =  WinConGeneral.window(user.root, user, 'Show Contacts', 'medium')

        # Set up frames
        top_frame = WinConGeneral.side_frame(window, user, 'top')
        scroll_frame = WinConGeneral.scroll_frame(window, user)
        bottom_frame = WinConGeneral.side_frame(window, user, 'bottom')

        # Top Frame
        text = 'Contacts for ' + user.name + ':'
        WinConGeneral.title(top_frame, user, text)

        # Scroll Frame
        WinCon.scroll_button_list(window, scroll_frame, user)

        # Bottom Frame
        WinCon.add_window_button(bottom_frame, user)
        WinCon.close_show_window_button(window, bottom_frame, user)

        # Add window and scroll frame to user so can be refreshed from outside of method
        user.contact_win.show_windows.insert(0, [window, scroll_frame])
        # Close window sent through method so can be removed from user
        window.protocol("WM_DELETE_WINDOW", lambda: WinCon.close_show_window(window, user))
