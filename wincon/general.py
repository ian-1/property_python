from tkinter import Label,\
                    Button

class WinConGeneral():

    def title(user, frame, text, bg = False):
        if bg == False:
            # Sets the default bg colour if no bg given
            bg = user.window_bg_colour
        label = Label(frame, text=text, font=user.large_font, anchor='w', bg=bg)
        label.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)

    def close_button(window, frame, user):
        text = 'Close Window'
        button = Button(frame, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: window.destroy())
        button.grid(row=0, column=1, sticky='nsew', padx=user.padx, pady=user.pady)
