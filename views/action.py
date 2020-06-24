
from tkinter import Toplevel,\
                    Label,\
                    Entry,\
                    Button,\
                    PhotoImage
from lib.action import Action

class ActionViews:
    # view items used in add action window

    def add_action(window, confirm_window, user, property, message):
        user.add_action(property, message)
        confirm_window.destroy()
        window.destroy()
        Action.save_actions(user)


    def confirm_window(window, user, property, message):
        confirm_action_window = Toplevel(window)
        confirm_action_window.title('Property Python - Confirm Action')
        confirm_action_window.iconbitmap('icon.ico')
        confirm_action_window.configure(bg=user.window_bg_colour)
        confirm_action_window.minsize(user.small_window_width, user.small_window_height)

        lable_title = Label(confirm_action_window, text='Check and confirm action:', font=user.large_font, anchor='w', bg=user.window_bg_colour)
        lable_title.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)


        action_summary = property + ' - ' + message
        lable_property = Label(confirm_action_window, text=action_summary, font=user.standard_font, bg=user.window_bg_colour)
        lable_property.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)

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
        lable_title = Label(add_action_window, text=title, font=user.large_font, anchor='w', bg=user.window_bg_colour)
        lable_title.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)

        lable_property = Label(add_action_window, text='Property:', font=user.standard_font, bg=user.window_bg_colour)
        lable_property.grid(row=1, column=0, padx=user.padx, pady=user.pady)
        entry_property = Entry(add_action_window, bd = 3, font=user.standard_font)
        entry_property.grid(row=1, column=1, padx=user.padx, pady=user.pady)

        lable_message = Label(add_action_window, text='Message:', font=user.standard_font, bg=user.window_bg_colour)
        lable_message.grid(row=2, column=0, padx=user.padx, pady=user.pady)
        entry_message = Entry(add_action_window, bd = 3, font=user.standard_font)
        entry_message.grid(row=2, column=1, padx=user.padx, pady=user.pady)

        button_text = 'SUBMIT (as ' + user.name + ')'
        button = Button(add_action_window, text=button_text, font=user.large_font, bg=user.button_bg_colour, command=lambda: ActionViews.confirm_window(add_action_window, user, entry_property.get(), entry_message.get()))
        button.grid(row=3, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)

    def show_window(window, user):
        show_actions_window = Toplevel(window)
        show_actions_window.title('Property Python - Show Actions')
        show_actions_window.iconbitmap('icon.ico')
        show_actions_window.configure(bg=user.window_bg_colour)
        show_actions_window.minsize(user.medium_window_width, user.medium_window_height)


        title = 'Actions for ' + user.name + ':'
        lable_title = Label(show_actions_window, text=title, font=user.large_font, anchor='w', bg=user.window_bg_colour)
        lable_title.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=user.padx, pady=user.pady)

        row = 1
        width = int(user.medium_window_width/4)
        for action in user.actions:
            action_summary = action.date + ' - ' + action.property + ' - ' + action.message
            button_action = Button(show_actions_window, text=action_summary[:width], font=user.standard_font, anchor='w')
            button_action.grid(row=row, column=0, columnspan=2, sticky='nsew', padx=user.padx)
            row += 1

        add_button = Button(show_actions_window, text='Add Action', font=user.large_font, bg=user.button_bg_colour, command=lambda: ActionViews.add_window(window, user))
        add_button.grid(row=row, column=0, sticky='nsew', padx=user.padx, pady=user.pady)
        close_button = Button(show_actions_window, text='Close Window', font=user.large_font, bg=user.button_bg_colour, command=lambda: show_actions_window.destroy())
        close_button.grid(row=row, column=1, sticky='nsew', padx=user.padx, pady=user.pady)
