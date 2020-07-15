from wincon.general import WinConGeneral
from wincon.task import WinConTask as WinCon
from wincon.property import WinConProperty
from lib.task import Task
from lib.property import Property
from datetime import date

class TaskWin:
    def __init__(self):
        self.see_windows = []
        self.show_windows = []

    def see_window_left(window, user, number):
        row = 0

        insert = user.tasks[number].date
        entry_date = WinConGeneral.entry(window, user, 'Start date:', row, 2, insert)
        WinCon.update_button(window, user, number, 'date', entry_date, row, 2, insert)
        row += 2

        insert = user.tasks[number].property
        entry_property = WinConGeneral.entry(window, user, 'Property:', row, 2, insert)
        WinCon.update_button(window, user, number, 'property', entry_property, row, 2, insert)
        row += 2

        insert = user.tasks[number].due
        entry_due = WinConGeneral.entry(window, user, 'Due date:', row, 2, insert)
        WinCon.update_button(window, user, number, 'due', entry_due, row, 2, insert)
        row += 2

        insert = user.tasks[number].message
        entry_message = WinConGeneral.entry(window, user, 'Message:', row, 2, insert)
        WinCon.update_button(window, user, number, 'message', entry_message, row, 2, insert)
        row += 2

        return row

    def see_window_right(window, user, number):
        row = 0
        column = 5
        WinConGeneral.line(window, user, '', row, column)
        column += 1

        break_line = '------------------------------------------------------------------------------------------------------'

        length = Task.date_length(user.tasks[number].date, str(date.today()))
        line = 'Days running: ' + str(length)
        WinConGeneral.line(window, user, line, row, column)
        row += 1

        till_due = Task.date_length(str(date.today()), user.tasks[number].due)
        alert = False
        if till_due < 1: alert = True
        line = 'Days till due: ' + str(till_due)
        WinConGeneral.title(window, user, line, row, column, alert)
        row += 1

        WinConGeneral.line(window, user, break_line, row, column)
        row += 1

        line = Property.address_from_code(user, user.tasks[number].property)
        WinConGeneral.title(window, user, line, row, column)
        row += 1

        text = user.tasks[number].message
        WinConGeneral.content(window, user, text, row, column)

    def see_window(user, number):
        # Set up window
        window =  WinConGeneral.window(user.root, user, 'See Task', 'medium')

        # Left side entries/update
        row = TaskWin.see_window_left(window, user, number)

        # Left Side Buttons
        code = user.tasks[number].property
        WinConProperty.see_window_button(window, user, code, row, 2)
        WinCon.close_see_window_button(window, window, user, row, 2)

        # Right Side
        TaskWin.see_window_right(window, user, number)

        # Add window and number to user so see_window_right can be called from outside of method
        user.task_win.see_windows.insert(0, [window, number])
        # Close window sent through method so can be removed from user
        window.protocol("WM_DELETE_WINDOW", lambda: WinCon.close_see_window(window, user))

    def confirm_window(add_window, user, property, message):
        # Set up window
        window =  WinConGeneral.window(add_window, user, 'Confirm Task', 'small')
        row = 0

        text = 'Check and confirm task:'
        WinConGeneral.line(window, user, text)
        row += 1

        address = Property.address_from_code(user, property)
        text = 'Address: ' + address
        WinConGeneral.title(window, user, text, row)
        row += 1

        text = message
        WinConGeneral.content(window, user, text, row)
        row += 1

        text = 'CONFIRM (as ' + user.name + ')'
        WinCon.add_button(add_window, window, user, text, property, message, row)
        text = "Cancel (don't confirm)"
        WinConGeneral.close_button(window, window, user, row, 1, text)

    def add_window(user):
        # Set up window
        window =  WinConGeneral.window(user.root, user, 'Add Task', 'small')
        row = 0

        text = 'Add task as ' + user.name
        WinConGeneral.title(window, user, text)
        row += 1

        options = []
        for property in user.properties:
            text = property.code + ' - ' + property.address
            options.append(text)
        entry_property = WinConGeneral.drop_down(window, user, 'Property:', options, row)
        row += 1
        entry_message = WinConGeneral.entry(window, user, 'Message:', row)
        row += 1

        text = 'SUBMIT (as ' + user.name + ')'
        WinCon.confirm_window_button(window, user, text, entry_property, entry_message, row)
        WinConGeneral.close_button(window, window, user, row, 2)


    def print_temp():
        print('closed')

    def show_window(user, code=False): # code for where tasks for just one property are requested, otherwise False
        # Set up window
        window =  WinConGeneral.window(user.root, user, 'Show Tasks', 'medium')

        # Set up frames
        top_frame = WinConGeneral.side_frame(window, user, 'top')
        scroll_frame = WinConGeneral.scroll_frame(window, user)
        bottom_frame = WinConGeneral.side_frame(window, user, 'bottom')

        # Top Frame
        text = 'Tasks for ' + user.name + ':'
        WinConGeneral.title(top_frame, user, text)

        # Scroll Frame
        WinCon.scroll_button_list(window, scroll_frame, user, code)

        # Bottom Frame
        WinCon.add_window_button(bottom_frame, user)
        WinCon.close_show_window_button(window, bottom_frame, user)

        # Add window and scroll frame to user so can be refreshed from outside of method
        user.task_win.show_windows.insert(0, [window, scroll_frame, code])
        # Close window sent through method so can be removed from user
        window.protocol("WM_DELETE_WINDOW", lambda: WinCon.close_show_window(window, user))
