
from tkinter import Toplevel,\
                    Label,\
                    Entry,\
                    Button,\
                    PhotoImage,\
                    Frame,\
                    Scrollbar,\
                    Listbox,\
                    LabelFrame
from views.vertical_scrolled_frame import VerticalScrolledFrame
from lib.property import Property
from lib.custom import Custom

class PropertyViews:
    # view items used in add property window

    def add_property(window, confirm_window, user, action, message):
        user.add_property(action, message)
        confirm_window.destroy()
        window.destroy()
        Property.save_properties(user)

    def update_property(root, window, user, number, type, new):
        user.properties[number].update_property(type, new)
        window.destroy()
        Property.save_properties(user)
        PropertyViews.show_window(root, user, number)  # inclusion of number auto_launches new see_window


    def see_window(root, window, user, number):
        see_property_window = Toplevel(window)
        see_property_window.title('Property Python - See Property')
        see_property_window.iconbitmap('icon.ico')
        see_property_window.configure(bg=user.window_bg_colour)
        see_property_window.minsize(user.medium_window_width, user.medium_window_height)

        label_date = Label(see_property_window, text='Date:', font=user.large_font, bg=user.window_bg_colour)
        label_date.grid(row=0, column=0, rowspan=2, padx=user.padx, pady=user.pady)
        entry_date = Entry(see_property_window, bd = 3, font=user.standard_font)
        entry_date.grid(row=0, column=1, rowspan=2, padx=user.padx, pady=user.pady)
        entry_date.insert(0, user.properties[number].date)
        button_date = Button(see_property_window, text='update', font=user.standard_font, command=lambda: PropertyViews.update_property(root, window, user, number, 'date', entry_date.get()))
        button_date.grid(row=0, column=2, rowspan=2, padx=user.padx, pady=user.pady)

        date = 'Date: ' + user.properties[number].date
        label_date_line = Label(see_property_window, text=date, font=user.standard_font, bg=user.window_bg_colour, anchor='w')
        label_date_line.grid(row=0, column=4, padx=20, sticky='nsew')
        label_date_break = Label(see_property_window, text='------------------------------', font=user.standard_font, bg=user.window_bg_colour, anchor='w')
        label_date_break.grid(row=1, column=4, padx=20, sticky='nsew')

        label_action = Label(see_property_window, text='action:', font=user.large_font, bg=user.window_bg_colour)
        label_action.grid(row=2, column=0, rowspan=2, padx=user.padx, pady=user.pady)
        entry_action = Entry(see_property_window, bd = 3, font=user.standard_font)
        entry_action.grid(row=2, column=1, rowspan=2, padx=user.padx, pady=user.pady)
        entry_action.insert(0, user.properties[number].action)
        button_action = Button(see_property_window, text='update', font=user.standard_font, command=lambda: PropertyViews.update_property(root, window, user, number, 'action', entry_action.get()))
        button_action.grid(row=2, column=2, rowspan=2, padx=user.padx, pady=user.pady)

        action = 'action: ' + user.properties[number].action
        label_action_line = Label(see_property_window, text=action, font=user.standard_font, bg=user.window_bg_colour, anchor='w')
        label_action_line.grid(row=2, column=4, padx=20, sticky='nsew')
        label_action_break = Label(see_property_window, text='------------------------------', font=user.standard_font, bg=user.window_bg_colour, anchor='w')
        label_action_break.grid(row=3, column=4, padx=20, sticky='nsew')

        label_message = Label(see_property_window, text='Message:', font=user.large_font, bg=user.window_bg_colour)
        label_message.grid(row=4, column=0, rowspan=2, padx=user.padx, pady=user.pady)
        entry_message = Entry(see_property_window, bd = 3, font=user.standard_font)
        entry_message.grid(row=4, column=1, rowspan=2, padx=user.padx, pady=user.pady)
        entry_message.insert(0, user.properties[number].message)
        button_message = Button(see_property_window, text='update', font=user.standard_font, command=lambda:  PropertyViews.update_property(root, window, user, number, 'message', entry_message.get()))
        button_message.grid(row=4, column=2, rowspan=2, padx=user.padx, pady=user.pady)

        message_array = Custom.split_to_array(user.properties[number].message, 70)
        row = 5
        for line in message_array:
            label_message_line = Label(see_property_window, text=line, font=user.standard_font, bg=user.window_bg_colour, anchor='w')
            label_message_line.grid(row=row, column=4, padx=20, sticky='nsew')
            row+=1

    def confirm_window(window, user, action, message):
        confirm_property_window = Toplevel(window)
        confirm_property_window.title('Property Python - Confirm Property')
        confirm_property_window.iconbitmap('icon.ico')
        confirm_property_window.configure(bg=user.window_bg_colour)
        confirm_property_window.minsize(user.small_window_width, user.small_window_height)

        label_title = Label(confirm_property_window, text='Check and confirm property:', font=user.large_font, anchor='w', bg=user.window_bg_colour)
        label_title.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)


        property_summary = action + ' - ' + message
        label_action = Label(confirm_property_window, text=property_summary, font=user.standard_font, bg=user.window_bg_colour)
        label_action.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)

        button_text = 'CONFIRM (as ' + user.name + ')'
        button = Button(confirm_property_window, text=button_text, font=user.large_font, bg=user.button_bg_colour, command=lambda: PropertyViews.add_property(window, confirm_property_window, user, action, message))
        button.grid(row=2, column=0, sticky='nsew', padx=user.padx, pady=user.pady)
        cancel_button = Button(confirm_property_window, text="Cancel (don't confirm)", font=user.large_font, bg=user.button_bg_colour, command=lambda: confirm_property_window.destroy())
        cancel_button.grid(row=2, column=1, sticky='nsew', padx=user.padx, pady=user.pady)

    def add_window(window, user):
        add_property_window = Toplevel(window)
        add_property_window.title('Property Python - Add Property')
        add_property_window.iconbitmap('icon.ico')
        add_property_window.configure(bg=user.window_bg_colour)
        add_property_window.minsize(user.small_window_width, user.small_window_height)

        title = 'Add property as ' + user.name
        label_title = Label(add_property_window, text=title, font=user.large_font, anchor='w', bg=user.window_bg_colour)
        label_title.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)

        label_action = Label(add_property_window, text='action:', font=user.standard_font, bg=user.window_bg_colour)
        label_action.grid(row=1, column=0, padx=user.padx, pady=user.pady)
        entry_action = Entry(add_property_window, bd = 3, font=user.standard_font)
        entry_action.grid(row=1, column=1, padx=user.padx, pady=user.pady)

        label_message = Label(add_property_window, text='Message:', font=user.standard_font, bg=user.window_bg_colour)
        label_message.grid(row=2, column=0, padx=user.padx, pady=user.pady)
        entry_message = Entry(add_property_window, bd = 3, font=user.standard_font)
        entry_message.grid(row=2, column=1, padx=user.padx, pady=user.pady)

        button_text = 'SUBMIT (as ' + user.name + ')'
        button = Button(add_property_window, text=button_text, font=user.large_font, bg=user.button_bg_colour, command=lambda: PropertyViews.confirm_window(add_property_window, user, entry_action.get(), entry_message.get()))
        button.grid(row=3, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)

    def show_window(root, user, number):     # number is for where a see_window is being auto-launched, otherwise False
        show_properties_window = Toplevel(root)
        show_properties_window.title('Property Python - Show Properties')
        show_properties_window.iconbitmap('icon.ico')
        show_properties_window.configure(bg=user.window_bg_colour)
        show_properties_window.minsize(user.medium_window_width, user.medium_window_height)

        # Auto-launch see_window
        if number != False:
            PropertyViews.see_window(root, show_properties_window, user, number)

        top_frame = Frame(show_properties_window, bg=user.window_bg_colour)
        top_frame.pack(side='top', fill='x', expand=0, anchor='n', padx=5, pady=5)
        scroll_frame = VerticalScrolledFrame(show_properties_window, bg=user.window_bg_colour)
        scroll_frame.pack(fill='both', expand=1, padx=10)
        bottom_frame = Frame(show_properties_window, bg=user.window_bg_colour)
        bottom_frame.pack(side='bottom', fill='x', expand=0, anchor='n', padx=5, pady=5)

        title = 'Properties:'
        label_title = Label(top_frame, text=title, font=user.large_font, anchor='w', bg=user.window_bg_colour)
        label_title.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)

        width = int(user.medium_window_width/7)
        counter = 0
        for property in user.properties:
            property_summary = Property.date + ' - ' + Property.action + ' - ' + Property.message
            button_property = Button(scroll_frame.interior, relief='flat', bg="gray99",
                font=user.standard_font, text=property_summary, width=width, anchor='w',
                command=lambda number=counter: PropertyViews.see_window(root, show_properties_window, user, number))
            button_property.pack(padx=10, pady=5, side='top', fill='x')
            counter += 1

        add_button = Button(bottom_frame, text='Add Property', font=user.large_font, bg=user.button_bg_colour, command=lambda: PropertyViews.add_window(root, user))
        add_button.grid(row=0, column=0, sticky='nsew', padx=user.padx, pady=user.pady)
        close_button = Button(bottom_frame, text='Close Window', font=user.large_font, bg=user.button_bg_colour, command=lambda: show_properties_window.destroy())
        close_button.grid(row=0, column=1, sticky='nsew', padx=user.padx, pady=user.pady)
