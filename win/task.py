import win.widget as Widget
from lib.task import Task
from lib.property import Property
from datetime import date

class TaskWin:
    def see_window_left(window, user, number):
        row = 0

        insert = user.task_list[number].date
        entry_date = Widget.entry(window, user, 'Start date:', row, 2, insert)
        Widget.update_button(window, user, 'task', number, 'date', entry_date, row, 2)
        row += 2

        insert = user.task_list[number].property
        entry_property = Widget.entry(window, user, 'Property:', row, 2, insert)
        Widget.update_button(window, user, 'task', number, 'property', entry_property, row, 2)
        row += 2

        insert = user.task_list[number].due
        entry_due = Widget.entry(window, user, 'Due date:', row, 2, insert)
        Widget.update_button(window, user, 'task', number, 'due', entry_due, row, 2)
        row += 2

        insert = user.task_list[number].message
        entry_message = Widget.entry(window, user, 'Message:', row, 2, insert)
        Widget.update_button(window, user, 'task', number, 'message', entry_message, row, 2)
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
