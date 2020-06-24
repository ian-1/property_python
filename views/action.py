
from tkinter import Toplevel,\
                    Label,\
                    Entry,\
                    Button

class Action:
    # view items used in add action window

    def add_action(window, user, property, message):
        user.add_action(property, message)
        window.destroy()

    def add_window(window, user):
        add_action_window = Toplevel(window)

        lable_property = Label(add_action_window, text='Property:')
        lable_property.pack()
        entry_property = Entry(add_action_window, bd = 5)
        entry_property.pack()

        lable_message = Label(add_action_window, text='Message:')
        lable_message.pack()
        entry_message = Entry(add_action_window, bd = 5)
        entry_message.pack()

        button = Button(add_action_window, text='ADD ACTION', command=lambda: Action.add_action(add_action_window, user, '5 skdhfjksd', 'yweiou ufhuihf sdjk'))
        button.pack()
