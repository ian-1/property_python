from tkinter import Button
import win.task
from lib.task import Task

class WinConTask():

    def add(add_window, user, property, message):
        user.add_task(user, property, message)
        add_window.destroy()
        user.save_all_class_type('task')
        WinConTask.refresh(user)

    def update(user, number, type, new):
        user.task_list[number].update(type, new)
        user.save_all_class_type('task')
        WinConTask.refresh(user)

    # Window refresh management

    def refresh(user):
        import win.widget as Widget
        for win_frame in user.task_win.see_windows:
            win.task.TaskWin.see_window_right(win_frame[0], user, win_frame[1])
        for win_frame in user.task_win.show_windows:
            Widget.scroll_button_list(win_frame[0], win_frame[1], user, 'task', win_frame[2])

    # Action Buttons

    def add_button(add_window, confirm_window, user, text, property, message, row):
        button = Button(confirm_window, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: WinConTask.add(add_window, user, property, message))
        button.grid(row=row, column=0, sticky='nsew', padx=user.padx, pady=user.pady)

    def update_button(frame, user, number, type, entry, row, rowspan, insert):
        bg = 'white'
        if entry.get() != insert:
            bg = 'red'
        button = Button(frame, text='update', font=user.standard_font, bg=bg,
                             command=lambda: WinConTask.update(user, number, type, entry.get()))
        button.grid(row=row, column=3, rowspan=rowspan, padx=user.padx, pady=user.pady)
