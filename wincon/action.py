from tkinter import Button
import win.action
from lib.action import Action

class WinConAction():

    def add(add_window, user, property, message):
        user.add_action(property, message)
        add_window.destroy()
        Action.save_actions(user)
        WinConAction.refresh(user)

    def update(user, number, type, new):
        user.actions[number].update_action(type, new)
        Action.save_actions(user)
        WinConAction.refresh(user)

    # Window refresh management

    def refresh(user):
        for win_frame in user.action_win.see_windows:
            win.action.ActionWin.see_window_right(win_frame[0], user, win_frame[1])
        for win_frame in user.action_win.show_windows:
            WinConAction.scroll_button_list(win_frame[0], win_frame[1], user, win_frame[2])

    def close_see_window(window, user):
        for win_frame in user.action_win.see_windows[:]:
            if win_frame[0] == window:
                user.action_win.see_windows.remove(win_frame)
        window.destroy()

    def close_show_window(window, user):
        for win_frame in user.action_win.show_windows[:]:
            if win_frame[0] == window:
                user.action_win.show_windows.remove(win_frame)
        window.destroy()

    # Action Buttons

    def add_button(add_window, confirm_window, user, text, property, message, row):
        button = Button(confirm_window, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: WinConAction.add(add_window, user, property, message))
        button.grid(row=row, column=0, sticky='nsew', padx=user.padx, pady=user.pady)

    def update_button(frame, user, number, type, entry, row, rowspan, insert):
        bg = 'white'
        if entry.get() != insert:
            bg = 'red'
        button_date = Button(frame, text='update', font=user.standard_font, bg=bg,
                             command=lambda: WinConAction.update(user, number, type, entry.get()))
        button_date.grid(row=row, column=3, rowspan=rowspan, padx=user.padx, pady=user.pady)

    # Window Buttons

    # See Window

    def scroll_button_list(window, frame, user, code):
        width = int(user.medium_window_width/7)
        counter = 0
        for action in user.actions:
            text = action.date + ' - ' + action.property + ' - ' + action.message
            # if show all or property code matches
            if code in (False, action.property):
                button = Button(frame.interior, relief='flat', bg="gray99",
                    font=user.standard_font, text=text, width=width, anchor='w',
                    command=lambda number=counter: win.action.ActionWin.see_window(user, number))
                button.grid(row=counter, column = 0, sticky='nsew', padx=user.padx, pady=user.pady)
            counter += 1

    def close_see_window_button(window, frame, user, row=0, column=1, text='Close Window'):
        button = Button(frame, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: WinConAction.close_see_window(window, user))
        button.grid(row=row, column=column, sticky='nsew', padx=user.padx, pady=user.pady)

    # Show Window

    def show_window_button(window, user, code, row, rowspan=1):
        actions_button = Button(window, text='View Actions', font=user.large_font, bg=user.button_bg_colour,
                                command=lambda: win.action.ActionWin.show_window(user, code))
        actions_button.grid(row=row, column=0, rowspan=rowspan, sticky='nsew', padx=user.padx, pady=user.pady)

    def close_show_window_button(window, frame, user, row=0, column=1, text='Close Window'):
        button = Button(frame, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: WinConAction.close_show_window(window, user))
        button.grid(row=row, column=column, sticky='nsew', padx=user.padx, pady=user.pady)

    # Add & Confirm windows

    def add_window_button(frame, user):
        add_button = Button(frame, text='Add Action', font=user.large_font, bg=user.button_bg_colour,
                            command=lambda: win.action.ActionWin.add_window(user))
        add_button.grid(row=0, column=0, sticky='nsew', padx=user.padx, pady=user.pady)

    def confirm_window_button(window, user, text, entry_property, entry_message, row):
        button = Button(window, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: win.action.ActionWin.confirm_window(window, user, entry_property.get(), entry_message.get()))
        button.bind('<Return>', lambda e: win.action.ActionWin.confirm_window(window, user, entry_property.get(), entry_message.get()))
        button.grid(row=row, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)