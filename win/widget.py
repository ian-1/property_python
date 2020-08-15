from tkinter import Toplevel,\
                    Frame,\
                    Text,\
                    Label,\
                    Entry,\
                    OptionMenu,\
                    Button,\
                    StringVar
from win.vertical_scrolled_frame import VerticalScrolledFrame
import win.window as Window

# GENERAL WIDGETS

# Widget sub-methods

def import_ClassTypeLib(class_type):
    # Method imports relevant class module for object class type
    from importlib import import_module
    # warning import_module takes arguments in backwards order ie a.b is (.b, a)
    lib_dot_class_type = import_module('.' + class_type, 'lib')
    # returns class_type class
    return getattr(lib_dot_class_type, class_type.title())

def import_ClassTypeWin(class_type):
    # Method imports relevant 'Win' module for object class type
    from importlib import import_module
    # warning import_module takes arguments in backwards order ie a.b is (.b, a)
    win_dot_class_type = import_module('.' + class_type, 'win')
    # returns ClassTypeWin class
    return getattr(win_dot_class_type, class_type.title() + 'Win')

def add(add_window, user, class_type, data, open=False):
    user.add(user, class_type, data)
    add_window.destroy()
    user.save_all_class_type(class_type)
    refresh(user)
    if open:
        # Currently only used by property, needs to be generalised if to be used elsewhere
        from lib.property import Property
        import win.property
        number = Property.number_from_code(user, data['code'])
        win.property.PropertyWin.see_window(user, number)

def update(user, class_type, number, type, new):
    class_list = getattr(user, class_type + '_list')
    class_list[number].update(type, new)
    user.save_all_class_type(class_type)
    refresh(user)

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
    bg = bg_set(user, alert)
    window.configure(bg=bg)
    if size == 'small':
        window.minsize(user.small_window_width, user.small_window_height)
    else:
        window.minsize(user.medium_window_width, user.medium_window_height)
    return window

def close_window(window, window_type, user, class_type):
    # Closes window and removes window from refresh list
    win_frame_list = getattr(user, class_type + '_' + window_type + '_windows')
    for win_frame in win_frame_list[:]:
        if win_frame[0] == window:
            win_frame_list.remove(win_frame)
    window.destroy()

def refresh(user):
    # Refreshes windows refresh lists
    for class_type in user.class_types:
        ClassTypeWin = import_ClassTypeWin(class_type)
        for win_frame in getattr(user, class_type + '_see_windows'):
            ClassTypeWin.see_window_right(win_frame[0], user, win_frame[1])
        for win_frame in getattr(user, class_type + '_show_windows'):
            scroll_button_list(win_frame[0], win_frame[1], user, class_type, win_frame[2])

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
    bg = bg_set(user, alert)
    label = Label(frame, text=text, font=user.large_font, anchor='w', bg=bg)
    label.grid(row=row, column=column, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)

def line(frame, user, text, row=0, column=0, alert = False):
    bg = bg_set(user, alert)
    label = Label(frame, text=text, font=user.standard_font, anchor='w', bg=bg)
    label.grid(row=row, column=column, columnspan=2, sticky='nsew', padx=user.padx)

def content(frame, user, text, row=1, column=0, alert = False):
    width = int(user.small_window_width / 5)
    height = int(len(text) / (width * 1)) + 1
    bg = bg_set(user, alert)
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

# Window Buttons

def close_button(window, window_type, frame, user, class_type, row=0, column=1, text='Close Window'):
    # Closes different types of windows
    # From 'see'/'show' windows (also removes window from refresh list)
    if window_type:
        button = Button(frame, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: close_window(window, window_type, user, class_type))
    # From other windows (where there is no associated refresh list)
    else:
        button = Button(frame, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: window.destroy())
    button.grid(row=row, column=column, sticky='nsew', padx=user.padx, pady=user.pady)

def add_window_button(frame, user, class_type, number=False, row=0, column=0):
    # Directs to the add object window
    ClassTypeWin = import_ClassTypeWin(class_type)
    text = 'Add ' + class_type.title()
    button = Button(frame, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: Window.add_window(user, class_type, number))
    button.grid(row=row, column=column, sticky='nsew', padx=user.padx, pady=user.pady)

