
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
from lib.action import Action
from lib.custom import Custom

class ActionViews:
    # view items used in add action window

    def add_action(window, confirm_window, user, property, message):
        user.add_action(property, message)
        confirm_window.destroy()
        window.destroy()
        Action.save_actions(user)

    def update_action(root, window, user, number, type, new):
        user.actions[number].update_action(type, new)
        window.destroy()
        Action.save_actions(user)
        ActionViews.show_window(root, user, number)  # inclusion of number auto_launches new see_window


    def see_window(root, window, user, number):
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
        button_date = Button(see_action_window, text='update', font=user.standard_font, command=lambda: ActionViews.update_action(root, window, user, number, 'date', entry_date.get()))
        button_date.grid(row=0, column=2, rowspan=2, padx=user.padx, pady=user.pady)

        date = 'Date: ' + user.actions[number].date
        label_date_line = Label(see_action_window, text=date, font=user.standard_font, bg=user.window_bg_colour, anchor='w')
        label_date_line.grid(row=0, column=4, padx=20, sticky='nsew')
        label_date_break = Label(see_action_window, text='------------------------------', font=user.standard_font, bg=user.window_bg_colour, anchor='w')
        label_date_break.grid(row=1, column=4, padx=20, sticky='nsew')

        label_property = Label(see_action_window, text='Property:', font=user.large_font, bg=user.window_bg_colour)
        label_property.grid(row=2, column=0, rowspan=2, padx=user.padx, pady=user.pady)
        entry_property = Entry(see_action_window, bd = 3, font=user.standard_font)
        entry_property.grid(row=2, column=1, rowspan=2, padx=user.padx, pady=user.pady)
        entry_property.insert(0, user.actions[number].property)
        button_property = Button(see_action_window, text='update', font=user.standard_font, command=lambda: ActionViews.update_action(root, window, user, number, 'property', entry_property.get()))
        button_property.grid(row=2, column=2, rowspan=2, padx=user.padx, pady=user.pady)

        property = 'Property: ' + user.actions[number].property
        label_property_line = Label(see_action_window, text=property, font=user.standard_font, bg=user.window_bg_colour, anchor='w')
        label_property_line.grid(row=2, column=4, padx=20, sticky='nsew')
        label_property_break = Label(see_action_window, text='------------------------------', font=user.standard_font, bg=user.window_bg_colour, anchor='w')
        label_property_break.grid(row=3, column=4, padx=20, sticky='nsew')

        label_message = Label(see_action_window, text='Message:', font=user.large_font, bg=user.window_bg_colour)
        label_message.grid(row=4, column=0, rowspan=2, padx=user.padx, pady=user.pady)
        entry_message = Entry(see_action_window, bd = 3, font=user.standard_font)
        entry_message.grid(row=4, column=1, rowspan=2, padx=user.padx, pady=user.pady)
        entry_message.insert(0, user.actions[number].message)
        button_message = Button(see_action_window, text='update', font=user.standard_font, command=lambda:  ActionViews.update_action(root, window, user, number, 'message', entry_message.get()))
        button_message.grid(row=4, column=2, rowspan=2, padx=user.padx, pady=user.pady)

        message_array = Custom.split_to_array(user.actions[number].message, 70)
        row = 5
        for line in message_array:
            label_message_line = Label(see_action_window, text=line, font=user.standard_font, bg=user.window_bg_colour, anchor='w')
            label_message_line.grid(row=row, column=4, padx=20, sticky='nsew')
            row+=1

    def confirm_window(window, user, property, message):
        confirm_action_window = Toplevel(window)
        confirm_action_window.title('Property Python - Confirm Action')
        confirm_action_window.iconbitmap('icon.ico')
        confirm_action_window.configure(bg=user.window_bg_colour)
        confirm_action_window.minsize(user.small_window_width, user.small_window_height)

        label_title = Label(confirm_action_window, text='Check and confirm action:', font=user.large_font, anchor='w', bg=user.window_bg_colour)
        label_title.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)


        action_summary = property + ' - ' + message
        label_property = Label(confirm_action_window, text=action_summary, font=user.standard_font, bg=user.window_bg_colour)
        label_property.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)

        button_text = 'CONFIRM (as ' + user.name + ')'
        button = Button(confirm_action_window, text=button_text, font=user.large_font, bg=user.button_bg_colour, command=lambda: ActionViews.add_action(window, confirm_action_window, user, property, message))
        button.grid(row=2, column=0, sticky='nsew', padx=user.padx, pady=user.pady)
        cancel_button = Button(confirm_action_window, text="Cancel (don't confirm)", font=user.large_font, bg=user.button_bg_colour, command=lambda: confirm_action_window.destroy())
        cancel_button.grid(row=2, column=1, sticky='nsew', padx=user.padx, pady=user.pady)

    def add_window(window, user):
        add_action_window = Toplevel(window)
        add_action_window.title('Property Python - Add Action')
        add_action_window.iconbitmap('icon.ico')
        add_action_window.configure(bg=user.window_bg_colour)
        add_action_window.minsize(user.small_window_width, user.small_window_height)

        title = 'Add action as ' + user.name
        label_title = Label(add_action_window, text=title, font=user.large_font, anchor='w', bg=user.window_bg_colour)
        label_title.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)

        label_property = Label(add_action_window, text='Property:', font=user.standard_font, bg=user.window_bg_colour)
        label_property.grid(row=1, column=0, padx=user.padx, pady=user.pady)
        entry_property = Entry(add_action_window, bd = 3, font=user.standard_font)
        entry_property.grid(row=1, column=1, padx=user.padx, pady=user.pady)

        label_message = Label(add_action_window, text='Message:', font=user.standard_font, bg=user.window_bg_colour)
        label_message.grid(row=2, column=0, padx=user.padx, pady=user.pady)
        entry_message = Entry(add_action_window, bd = 3, font=user.standard_font)
        entry_message.grid(row=2, column=1, padx=user.padx, pady=user.pady)

        button_text = 'SUBMIT (as ' + user.name + ')'
        button = Button(add_action_window, text=button_text, font=user.large_font, bg=user.button_bg_colour, command=lambda: ActionViews.confirm_window(add_action_window, user, entry_property.get(), entry_message.get()))
        button.grid(row=3, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)

    def show_window(root, user, number):     # number is for where a see_window is being auto-launched, otherwise False
        show_actions_window = Toplevel(root)
        show_actions_window.title('Property Python - Show Actions')
        show_actions_window.iconbitmap('icon.ico')
        show_actions_window.configure(bg=user.window_bg_colour)
        show_actions_window.minsize(user.medium_window_width, user.medium_window_height)

        # Auto-launch see_window
        if number != False:
            ActionViews.see_window(root, show_actions_window, user, number)

        top_frame = Frame(show_actions_window, bg=user.window_bg_colour)
        top_frame.pack(side='top', fill='x', expand=0, anchor='n', padx=5, pady=5)
        scroll_frame = VerticalScrolledFrame(show_actions_window, bg=user.window_bg_colour)
        scroll_frame.pack(fill='both', expand=1, padx=10)
        bottom_frame = Frame(show_actions_window, bg=user.window_bg_colour)
        bottom_frame.pack(side='bottom', fill='x', expand=0, anchor='n', padx=5, pady=5)

        title = 'Actions for ' + user.name + ':'
        label_title = Label(top_frame, text=title, font=user.large_font, anchor='w', bg=user.window_bg_colour)
        label_title.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)

        width = int(user.medium_window_width/7)
        counter = 0
        for action in user.actions:
            action_summary = action.date + ' - ' + action.property + ' - ' + action.message
            button_action = Button(scroll_frame.interior, relief='flat', bg="gray99",
                font=user.standard_font, text=action_summary, width=width, anchor='w',
                command=lambda number=counter: ActionViews.see_window(root, show_actions_window, user, number))
            button_action.pack(padx=10, pady=5, side='top', fill='x')
            counter += 1

        add_button = Button(bottom_frame, text='Add Action', font=user.large_font, bg=user.button_bg_colour, command=lambda: ActionViews.add_window(root, user))
        add_button.grid(row=0, column=0, sticky='nsew', padx=user.padx, pady=user.pady)
        close_button = Button(bottom_frame, text='Close Window', font=user.large_font, bg=user.button_bg_colour, command=lambda: show_actions_window.destroy())
        close_button.grid(row=0, column=1, sticky='nsew', padx=user.padx, pady=user.pady)
