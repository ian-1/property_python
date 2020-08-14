import win.widget as Widget
from wincon.task import WinConTask as WinCon
from wincon.property import WinConProperty
from lib.task import Task
from lib.property import Property
from datetime import date

class TaskWin:
    def see_window_left(window, user, number):
        row = 0

        insert = user.task_list[number].date
        entry_date = Widget.entry(window, user, 'Start date:', row, 2, insert)
        WinCon.update_button(window, user, number, 'date', entry_date, row, 2, insert)
        row += 2

        insert = user.task_list[number].property
        entry_property = Widget.entry(window, user, 'Property:', row, 2, insert)
        WinCon.update_button(window, user, number, 'property', entry_property, row, 2, insert)
        row += 2

        insert = user.task_list[number].due
        entry_due = Widget.entry(window, user, 'Due date:', row, 2, insert)
        WinCon.update_button(window, user, number, 'due', entry_due, row, 2, insert)
        row += 2

        insert = user.task_list[number].message
        entry_message = Widget.entry(window, user, 'Message:', row, 2, insert)
        WinCon.update_button(window, user, number, 'message', entry_message, row, 2, insert)
        row += 2

        return row

    def see_window_right(window, user, number):
        row = 0
        column = 5
        Widget.line(window, user, '', row, column)
        column += 1

        break_line = '------------------------------------------------------------------------------------------------------'

        length = Task.date_length(user.task_list[number].date, str(date.today()))
        line = 'Days running: ' + str(length)
        Widget.line(window, user, line, row, column)
        row += 1

        till_due = Task.date_length(str(date.today()), user.task_list[number].due)
        alert = False
        if till_due < 1: alert = True
        line = 'Days till due: ' + str(till_due)
        Widget.title(window, user, line, row, column, alert)
        row += 1

        Widget.line(window, user, break_line, row, column)
        row += 1

        line = Property.address_from_code(user, user.task_list[number].property)
        Widget.title(window, user, line, row, column)
        row += 1

        text = user.task_list[number].message
        Widget.content(window, user, text, row, column)

    def see_window(user, number):
        # Set up window
        window =  Widget.window(user.root, user, 'See Task', 'medium')

        # Left side entries/update
        row = TaskWin.see_window_left(window, user, number)

        # Left Side Buttons
        code = user.task_list[number].property
        Widget.see_window_button(window, user, 'property', code, row, 2)
        Widget.close_button(window, 'see', window, user, 'task', row, 2)


        # Right Side
        TaskWin.see_window_right(window, user, number)

        # Add window and number to user so see_window_right can be called from outside of method
        user.task_see_windows.insert(0, [window, number])
        # Close window sent through method so can be removed from user
        window.protocol("WM_DELETE_WINDOW", lambda: Widget.close_window(window, 'see', user, 'task'))

    def confirm_window(add_window, user, entries):
        # Set up window
        window =  Widget.window(add_window, user, 'Confirm Task', 'small')
        row = 0

        # open entries array
        property_code_address = entries[0].get()
        property_code = property_code_address[0:6]
        message = entries[1].get()

        text = 'Check and confirm task:'
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
        WinCon.add_button(add_window, window, user, text, property_code, message, row)
        text = "Cancel (don't confirm)"
        Widget.close_button(window, False, window, user, False, row, 1, text)

    def add_window(user, number=False):
        # Set up window
        window =  Widget.window(user.root, user, 'Add Task', 'small')
        row = 0

        text = 'Add task as ' + user.name
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
        Widget.confirm_window_button(window, user, 'task', text, entries, row)
        Widget.close_button(window, False, window, user, False, row, 2)


    def print_temp():
        print('closed')

    def show_window(user, code=False): # code for where tasks for just one property are requested, otherwise False
        # Set up window
        window =  Widget.window(user.root, user, 'Show Tasks', 'medium')

        # Set up frames
        top_frame = Widget.side_frame(window, user, 'top')
        scroll_frame = Widget.scroll_frame(window, user)
        bottom_frame = Widget.side_frame(window, user, 'bottom')

        # Top Frame
        text = 'Tasks for ' + user.name + ':'
        Widget.title(top_frame, user, text)

        # Scroll Frame
        Widget.scroll_button_list(window, scroll_frame, user, 'task', code)

        # Bottom Frame
        Widget.add_window_button(bottom_frame, user, 'task')
        Widget.close_button(window, 'show', bottom_frame, user, 'task')

        # Add window and scroll frame to user so can be refreshed from outside of method
        user.task_show_windows.insert(0, [window, scroll_frame, code])
        # Close window sent through method so can be removed from user
        window.protocol("WM_DELETE_WINDOW", lambda: Widget.close_window(window, 'show', user, 'task'))
