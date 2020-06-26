
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

    def add_property(window, confirm_window, user, code, address):
        user.add_property(code, address)
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

        label_code = Label(see_property_window, text='code:', font=user.large_font, bg=user.window_bg_colour)
        label_code.grid(row=0, column=0, rowspan=2, padx=user.padx, pady=user.pady)
        entry_code = Entry(see_property_window, bd = 3, font=user.standard_font)
        entry_code.grid(row=0, column=1, rowspan=2, padx=user.padx, pady=user.pady)
        entry_code.insert(0, user.properties[number].code)
        button_code = Button(see_property_window, text='update', font=user.standard_font, command=lambda: PropertyViews.update_property(root, window, user, number, 'code', entry_code.get()))
        button_code.grid(row=0, column=2, rowspan=2, padx=user.padx, pady=user.pady)

        code = 'Code: ' + user.properties[number].code
        label_code_line = Label(see_property_window, text=code, font=user.standard_font, bg=user.window_bg_colour, anchor='w')
        label_code_line.grid(row=0, column=4, padx=20, sticky='nsew')
        label_code_break = Label(see_property_window, text='------------------------------', font=user.standard_font, bg=user.window_bg_colour, anchor='w')
        label_code_break.grid(row=1, column=4, padx=20, sticky='nsew')

        label_address = Label(see_property_window, text='address:', font=user.large_font, bg=user.window_bg_colour)
        label_address.grid(row=2, column=0, rowspan=2, padx=user.padx, pady=user.pady)
        entry_address = Entry(see_property_window, bd = 3, font=user.standard_font)
        entry_address.grid(row=2, column=1, rowspan=2, padx=user.padx, pady=user.pady)
        entry_address.insert(0, user.properties[number].address)
        button_address = Button(see_property_window, text='update', font=user.standard_font, command=lambda:  PropertyViews.update_property(root, window, user, number, 'address', entry_address.get()))
        button_address.grid(row=2, column=2, rowspan=2, padx=user.padx, pady=user.pady)

        address = 'Address: ' + user.properties[number].address
        label_address_line = Label(see_property_window, text=address, font=user.standard_font, bg=user.window_bg_colour, anchor='w')
        label_address_line.grid(row=2, column=4, padx=20, sticky='nsew')
        label_address_break = Label(see_property_window, text='------------------------------', font=user.standard_font, bg=user.window_bg_colour, anchor='w')
        label_address_break.grid(row=3, column=4, padx=20, sticky='nsew')

    def confirm_window(window, user, code, address):
        confirm_property_window = Toplevel(window)
        confirm_property_window.title('Property Python - Confirm Property')
        confirm_property_window.iconbitmap('icon.ico')
        confirm_property_window.configure(bg=user.window_bg_colour)
        confirm_property_window.minsize(user.small_window_width, user.small_window_height)

        label_title = Label(confirm_property_window, text='Check and confirm property:', font=user.large_font, anchor='w', bg=user.window_bg_colour)
        label_title.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)


        property_summary = code + ' - ' + address
        label_code = Label(confirm_property_window, text=property_summary, font=user.standard_font, bg=user.window_bg_colour)
        label_code.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)

        button_text = 'CONFIRM (as ' + user.name + ')'
        button = Button(confirm_property_window, text=button_text, font=user.large_font, bg=user.button_bg_colour, command=lambda: PropertyViews.add_property(window, confirm_property_window, user, code, address))
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

        label_code = Label(add_property_window, text='code:', font=user.standard_font, bg=user.window_bg_colour)
        label_code.grid(row=1, column=0, padx=user.padx, pady=user.pady)
        entry_code = Entry(add_property_window, bd = 3, font=user.standard_font)
        entry_code.grid(row=1, column=1, padx=user.padx, pady=user.pady)

        label_address = Label(add_property_window, text='address:', font=user.standard_font, bg=user.window_bg_colour)
        label_address.grid(row=2, column=0, padx=user.padx, pady=user.pady)
        entry_address = Entry(add_property_window, bd = 3, font=user.standard_font)
        entry_address.grid(row=2, column=1, padx=user.padx, pady=user.pady)

        button_text = 'SUBMIT (as ' + user.name + ')'
        button = Button(add_property_window, text=button_text, font=user.large_font, bg=user.button_bg_colour, command=lambda: PropertyViews.confirm_window(add_property_window, user, entry_code.get(), entry_address.get()))
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
            property_summary = property.code + ' - ' + property.address
            button_property = Button(scroll_frame.interior, relief='flat', bg="gray99",
                font=user.standard_font, text=property_summary, width=width, anchor='w',
                command=lambda number=counter: PropertyViews.see_window(root, show_properties_window, user, number))
            button_property.pack(padx=10, pady=5, side='top', fill='x')
            counter += 1

        add_button = Button(bottom_frame, text='Add Property', font=user.large_font, bg=user.button_bg_colour, command=lambda: PropertyViews.add_window(root, user))
        add_button.grid(row=0, column=0, sticky='nsew', padx=user.padx, pady=user.pady)
        close_button = Button(bottom_frame, text='Close Window', font=user.large_font, bg=user.button_bg_colour, command=lambda: show_properties_window.destroy())
        close_button.grid(row=0, column=1, sticky='nsew', padx=user.padx, pady=user.pady)
