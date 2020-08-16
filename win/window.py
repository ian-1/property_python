import win.widget as Widget
from lib.property import Property

def confirm_window(add_window, user, class_type, entries):
    # Set up window
    alert = False
    if class_type == 'property': alert = True
    text = 'Confirm ' + class_type.title()
    window =  Widget.window(add_window, user, text, 'small', alert)
    row = 0
    column = 0

    # Get data from entries dictionary
    data = {}
    number = entries.get('number', '')
    data.update({'number': number})

    data_types = ['message', 'code', 'address', 'title', 'first_names', 'surname', 'note', 'type', 'enter']
    for data_type in data_types:
        data_item = entries.get(data_type, Widget.blank_entry()).get()
        data.update({data_type: data_item})

    if class_type == 'action' or class_type == 'task':
        # Retrieve address from dropdown list
        property_code_address = entries.get('property', Widget.blank_entry()).get()
        property_code = property_code_address[0:6]
        data.update({'property_code': property_code})
        address = Property.address_from_code(user, property_code)
        data.update({'address': address})

    # Intro line
    text = 'Check and confirm ' + class_type + ':'
    if class_type == 'property': text = 'ARE YOU SURE YOU WANT TO ADD PROPERTY?'
    Widget.line(window, user, text, row, column, alert)
    row += 1

    # Main data display: property (code)
    if data['code'] != '':
        text = 'Code: ' + data['code']
        Widget.title(window, user, text, row, column, alert)
        row += 1
    elif class_type == 'property':
        text = 'NO PROPERTY CODE ADDED'
        Widget.title(window, user, text, row, column, alert)
        row += 1

    # Main data display: property, action & task (address)
    if data['address'] != '':
        text = 'Property: '
        if class_type == 'property': text = 'Address: '
        text += data['address']
        Widget.title(window, user, text, row, column, alert)
        row += 1
    elif class_type == 'property':
        text = 'NO ADDRESS ADDED'
        Widget.title(window, user, text, row, column, alert)
        row += 1

    # Main data: action & task (message) - if exists displayed below in sub-data
    if data['message'] == '':
        if class_type == 'action' or class_type == 'task':
            text = 'NO MESSAGE ADDED'
            Widget.title(window, user, text, row, column, alert)
            row += 1

    # Main data display: landlord (full name)
    if data['surname'] != '':
        text = data['title'] + ' ' + data['first_names'] + ' ' + data['surname']
        Widget.title(window, user, text, row, column, alert)
        row += 1
    elif class_type == 'landlord':
        text = 'NO SURNAME ADDED'
        Widget.title(window, user, text, row, column, alert)
        row += 1

    # Main data display: contact (email/phone/address)
    if data['type'] != '':
        text = data['type'] + ': ' + data['enter']
        Widget.title(window, user, text, row, column, alert)
        row += 1
    elif class_type == 'contact':
        text = 'NO TYPE SELECTED'
        Widget.title(window, user, text, row, column, alert)
        row += 1

    # Sub-data display
    data_types = ['message', 'note'] # Action & Task
    for data_type in data_types:
        if data[data_type] != '':
            text = data[data_type]
            Widget.content(window, user, text, row, column, alert)
            row += 1

    # Open the new objects's see window after adding
    open = False
    if class_type == 'property': open = True

    # Submit
    text = 'CONFIRM (as ' + user.name + ')'
    Widget.add_button(add_window, window, user, class_type, text, data, row, open)
    text = "Cancel (don't confirm)"
    Widget.close_button(window, False, window, user, False, row, 1, text)

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
