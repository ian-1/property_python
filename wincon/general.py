from tkinter import Toplevel,\
                    Frame,\
                    Text,\
                    Label,\
                    Entry,\
                    Button
from wincon.vertical_scrolled_frame import VerticalScrolledFrame

class WinConGeneral():

    def bg_set(user, alert):
        if alert == True:
            return user.window_bg_colour_alert
        else:
            return user.window_bg_colour

    # Windows

    def window(toplevel, user, name, type, alert=False):
        window = Toplevel(toplevel)
        window.title(user.company_name + ' - ' + name)
        window.iconbitmap(user.company_icon)
        bg = WinConGeneral.bg_set(user, alert)
        window.configure(bg=bg)
        if type == 'small':
            window.minsize(user.small_window_width, user.small_window_height)
        else:
            window.minsize(user.medium_window_width, user.medium_window_height)
        return window

    # Standard Frames

    def side_frame(window, user, side):
        frame = Frame(window, bg=user.window_bg_colour)
        frame.pack(side=side, fill='x', expand=0, anchor='n', padx=5, pady=5)
        return frame

    def scroll_frame(window, user):
        frame = VerticalScrolledFrame(window, bg=user.window_bg_colour)
        frame.pack(fill='both', expand=1, padx=10)
        return frame

    # Standard Labels/Text

    def title(frame, user, text, row=0, column=0, alert = False):
        bg = WinConGeneral.bg_set(user, alert)
        label = Label(frame, text=text, font=user.large_font, anchor='w', bg=bg)
        label.grid(row=row, column=column, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)

    def line(frame, user, text, row=0, column=0, alert = False):
        bg = WinConGeneral.bg_set(user, alert)
        label = Label(frame, text=text, font=user.standard_font, anchor='w', bg=bg)
        label.grid(row=row, column=column, sticky='nsew', padx=user.padx)

    def content(frame, user, text, row=1, column=0, alert = False):
                width = int(user.small_window_width / 5)
                height = int(len(text) / (width * 1)) + 1
                bg = WinConGeneral.bg_set(user, alert)
                text_box = Text(frame, font=user.standard_font, wrap='word', bg=bg, height=height, width=width)
                text_box.grid(row=row, column=column, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)
                text_box.insert('end', text)
                text_box.configure(state='disabled')

    # Standard Entries

    def entry(window, user, text, row, rowspan=1, insert=False):
                label = Label(window, text=text, font=user.standard_font, bg=user.window_bg_colour)
                label.grid(row=row, column=0, rowspan=rowspan, padx=user.padx, pady=user.pady)
                entry = Entry(window, bd = 3, font=user.standard_font)
                entry.grid(row=row, column=1, rowspan=rowspan, columnspan=2, padx=user.padx, pady=user.pady)
                if insert != False:
                    entry.insert(0, insert)
                return entry

    # Standard Buttons

    def close_button(window, frame, user, row=0, column=1, text='Close Window'):
        button = Button(frame, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: window.destroy())
        button.grid(row=row, column=column, sticky='nsew', padx=user.padx, pady=user.pady)
