
from tkinter import Toplevel,\
                    Label,\
                    Entry,\
                    Button
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

        action_summary = property + ' - ' + message

        lable_property = Label(confirm_action_window, text=action_summary)
        lable_property.pack()

        button_text = 'CONFIRM (as ' + user.name + ')'
        button = Button(confirm_action_window, text=button_text, command=lambda: ActionViews.add_action(window, confirm_action_window, user, property, message))
        button.pack()
        cancel_button = Button(confirm_action_window, text="cancel (don't confirm)", command=lambda: confirm_action_window.destroy())
        cancel_button.pack()

    def add_window(window, user):
        add_action_window = Toplevel(window)

        title = 'Add action as ' + user.name
        lable_title = Label(add_action_window, text=title)
        lable_title.pack()

        lable_property = Label(add_action_window, text='Property:')
        lable_property.pack()
        entry_property = Entry(add_action_window, bd = 3)
        entry_property.pack()

        lable_message = Label(add_action_window, text='Message:')
        lable_message.pack()
        entry_message = Entry(add_action_window, bd = 3)
        entry_message.pack()

        button_text = 'SUBMIT (as ' + user.name + ')'
        button = Button(add_action_window, text=button_text, command=lambda: ActionViews.confirm_window(add_action_window, user, entry_property.get(), entry_message.get()))
        button.pack()

    def show_window(window, user):
        show_actions_window = Toplevel(window)

        title = 'Actions for ' + user.name + ':'
        lable_title = Label(show_actions_window, text=title)
        lable_title.pack()

        for action in user.actions:
            action_summary = action.date + ' - ' + action.property + ' - ' + action.message
            lable_action = Label(show_actions_window, text=action_summary)
            lable_action.pack()

        add_button = Button(show_actions_window, text='add action', command=lambda: ActionViews.add_window(window, user))
        add_button.pack()

        close_button = Button(show_actions_window, text='close window', command=lambda: show_actions_window.destroy())
        close_button.pack()
