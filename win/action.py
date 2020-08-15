import win.widget as Widget
from wincon.action import WinConAction as WinCon
from wincon.property import WinConProperty
from lib.action import Action
from lib.property import Property

class ActionWin:
    def see_window_left(window, user, number):
        row = 0

        insert = user.action_list[number].date
        entry_date = Widget.entry(window, user, 'Date:', row, 2, insert)
        WinCon.update_button(window, user, 'action', number, 'date', entry_date, row, 2, insert)
        row += 2

        insert = user.action_list[number].property
        entry_property = Widget.entry(window, user, 'Property:', row, 2, insert)
        WinCon.update_button(window, user, 'action', number, 'property', entry_property, row, 2, insert)
        row += 2

        insert = user.action_list[number].message
        entry_message = Widget.entry(window, user, 'Message:', row, 2, insert)
        WinCon.update_button(window, user, 'action', number, 'message', entry_message, row, 2, insert)
        row += 2

        return row

    def see_window_right(window, user, number):
        row = 0
        column = 5
        Widget.line(window, user, '', row, column)
        column += 1

        break_line = '------------------------------------------------------------------------------------------------------'

        line1 = 'Date: ' + user.action_list[number].date + '                         ¦     Code: ' + user.action_list[number].property
        Widget.title(window, user, line1, row, column)
        row += 1
        Widget.line(window, user, break_line, row, column)
        row += 1

        line2 = Property.address_from_code(user, user.action_list[number].property)
        Widget.title(window, user, line2, row, column)
        row += 1
        Widget.line(window, user, break_line, row, column)
        row += 1

        text = user.action_list[number].message
        Widget.content(window, user, text, row, column)

    def see_window(user, number):
        # Set up window
        window =  Widget.window(user.root, user, 'See Action', 'medium')

        # Left side entries/update
        row = ActionWin.see_window_left(window, user, number)

        # Left Side Buttons
        code = user.action_list[number].property
        Widget.see_window_button(window, user, 'property', code, row, 2)
        Widget.close_button(window, 'see', window, user, 'action', row, 2)

        # Right Side
        ActionWin.see_window_right(window, user, number)

        # Add window and number to user so see_window_right can be called from outside of method
        user.action_see_windows.insert(0, [window, number])
        # Close window sent through method so can be removed from user
        window.protocol("WM_DELETE_WINDOW", lambda: Widget.close_window(window, 'see', user, 'action'))

    def confirm_window(add_window, user, entries):
        # Set up window
        window =  Widget.window(add_window, user, 'Confirm Action', 'small')
        row = 0

        # open entries array
        property_code_address = entries[0].get()
        property_code = property_code_address[0:6]
        message = entries[1].get()

        text = 'Check and confirm action:'
        Widget.line(window, user, text)
        row += 1

        address = Property.address_from_code(user, property_code)
        text = 'Address: ' + address
        Widget.title(window, user, text, row)
        row += 1

        text = message
        Widget.content(window, user, text, row)
        row += 1

        text = 'CONFIRM (as ' + user.name + ')'
        data = {'property': property_code, 'message': message}
        Widget.add_button(add_window, window, user, 'action', text, data, row)
        text = "Cancel (don't confirm)"
        Widget.close_button(window, False, window, user, False, row, 1, text)

    def add_window(user, number=False):
        # Set up window
        window =  Widget.window(user.root, user, 'Add Action', 'small')
        row = 0

        text = 'Add action as ' + user.name
        Widget.title(window, user, text)
        row += 1

        options = []
        for property in user.property_list:
            text = property.code + ' - ' + property.address
            options.append(text)
        entry_property = Widget.drop_down(window, user, 'Property:', options, row)
        row += 1
        entry_message = Widget.entry(window, user, 'Message:', row)
        row += 1

        text = 'SUBMIT (as ' + user.name + ')'
        entries = [entry_property, entry_message]
        Widget.confirm_window_button(window, user, 'action', text, entries, row)
        Widget.close_button(window, False, window, user, False, row, 2)


    def print_temp():
        print('closed')

    def show_window(user, code=False): # code for where actions for just one property are requested, otherwise False
        # Set up window
        window =  Widget.window(user.root, user, 'Show Actions', 'medium')

        # Set up frames
        top_frame = Widget.side_frame(window, user, 'top')
        scroll_frame = Widget.scroll_frame(window, user)
        bottom_frame = Widget.side_frame(window, user, 'bottom')

        # Top Frame
        text = 'Actions for ' + user.name + ':'
        Widget.title(top_frame, user, text)

        # Scroll Frame
        Widget.scroll_button_list(window, scroll_frame, user, 'action', code)

        # Bottom Frame
        Widget.add_window_button(bottom_frame, user, 'action')
        Widget.close_button(window, 'show', bottom_frame, user, 'action')

        # Add window and scroll frame to user so can be refreshed from outside of method
        user.action_show_windows.insert(0, [window, scroll_frame, code])
        # Close window sent through method so can be removed from user
        window.protocol("WM_DELETE_WINDOW", lambda: Widget.close_window(window, 'show', user, 'action'))
