
from tkinter import Toplevel,\
                    Label,\
                    Entry,\
                    Button

class Action:
    # view items used in add action window

    def add_action(window, confirm_window, user, property, message):
        user.add_action(property, message)
        confirm_window.destroy()
        window.destroy()

    def confirm_window(window, user, property, message):
        confirm_action_window = Toplevel(window)

        action_summary = property + ' - ' + message

        lable_property = Label(confirm_action_window, text=action_summary)
        lable_property.pack()

        button = Button(confirm_action_window, text='CONFIRM ADD ACTION', command=lambda: Action.add_action(window, confirm_action_window, user, property, message))
        button.pack()
        cancel_button = Button(confirm_action_window, text="cancel (don't confirm)", command=lambda: confirm_action_window.destroy())
        cancel_button.pack()

    def add_window(window, user):
        add_action_window = Toplevel(window)

        lable_property = Label(add_action_window, text='Property:')
        lable_property.pack()
        entry_property = Entry(add_action_window, bd = 3)
        entry_property.pack()

        lable_message = Label(add_action_window, text='Message:')
        lable_message.pack()
        entry_message = Entry(add_action_window, bd = 3)
        entry_message.pack()

        button = Button(add_action_window, text='ADD ACTION', command=lambda: Action.confirm_window(add_action_window, user, entry_property.get(), entry_message.get()))
        button.pack()
