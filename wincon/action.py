from tkinter import Button
import win.action

class WinConAction():
    def scroll_button_list(root, window, frame, user, number, code):
        width = int(user.medium_window_width/7)
        counter = 0
        for action in user.actions:
            text = action.date + ' - ' + action.property + ' - ' + action.message
            # if show all or property code matches
            if code in (False, action.property):
                button = Button(frame.interior, relief='flat', bg="gray99",
                    font=user.standard_font, text=text, width=width, anchor='w',
                    command=lambda number=counter: win.action.ActionWin.see_window(root, window, frame, user, number, code))
                button.pack(padx=10, pady=5, side='top', fill='x')
            counter += 1
