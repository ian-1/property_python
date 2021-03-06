import win.widget as Widget
from lib.action import Action
from lib.property import Property

class ActionWin:
    def see_window_left(window, user, number):
        row = 0

        insert = user.action_list[number].date
        entry_date = Widget.entry(window, user, 'Date:', row, 2, insert)
        Widget.update_button(window, user, 'action', number, 'date', entry_date, row, 2)
        row += 2

        insert = user.action_list[number].property
        entry_property = Widget.entry(window, user, 'Property:', row, 2, insert)
        Widget.update_button(window, user, 'action', number, 'property', entry_property, row, 2)
        row += 2

        insert = user.action_list[number].message
        entry_message = Widget.entry(window, user, 'Message:', row, 2, insert)
        Widget.update_button(window, user, 'action', number, 'message', entry_message, row, 2)
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
