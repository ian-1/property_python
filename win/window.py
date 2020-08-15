import win.widget as Widget

def add_window(user, class_type, number=''):
    # Set up window
    text = 'Add ' + class_type.title()
    window = Widget.window(user.root, user, text, 'small')
    row = 0

    # Intro
    text = 'Add ' + class_type + ' as ' + user.name
    Widget.title(window, user, text)
    row += 1
    entries = {'number': number}

    # Drop downs
    if class_type == 'action' or class_type == 'task':
        options = []
        for property in user.property_list:
            text = property.code + ' - ' + property.address
            options.append(text)
        entry_property = Widget.drop_down(window, user, 'Property:', options, row)
        entries.update({'property': entry_property})
        row += 1

    if class_type == 'contact':
        entry_type = Widget.drop_down(window, user, 'Type:', ['Address', 'Phone Number', 'Email'], row)
        entries.update({'type': entry_type})
        row += 1

    # Non drop downs
    data_types = ['message'] # Action & Task
    if class_type == 'property': data_types = ['code', 'address']
    if class_type == 'landlord': data_types = ['title', 'first_names', 'surname', 'note']
    if class_type == 'contact': data_types = ['enter', 'note']

    for data_type in data_types:
        text = data_type.title() + ':'
        if data_type == 'first_names': text = 'First name(s):'
        if data_type == 'note': text = 'Note (optional):'
        entry = Widget.entry(window, user, text, row)
        entries.update({data_type: entry})
        row += 1

    # Submit
    text = 'SUBMIT (as ' + user.name + ')'
    Widget.confirm_window_button(window, user, class_type, text, entries, row)
    Widget.close_button(window, False, window, user, False, row, 2)

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
