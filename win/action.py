
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
import win.property
from wincon.general import WinConGeneral
from wincon.action import WinConAction
from lib.action import Action
from lib.property import Property
from lib.custom import Custom

class ActionWin:
    # view items used in add action window

    def add_action(root, show_window, add_window, user, property, message):
        user.add_action(property, message)
        add_window.destroy()
        Action.save_actions(user)
        # Only where there is a show_window
        if show_window != False:
            show_window.destroy()
            ActionWin.show_window(root, user, False, False)

    def update_action(root, window, scroll_frame, user, number, code, type, new):
        user.actions[number].update_action(type, new)
        WinConAction.scroll_button_list(root, window, scroll_frame, user, number, code)
        Action.save_actions(user)

    def see_window(root, window, scroll_frame, user, number, code):
        see_action_window = Toplevel(window)
        see_action_window.title('Property Python - See Action')
        see_action_window.iconbitmap('icon.ico')
        see_action_window.configure(bg=user.window_bg_colour)
        see_action_window.minsize(user.medium_window_width, user.medium_window_height)

        label_date = Label(see_action_window, text='Date:', font=user.large_font, bg=user.window_bg_colour)
        label_date.grid(row=0, column=0, rowspan=2, padx=user.padx, pady=user.pady)
        entry_date = Entry(see_action_window, bd = 3, font=user.standard_font)
        entry_date.grid(row=0, column=1, rowspan=2, padx=user.padx, pady=user.pady)
        entry_date.insert(0, user.actions[number].date)
        button_date = Button(see_action_window, text='update', font=user.standard_font, command=lambda: ActionWin.update_action(root, window, scroll_frame, user, number, code, 'date', entry_date.get()))
        button_date.grid(row=0, column=2, rowspan=2, padx=user.padx, pady=user.pady)

        date_code = 'Date: ' + user.actions[number].date + '                         ¦     Code: ' + user.actions[number].property
        label_date_code_line = Label(see_action_window, text=date_code, font=user.standard_font, bg=user.window_bg_colour, anchor='w')
        label_date_code_line.grid(row=0, column=4, padx=20, sticky='nsew')
        label_date_code_break = Label(see_action_window, text='------------------------------------------------------------------------------------------------------', font=user.standard_font, bg=user.window_bg_colour, anchor='w')
        label_date_code_break.grid(row=1, column=4, padx=20, sticky='nsew')

        label_property = Label(see_action_window, text='Property:', font=user.large_font, bg=user.window_bg_colour)
        label_property.grid(row=2, column=0, rowspan=2, padx=user.padx, pady=user.pady)
        entry_property = Entry(see_action_window, bd = 3, font=user.standard_font)
        entry_property.grid(row=2, column=1, rowspan=2, padx=user.padx, pady=user.pady)
        entry_property.insert(0, user.actions[number].property)
        button_property = Button(see_action_window, text='update', font=user.standard_font, command=lambda: ActionWin.update_action(root, window, scroll_frame, user, number, code, 'property', entry_property.get()))
        button_property.grid(row=2, column=2, rowspan=2, padx=user.padx, pady=user.pady)

        property = 'Address: ' + Property.address_from_code(user, user.actions[number].property)
        label_property_line = Label(see_action_window, text=property, font=user.standard_font, bg=user.window_bg_colour, anchor='w')
        label_property_line.grid(row=2, column=4, padx=20, sticky='nsew')
        label_property_break = Label(see_action_window, text='------------------------------------------------------------------------------------------------------', font=user.standard_font, bg=user.window_bg_colour, anchor='w')
        label_property_break.grid(row=3, column=4, padx=20, sticky='nsew')

        label_message = Label(see_action_window, text='Message:', font=user.large_font, bg=user.window_bg_colour)
        label_message.grid(row=4, column=0, rowspan=2, padx=user.padx, pady=user.pady)
        entry_message = Entry(see_action_window, bd = 3, font=user.standard_font)
        entry_message.grid(row=4, column=1, rowspan=2, padx=user.padx, pady=user.pady)
        entry_message.insert(0, user.actions[number].message)
        button_message = Button(see_action_window, text='update', font=user.standard_font, command=lambda:  ActionWin.update_action(root, window, scroll_frame, user, number, code, 'message', entry_message.get()))
        button_message.grid(row=4, column=2, rowspan=2, padx=user.padx, pady=user.pady)

        message_array = Custom.split_to_array(user.actions[number].message, 70)
        row = 5
        for line in message_array:
            label_message_line = Label(see_action_window, text=line, font=user.standard_font, bg=user.window_bg_colour, anchor='w')
            label_message_line.grid(row=row, column=4, padx=20, sticky='nsew')
            row+=1

        property_number = Property.number_from_code(user, user.actions[number].property)
        if property_number != False:
            property_button = Button(see_action_window, text='Open Property', font=user.large_font, bg=user.button_bg_colour, command=lambda: win.property.PropertyWin.see_window(root, window, user, property_number))
            property_button.grid(row=6, column=0, rowspan=2, padx=user.padx, pady=user.pady)
        close_button = Button(see_action_window, text='Close Window', font=user.large_font, bg=user.button_bg_colour, command=lambda: see_action_window.destroy())
        close_button.grid(row=6, column=1, rowspan=2, padx=user.padx, pady=user.pady)

    def confirm_window(root, show_window, add_window, user, property, message):
        confirm_action_window = Toplevel(add_window)
        confirm_action_window.title('Property Python - Confirm Action')
        confirm_action_window.iconbitmap('icon.ico')
        confirm_action_window.configure(bg=user.window_bg_colour)
        confirm_action_window.minsize(user.small_window_width, user.small_window_height)

        title = 'Check and confirm action:'
        WinConGeneral.title(user, confirm_action_window, title)

        action_summary = property + ' - ' + message
        label_property = Label(confirm_action_window, text=action_summary, font=user.standard_font, bg=user.window_bg_colour)
        label_property.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)

        button_text = 'CONFIRM (as ' + user.name + ')'
        button = Button(confirm_action_window, text=button_text, font=user.large_font, bg=user.button_bg_colour, command=lambda: ActionWin.add_action(root, show_window, add_window, user, property, message))
        button.grid(row=2, column=0, sticky='nsew', padx=user.padx, pady=user.pady)
        cancel_button = Button(confirm_action_window, text="Cancel (don't confirm)", font=user.large_font, bg=user.button_bg_colour, command=lambda: confirm_action_window.destroy())
        cancel_button.grid(row=2, column=1, sticky='nsew', padx=user.padx, pady=user.pady)

    def add_window(root, show_window, user):
        add_action_window = Toplevel(root)
        add_action_window.title('Property Python - Add Action')
        add_action_window.iconbitmap('icon.ico')
        add_action_window.configure(bg=user.window_bg_colour)
        add_action_window.minsize(user.small_window_width, user.small_window_height)

        title = 'Add action as ' + user.name
        WinConGeneral.title(user, add_action_window, title)

        label_property = Label(add_action_window, text='Property:', font=user.standard_font, bg=user.window_bg_colour)
        label_property.grid(row=1, column=0, padx=user.padx, pady=user.pady)
        entry_property = Entry(add_action_window, bd = 3, font=user.standard_font)
        entry_property.grid(row=1, column=1, padx=user.padx, pady=user.pady)

        label_message = Label(add_action_window, text='Message:', font=user.standard_font, bg=user.window_bg_colour)
        label_message.grid(row=2, column=0, padx=user.padx, pady=user.pady)
        entry_message = Entry(add_action_window, bd = 3, font=user.standard_font)
        entry_message.grid(row=2, column=1, padx=user.padx, pady=user.pady)

        button_text = 'SUBMIT (as ' + user.name + ')'
        button = Button(add_action_window, text=button_text, font=user.large_font, bg=user.button_bg_colour, command=lambda: ActionWin.confirm_window(root, show_window, add_action_window, user, entry_property.get(), entry_message.get()))
        button.grid(row=3, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)

    def show_window(root, user, number, code):
        # number is for where a see_window is being auto-launched, otherwise False
        # code if for where actions for just one property are requested, otherwise False
        window = Toplevel(root)
        window.title('Property Python - Show Actions')
        window.iconbitmap('icon.ico')
        window.configure(bg=user.window_bg_colour)
        window.minsize(user.medium_window_width, user.medium_window_height)

        # Auto-launch see_window
        if number != False:
            ActionWin.see_window(root, window, user, number, code)

        # Set up frames
        top_frame = Frame(window, bg=user.window_bg_colour)
        top_frame.pack(side='top', fill='x', expand=0, anchor='n', padx=5, pady=5)
        scroll_frame = VerticalScrolledFrame(window, bg=user.window_bg_colour)
        scroll_frame.pack(fill='both', expand=1, padx=10)
        bottom_frame = Frame(window, bg=user.window_bg_colour)
        bottom_frame.pack(side='bottom', fill='x', expand=0, anchor='n', padx=5, pady=5)

        # Top Frame
        title = 'Actions for ' + user.name + ':'
        WinConGeneral.title(user, top_frame, title)

        # Scroll Frame
        WinConAction.scroll_button_list(root, window, scroll_frame, user, number, code)

        # Bottom Frame
        add_button = Button(bottom_frame, text='Add Action', font=user.large_font, bg=user.button_bg_colour, command=lambda: ActionWin.add_window(root, window, user))
        add_button.grid(row=0, column=0, sticky='nsew', padx=user.padx, pady=user.pady)
        WinConGeneral.close_button(window, bottom_frame, user)
