from tkinter import Button
import win.property

class WinConProperty():
    def scroll_button_list(root, window, frame, user, number):
        width = int(user.medium_window_width/7)
        counter = 0
        for property in user.properties:
            text = property.code + ' - ' + property.address
            button = Button(frame.interior, relief='flat', bg="gray99",
                font=user.standard_font, text=text, width=width, anchor='w',
                command=lambda number=counter: win.property.PropertyWin.see_window(root, window, frame, user, number))
            button.pack(padx=10, pady=5, side='top', fill='x')
            counter += 1
