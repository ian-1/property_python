from tkinter import Button
import win.task
from lib.task import Task

class WinConTask():

    def add(add_window, user, property, message):
        user.add_task(property, message)
        add_window.destroy()
        Task.save(user)
        WinConTask.refresh(user)

    def update(user, number, type, new):
        user.tasks[number].update(type, new)
        Task.save(user)
        WinConTask.refresh(user)

    # Window refresh management

    def refresh(user):
        for win_frame in user.task_win.see_windows:
            win.task.TaskWin.see_window_right(win_frame[0], user, win_frame[1])
        for win_frame in user.task_win.show_windows:
            WinConTask.scroll_button_list(win_frame[0], win_frame[1], user, win_frame[2])

    def close_see_window(window, user):
        for win_frame in user.task_win.see_windows[:]:
            if win_frame[0] == window:
                user.task_win.see_windows.remove(win_frame)
        window.destroy()

    def close_show_window(window, user):
        for win_frame in user.task_win.show_windows[:]:
            if win_frame[0] == window:
                user.task_win.show_windows.remove(win_frame)
        window.destroy()

    # Action Buttons

    def add_button(add_window, confirm_window, user, text, property, message, row):
        button = Button(confirm_window, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: WinConTask.add(add_window, user, property, message))
        button.grid(row=row, column=0, sticky='nsew', padx=user.padx, pady=user.pady)

    def update_button(frame, user, number, type, entry, row, rowspan, insert):
        bg = 'white'
        if entry.get() != insert:
            bg = 'red'
        button_date = Button(frame, text='update', font=user.standard_font, bg=bg,
                             command=lambda: WinConTask.update(user, number, type, entry.get()))
        button_date.grid(row=row, column=3, rowspan=rowspan, padx=user.padx, pady=user.pady)

    # Window Buttons

    # See Window

    def scroll_button_list(window, frame, user, code):
        width = int(user.medium_window_width/7)
        counter = 0
        for task in user.tasks:
            text = task.date + ' - ' + task.property + ' - ' + task.message
            # if show all or property code matches
            if code in (False, task.property):
                button = Button(frame.interior, relief='flat', bg="gray99",
                    font=user.standard_font, text=text, width=width, anchor='w',
                    command=lambda number=counter: win.task.TaskWin.see_window(user, number))
                button.grid(row=counter, column = 0, sticky='nsew', padx=user.padx, pady=user.pady)
            counter += 1

    def close_see_window_button(window, frame, user, row=0, column=1, text='Close Window'):
        button = Button(frame, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: WinConTask.close_see_window(window, user))
        button.grid(row=row, column=column, sticky='nsew', padx=user.padx, pady=user.pady)

    # Show Window

    def show_window_button(window, user, code, row, rowspan=1):
        tasks_button = Button(window, text='View Tasks', font=user.large_font, bg=user.button_bg_colour,
                                command=lambda: win.task.TaskWin.show_window(user, code))
        tasks_button.grid(row=row, column=0, rowspan=rowspan, sticky='nsew', padx=user.padx, pady=user.pady)

    def close_show_window_button(window, frame, user, row=0, column=1, text='Close Window'):
        button = Button(frame, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: WinConTask.close_show_window(window, user))
        button.grid(row=row, column=column, sticky='nsew', padx=user.padx, pady=user.pady)

    # Add & Confirm windows

    def add_window_button(frame, user):
        add_button = Button(frame, text='Add Task', font=user.large_font, bg=user.button_bg_colour,
                            command=lambda: win.task.TaskWin.add_window(user))
        add_button.grid(row=0, column=0, sticky='nsew', padx=user.padx, pady=user.pady)

    def confirm_window_button(window, user, text, entry_property, entry_message, row):
        button = Button(window, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: win.task.TaskWin.confirm_window(window, user, entry_property.get()[0:6], entry_message.get()))
        button.bind('<Return>', lambda e: win.task.TaskWin.confirm_window(window, user, entry_property.get()[0:6], entry_message.get()))
        button.grid(row=row, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)