def confirm_window_button(window, user, class_type, text, entries, row):
    ClassTypeWin = import_ClassTypeWin(class_type)
    # Directs from the add object window to the confirm add object window
    button = Button(window, text=text, font=user.large_font, bg=user.button_bg_colour,
                    command=lambda: ClassTypeWin.confirm_window(window, user, entries))
    button.bind('<Return>', lambda e: ClassTypeWin.confirm_window(window, user, entries))
    button.grid(row=row, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)

def show_window_button(window, user, class_type, code, row, column=0, rowspan=1):
    # Directs from the see property window to tasks/actions with that property code
    text = 'View ' + class_type.title() + 's'
    button = Button(window, text=text, font=user.large_font, bg=user.button_bg_colour,
                    command=lambda: Window.show_window(user, class_type, code))
    button.grid(row=row, column=column, rowspan=rowspan, sticky='nsew', padx=user.padx, pady=user.pady)

def see_window_button(window, user, class_type, code, row=0, rowspan=1):
    # Directs ot the see object window
    ClassTypeLib = import_ClassTypeLib(class_type)
    ClassTypeWin = import_ClassTypeWin(class_type)
    object_number = ClassTypeLib.number_from_code(user, code)
    if object_number != False:
        text = 'Open ' + class_type.title()
        button = Button(window, text=text, font=user.large_font, bg=user.button_bg_colour,
                        command=lambda: ClassTypeWin.see_window(user, object_number))
        button.grid(row=row, column=0, rowspan=rowspan, padx=user.padx, pady=user.pady)

# Action Buttons

def add_button(add_window, confirm_window, user, class_type, text, data, row, open=False):
    # Adds object, closes add object window & confirm add object windows and refreshes
    button = Button(confirm_window, text=text, font=user.large_font, bg=user.button_bg_colour,
                    command=lambda: add(add_window, user, class_type, data, open))
    button.grid(row=row, column=0, sticky='nsew', padx=user.padx, pady=user.pady)

def update_button(frame, user, class_type, number, type, entry, row, rowspan=1):
    # Updates data for object and refreshes
    button = Button(frame, text='update', font=user.standard_font,
                    command=lambda: update(user, class_type, number, type, entry.get()))
    button.grid(row=row, column=3, rowspan=rowspan, padx=user.padx, pady=user.pady)

# Scroll Buttons

def scroll_button_display(object, class_type):
    text = 'scroll_button_display NOT SET UP FOR CLASS TYPE'
    bg="gray99"
    if class_type == 'task':
        from datetime import date
        from lib.task import Task
        till_due = Task.date_length(str(date.today()), object.due)
        text = object.due + ' (' + str(till_due) + ') - ' + object.property + ' - ' + object.message
        if till_due > 30: bg = 'grey97'
        if till_due < 1: bg = 'orange'
        if till_due < 0: bg = 'tomato'
        if till_due < -5: bg = 'firebrick'
    if class_type == 'action':
        text = object.date + ' - ' + object.property + ' - ' + object.message
    if class_type == 'property':
        text = object.code + ' - ' + object.address
    if class_type == 'landlord':
        text =  object.code + ' - ' + object.surname + ', ' + object.first_names + ' (' + object.title + ') - ' + object.note
    if class_type == 'contact':
        text =  object.type + ' - ' + object.address + ' (' + object.note + ')'
    return text, bg

def scroll_button_list(window, frame, user, class_type, code=False):
    ClassTypeWin = import_ClassTypeWin(class_type)
    width = int(user.medium_window_width/7)
    counter = 0
    for object in getattr(user, class_type + '_list'):
        # if show all (ie code = False) or if property code matches code
        if code in (False, getattr(object, 'property', False)):
            text, bg = scroll_button_display(object, class_type)
            button = Button(frame.interior, relief='flat', bg=bg,
                font=user.standard_font, text=text, width=width, anchor='w',
                command=lambda number=counter: ClassTypeWin.see_window(user, number))
            button.grid(row=counter, column = 0, sticky='nsew', padx=user.padx, pady=user.pady)
        counter += 1

# CLASS SPECIFIC WIDGETS

# property

def link_landlord_to_property(user, number, landlord_code):
    user.property_list[number].add_landlord(user, landlord_code)
    user.save_all_class_type('property')
    refresh(user)

def link_landlord_to_property_button(frame, user, number, entry, row, rowspan=1):
    button = Button(frame, text='add', font=user.standard_font,
                    command=lambda: link_landlord_to_property(user, number, entry.get()))
    button.grid(row=row, column=3, rowspan=rowspan, padx=user.padx, pady=user.pady)
