from tkinter import Toplevel,\
                    Frame,\
                    Text,\
                    Label,\
                    Entry,\
                    OptionMenu,\
                    Button,\
                    StringVar
from wincon.vertical_scrolled_frame import VerticalScrolledFrame

class WinConGeneral():

    def import_GroupWin(group):
        # Imports relevant 'Win' module for object class type - used for button methods below
        from importlib import import_module
        # warning import_module takes arguments in backwards order ie a.b is (.b, a)
        win_dot_group = import_module('.' + group, 'win')
        # returns GroupWin class
        return getattr(win_dot_group, group.title() + 'Win')

    # Windows

    def bg_set(user, alert):
        # Sets background colour for window
        if alert:
            return user.window_bg_colour_alert
        else:
            return user.window_bg_colour

    def window(toplevel, user, name, size, alert=False):
        # Creates new window
        window = Toplevel(toplevel)
        window.title(user.company_name + ' - ' + name)
        window.iconbitmap(user.company_icon)
        bg = WinConGeneral.bg_set(user, alert)
        window.configure(bg=bg)
        if size == 'small':
            window.minsize(user.small_window_width, user.small_window_height)
        else:
            window.minsize(user.medium_window_width, user.medium_window_height)
        return window

    def close_window(window, window_type, user, group):
        # Closes window and removes window from refresh list
        group_win = getattr(user, group + '_win')
        for win_frame in getattr(group_win, window_type + '_windows')[:]:
            if win_frame[0] == window:
                getattr(group_win, window_type + '_windows').remove(win_frame)
        window.destroy()

    # Frames

    def side_frame(window, user, side):
        frame = Frame(window, bg=user.window_bg_colour)
        frame.pack(side=side, fill='x', expand=0, anchor='n', padx=5, pady=5)
        return frame

    def scroll_frame(window, user):
        frame = VerticalScrolledFrame(window, bg=user.window_bg_colour)
        frame.pack(fill='both', expand=1, padx=10)
        return frame

    # Labels/Text

    def title(frame, user, text, row=0, column=0, alert = False):
        bg = WinConGeneral.bg_set(user, alert)
        label = Label(frame, text=text, font=user.large_font, anchor='w', bg=bg)
        label.grid(row=row, column=column, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)

    def line(frame, user, text, row=0, column=0, alert = False):
        bg = WinConGeneral.bg_set(user, alert)
        label = Label(frame, text=text, font=user.standard_font, anchor='w', bg=bg)
        label.grid(row=row, column=column, columnspan=2, sticky='nsew', padx=user.padx)

    def content(frame, user, text, row=1, column=0, alert = False):
        width = int(user.small_window_width / 5)
        height = int(len(text) / (width * 1)) + 1
        bg = WinConGeneral.bg_set(user, alert)
        text_box = Text(frame, font=user.standard_font, wrap='word', bg=bg, height=height, width=width)
        text_box.grid(row=row, column=column, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)
        text_box.insert('end', text)
        text_box.configure(state='disabled')

    # Entries

    def entry(window, user, text, row, rowspan=1, insert=False):
        label = Label(window, text=text, font=user.standard_font, bg=user.window_bg_colour)
        label.grid(row=row, column=0, rowspan=rowspan, padx=user.padx, pady=user.pady)
        entry = Entry(window, bd = 3, font=user.standard_font)
        entry.grid(row=row, column=1, rowspan=rowspan, sticky='ew', columnspan=2, padx=user.padx, pady=user.pady)
        if insert != False:
            entry.insert(0, insert)
        return entry

    def drop_down(window, user, text, options, row, rowspan=1, insert=False):
        label = Label(window, text=text, font=user.standard_font, bg=user.window_bg_colour)
        label.grid(row=row, column=0, rowspan=rowspan, padx=user.padx, pady=user.pady)
        entry = StringVar()
        drop_down = OptionMenu(window, entry, *options)
        drop_down.config(font=user.standard_font, anchor='w')
        drop_down.grid(row=row, column=1, rowspan=rowspan, sticky='ew', columnspan=2, padx=user.padx, pady=user.pady)
        if insert != False:
            entry.set(insert)
        return entry

    # Buttons

    def close_button(window, window_type, frame, user, group, row=0, column=1, text='Close Window'):
        # Closes different types of windows
        # From 'see'/'show' windows (also removes window from refresh list)
        if window_type:
            button = Button(frame, text=text, font=user.large_font, bg=user.button_bg_colour,
                            command=lambda: WinConGeneral.close_window(window, window_type, user, group))
        # From other windows (where there is no associated refresh list)
        else:
            button = Button(frame, text=text, font=user.large_font, bg=user.button_bg_colour,
                            command=lambda: window.destroy())
        button.grid(row=row, column=column, sticky='nsew', padx=user.padx, pady=user.pady)

    def add_window_button(frame, user, group):
        # Directs to the add object window
        GroupWin = WinConGeneral.import_GroupWin(group)
        text = 'Add ' + group.title()
        button = Button(frame, text=text, font=user.large_font, bg=user.button_bg_colour,
                            command=lambda: GroupWin.add_window(user))
        button.grid(row=0, column=0, sticky='nsew', padx=user.padx, pady=user.pady)

    def confirm_window_button(window, user, group, text, entries, row):
        GroupWin = WinConGeneral.import_GroupWin(group)
        # Directs from the add object window to the confirm add object window
        button = Button(window, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: GroupWin.confirm_window(window, user, entries))
        button.bind('<Return>', lambda e: GroupWin.confirm_window(window, user, entries))
        button.grid(row=row, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)

    def show_window_button(window, user, group, code, row, column=0, rowspan=1):
        # Directs from the see property window to tasks/actions with that property code
        GroupWin = WinConGeneral.import_GroupWin(group)
        text = 'View ' + group.title() + 's'
        button = Button(window, text=text, font=user.large_font, bg=user.button_bg_colour,
                                command=lambda: GroupWin.show_window(user, code))
        button.grid(row=row, column=column, rowspan=rowspan, sticky='nsew', padx=user.padx, pady=user.pady)

    def scroll_button_list(window, frame, user, group, code=False):
        GroupWin = WinConGeneral.import_GroupWin(group)
        width = int(user.medium_window_width/7)
        counter = 0
        for object in getattr(user, group + '_list'):
            bg="gray99"
            text = 'NOT SET UP FOR CLASS TYPE'
            if group == 'task':
                from datetime import date
                from lib.task import Task
                till_due = Task.date_length(str(date.today()), object.due)
                text = object.due + ' (' + str(till_due) + ') - ' + object.property + ' - ' + object.message
                if till_due > 30: bg = 'grey97'
                if till_due < 1: bg = 'orange'
                if till_due < 0: bg = 'tomato'
                if till_due < -5: bg = 'firebrick'
            if group == 'action':
                text = object.date + ' - ' + object.property + ' - ' + object.message
            if group == 'property':
                text = object.code + ' - ' + object.address
            if group == 'landlord':
                text =  object.code + ' - ' + object.surname + ', ' + object.first_names + ' (' + object.title + ') - ' + object.note
            if group == 'contact':
                text =  object.type + ' - ' + object.address + ' (' + object.note + ')'
            # if show all or property code matches
            if code in (False, getattr(object, 'property', False)):
                button = Button(frame.interior, relief='flat', bg=bg,
                    font=user.standard_font, text=text, width=width, anchor='w',
                    command=lambda number=counter: GroupWin.see_window(user, number))
                button.grid(row=counter, column = 0, sticky='nsew', padx=user.padx, pady=user.pady)
            counter += 1
