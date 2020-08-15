import win.widget as Widget

def show_window(user, class_type, code=False): # code for where actions for just one property are requested, otherwise False
    # Set up window
    text = 'Show ' + class_type.title() + 's'
    if class_type == 'property': text = 'Show Properties'
    window = Widget.window(user.root, user, text, 'medium')

    # Set up frames
    top_frame = Widget.side_frame(window, user, 'top')
    scroll_frame = Widget.scroll_frame(window, user)
    bottom_frame = Widget.side_frame(window, user, 'bottom')

    # Top Frame
    text = class_type.title() + 's for ' + user.name + ':'
    if class_type == 'property': text = 'Properties for ' + user.name + ':'
    Widget.title(top_frame, user, text)

    # Scroll Frame
    Widget.scroll_button_list(window, scroll_frame, user, class_type, code)

    # Bottom Frame
    Widget.add_window_button(bottom_frame, user, class_type)
    Widget.close_button(window, 'show', bottom_frame, user, class_type)

    # Add window and scroll frame to user so can be refreshed from outside of method
    show_windows = getattr(user, class_type + '_show_windows')
    show_windows.insert(0, [window, scroll_frame, code])
    # Close window sent through method so can be removed from user
    window.protocol("WM_DELETE_WINDOW", lambda: Widget.close_window(window, 'show', user, class_type))
