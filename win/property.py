
from tkinter import Toplevel,\
                    Label,\
                    Entry,\
                    Button,\
                    PhotoImage,\
                    Frame,\
                    Scrollbar,\
                    Listbox,\
                    LabelFrame
from win.vertical_scrolled_frame import VerticalScrolledFrame
from win.action import ActionWin
from wincon.general import WinConGeneral
from wincon.property import WinConProperty
from lib.property import Property
from lib.custom import Custom

class PropertyWin:
    # view items used in add property window

    def add_property(root, show_window, add_window, user, code, address):
        user.add_property(code, address)
        add_window.destroy()
        Property.save_properties(user)
        # Only where there is a show_window
        if show_window != False:
            show_window.destroy()
            PropertyWin.show_window(root, user, False)

    def update_property(root, window, scroll_frame, user, number, type, new):
        user.properties[number].update_property(type, new)
        WinConProperty.scroll_button_list(root, window, scroll_frame, user, number)
        Property.save_properties(user)

    def see_window(root, window, scroll_frame, user, number):
        see_property_window = Toplevel(window)
        see_property_window.title('Property Python - See Property')
        see_property_window.iconbitmap('icon.ico')
        see_property_window.configure(bg=user.window_bg_colour)
        see_property_window.minsize(user.medium_window_width, user.medium_window_height)

        label_code = Label(see_property_window, text='Code:', font=user.large_font, bg=user.window_bg_colour)
        label_code.grid(row=0, column=0, rowspan=2, padx=user.padx, pady=user.pady)
        entry_code = Entry(see_property_window, bd = 3, font=user.standard_font)
        entry_code.grid(row=0, column=1, rowspan=2, padx=user.padx, pady=user.pady)
        entry_code.insert(0, user.properties[number].code)
        button_code = Button(see_property_window, text='update', font=user.standard_font, command=lambda: PropertyWin.update_property(root, window, scroll_frame, user, number, 'code', entry_code.get()))
        button_code.grid(row=0, column=2, rowspan=2, padx=user.padx, pady=user.pady)

        code = 'Code: ' + user.properties[number].code
        label_code_line = Label(see_property_window, text=code, font=user.standard_font, bg=user.window_bg_colour, anchor='w')
        label_code_line.grid(row=0, column=4, padx=20, sticky='nsew')
        label_code_break = Label(see_property_window, text='------------------------------', font=user.standard_font, bg=user.window_bg_colour, anchor='w')
        label_code_break.grid(row=1, column=4, padx=20, sticky='nsew')

        label_address = Label(see_property_window, text='Address:', font=user.large_font, bg=user.window_bg_colour)
        label_address.grid(row=2, column=0, rowspan=2, padx=user.padx, pady=user.pady)
        entry_address = Entry(see_property_window, bd = 3, font=user.standard_font)
        entry_address.grid(row=2, column=1, rowspan=2, padx=user.padx, pady=user.pady)
        entry_address.insert(0, user.properties[number].address)
        button_address = Button(see_property_window, text='update', font=user.standard_font, command=lambda:  PropertyWin.update_property(root, window, scroll_frame, user, number, 'address', entry_address.get()))
        button_address.grid(row=2, column=2, rowspan=2, padx=user.padx, pady=user.pady)

        address = 'Address: ' + user.properties[number].address
        label_address_line = Label(see_property_window, text=address, font=user.standard_font, bg=user.window_bg_colour, anchor='w')
        label_address_line.grid(row=2, column=4, padx=20, sticky='nsew')
        label_address_break = Label(see_property_window, text='------------------------------', font=user.standard_font, bg=user.window_bg_colour, anchor='w')
        label_address_break.grid(row=3, column=4, padx=20, sticky='nsew')

        actions_button = Button(see_property_window, text='View Actions', font=user.large_font, bg=user.button_bg_colour, command=lambda: ActionWin.show_window(root, user, False, user.properties[number].code))
        actions_button.grid(row=4, column=0, sticky='nsew', padx=user.padx, pady=user.pady)

    def confirm_window(root, show_window, add_window, user, code, address):
        confirm_property_window = Toplevel(add_window)
        confirm_property_window.title('Property Python - Confirm Property')
        confirm_property_window.iconbitmap('icon.ico')
        confirm_property_window.configure(bg=user.window_bg_colour_alert)
        confirm_property_window.minsize(user.small_window_width, user.small_window_height)

        title = 'ARE YOU SURE YOU WANT TO ADD PROPERTY?'
        bg = user.window_bg_colour_alert
        WinConGeneral.title(user, confirm_property_window, title, bg)

        property_summary = code + ' - ' + address
        label_code = Label(confirm_property_window, text=property_summary, font=user.standard_font, bg=user.window_bg_colour_alert)
        label_code.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)

        button_text = 'CONFIRM (as ' + user.name + ')'
        button = Button(confirm_property_window, text=button_text, font=user.large_font, bg=user.button_bg_colour, command=lambda: PropertyWin.add_property(root, show_window, add_window, user, code, address))
        button.grid(row=2, column=0, sticky='nsew', padx=user.padx, pady=user.pady)
        cancel_button = Button(confirm_property_window, text="Cancel (don't confirm)", font=user.large_font, bg=user.button_bg_colour, command=lambda: confirm_property_window.destroy())
        cancel_button.grid(row=2, column=1, sticky='nsew', padx=user.padx, pady=user.pady)

    def add_window(root, show_window, user):
        add_property_window = Toplevel(root)
        add_property_window.title('Property Python - Add Property')
        add_property_window.iconbitmap('icon.ico')
        add_property_window.configure(bg=user.window_bg_colour)
        add_property_window.minsize(user.small_window_width, user.small_window_height)

        title = 'Add property as ' + user.name
        WinConGeneral.title(user, add_property_window, title)

        label_code = Label(add_property_window, text='code:', font=user.standard_font, bg=user.window_bg_colour)
        label_code.grid(row=1, column=0, padx=user.padx, pady=user.pady)
        entry_code = Entry(add_property_window, bd = 3, font=user.standard_font)
        entry_code.grid(row=1, column=1, padx=user.padx, pady=user.pady)

        label_address = Label(add_property_window, text='address:', font=user.standard_font, bg=user.window_bg_colour)
        label_address.grid(row=2, column=0, padx=user.padx, pady=user.pady)
        entry_address = Entry(add_property_window, bd = 3, font=user.standard_font)
        entry_address.grid(row=2, column=1, padx=user.padx, pady=user.pady)

        button_text = 'SUBMIT (as ' + user.name + ')'
        button = Button(add_property_window, text=button_text, font=user.large_font, bg=user.button_bg_colour, command=lambda: PropertyWin.confirm_window(root, show_window, add_property_window, user, entry_code.get(), entry_address.get()))
        button.grid(row=3, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)

    def show_window(root, user, number):     # number is for where a see_window is being auto-launched, otherwise False
        window = Toplevel(root)
        window.title('Property Python - Show Properties')
        window.iconbitmap('icon.ico')
        window.configure(bg=user.window_bg_colour)
        window.minsize(user.medium_window_width, user.medium_window_height)

        # Auto-launch see_window
        if number != False:
            PropertyWin.see_window(root, window, user, number)

        # Set up frames
        top_frame = Frame(window, bg=user.window_bg_colour)
        top_frame.pack(side='top', fill='x', expand=0, anchor='n', padx=5, pady=5)
        scroll_frame = VerticalScrolledFrame(window, bg=user.window_bg_colour)
        scroll_frame.pack(fill='both', expand=1, padx=10)
        bottom_frame = Frame(window, bg=user.window_bg_colour)
        bottom_frame.pack(side='bottom', fill='x', expand=0, anchor='n', padx=5, pady=5)

        # Top Frame
        title = 'Properties:'
        WinConGeneral.title(user, top_frame, title)

        # Scroll Frame
        WinConProperty.scroll_button_list(root, window, scroll_frame,
                                         user, number)

        # Bottom Frame
        add_button = Button(bottom_frame, text='Add Property', font=user.large_font, bg=user.button_bg_colour, command=lambda: PropertyWin.add_window(root, window, user))
        add_button.grid(row=0, column=0, sticky='nsew', padx=user.padx, pady=user.pady)
        WinConGeneral.close_button(window, bottom_frame, user)
