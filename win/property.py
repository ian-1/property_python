from win.action import ActionWin
import win.widget as Widget
from lib.property import Property

class PropertyWin:
    def see_window_left(window, user, number):
        row = 0

        insert = user.property_list[number].code
        entry_code = Widget.entry(window, user, 'Code:', row, 2, insert)
        Widget.update_button(window, user, 'property', number, 'code', entry_code, row, 2)
        row += 2

        insert = user.property_list[number].address
        entry_address = Widget.entry(window, user, 'Address:', row, 2, insert)
        Widget.update_button(window, user, 'property', number, 'address', entry_address, row, 2)
        row += 2

        entry_landlord = Widget.entry(window, user, 'Landlord:', row, 2)
        Widget.link_landlord_to_property_button(window, user, number, entry_landlord, row, 2)
        row += 2

        return row

    def see_window_right(window, user, number):
        row = 0
        column = 5
        Widget.line(window, user, '', row, column)
        column += 1

        break_line = '------------------------------------------------------------------------------------------------------'

        line1 = 'Code: ' + user.property_list[number].code
        Widget.title(window, user, line1, row, column)
        row += 1
        Widget.line(window, user, break_line, row, column)
        row += 1

        line2 = 'Address: ' + user.property_list[number].address
        Widget.title(window, user, line2, row, column)
        row += 1
        Widget.line(window, user, break_line, row, column)
        row += 1

        number, list = user.property_list[number].landlord_list(user)
        header = str(number) + ' Landlords: '
        if number == 0: header = 'No Landlord'
        if number == 1: header = 'Landlord: '
        line3 = header + list
        Widget.line(window, user, line3, row, column)
        row += 1
        Widget.line(window, user, break_line, row, column)
        row += 1

    def see_window(user, number):
        # Set up window
        window =  Widget.window(user.root, user, 'See Property', 'medium')

        # Left Side entries/update
        row = PropertyWin.see_window_left(window, user, number)

        # Left Side Buttons
        code = user.property_list[number].code
        Widget.show_window_button(window, user, 'action', code, row)
        Widget.show_window_button(window, user, 'task', code, row, 2)
        row += 1
        Widget.close_button(window, 'see', window, user, 'property', row, 2)

        # Right Side
        PropertyWin.see_window_right(window, user, number)

        # Add window and number to user so see_window_right can be called from outside of method
        user.property_see_windows.insert(0, [window, number])
        # Close window sent through method so can be removed from user
        window.protocol("WM_DELETE_WINDOW", lambda: Widget.close_window(window, 'see', user, 'property'))

    def confirm_window(add_window, user, entries):
        # Set up window
        alert = True
        window =  Widget.window(add_window, user, 'Confirm Property', 'small', alert)
        row = 0

        # open entries array
        code = entries[0].get()
        address = entries[1].get()

        text = 'ARE YOU SURE YOU WANT TO ADD PROPERTY?'
        Widget.title(window, user, text, row, 0, alert)
        row += 1

        text = code + ' - ' + address
        Widget.content(window, user, text, row, 0, alert)
        row += 1

        text = 'CONFIRM (as ' + user.name + ')'
        data = {'code': code, 'address': address}
        # Open the new property's see window after adding
        open = True
        Widget.add_button(add_window, window, user, 'property', text, data, row, open)
        text = "Cancel (don't confirm)"
        Widget.close_button(window, False, window, user, False, row, 1, text)

    def add_window(user, number=False):
        # Set up window
        window =  Widget.window(user.root, user, 'Add property', 'small')
        row = 0

        text = 'Add property as ' + user.name
        Widget.title(window, user, text)
        row += 1

        entry_code = Widget.entry(window, user, 'Code:', row)
        row += 1
        entry_address = Widget.entry(window, user, 'Address:', row)
        row += 1

        text = 'SUBMIT (as ' + user.name + ')'
        entries = [entry_code, entry_address]
        Widget.confirm_window_button(window, user, 'property', text, entries, row)
        Widget.close_button(window, False, window, user, False, row, 2)
