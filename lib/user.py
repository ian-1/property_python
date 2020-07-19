from lib.property import Property
from lib.landlord import Landlord
from lib.contact import Contact
from lib.task import Task
from lib.action import Action
import win.property
import win.landlord
import win.contact
import win.task
import win.action

class User():
    def __init__(self, name):
        self.name = name
        self.root = False
        self.property_list = []
        self.property_win = win.property.PropertyWin()
        self.landlord_list = []
        self.landlord_win = win.landlord.LandlordWin()
        self.contact_list = []
        self.contact_win = win.contact.ContactWin()
        self.task_list = []
        self.task_win = win.task.TaskWin()
        self.action_list = []
        self.action_win = win.action.ActionWin()
        # Load in data from files for above
        self.load_group('property')
        self.load_group('landlord')
        self.load_group('contact')
        self.load_group('task')
        self.load_group('action')
        # company attributes:
        self.company_name = 'Property Python'
        self.company_icon = 'icon.ico'
        # style attributes:
        # window sizes:
        self.root_window_width = 950
        self.root_window_height = 150
        self.medium_window_width = 750
        self.medium_window_height = 250
        self.small_window_width = 200
        self.small_window_height = 100
        # colours:
        self.window_bg_colour = 'light goldenrod'
        self.window_bg_colour_alert = 'orange red2'
        self.button_bg_colour = 'pale turquoise'
        # Fonts
        self.standard_font = 'Helvetica 10'
        self.large_font = 'Helvetica 11 bold'
        # Padding
        self.padx = 5
        self.pady = 5

    # Class methods:

    def variables_list(class_name):
        # Build list of [variable_name, is_list?]
        items = []
        dummy = globals()[class_name]()
        for key in vars(dummy).keys():
            item = []
            item.append(key)
            if getattr(dummy, key) == []:
                item.append(True)
            else:
                item.append(False)
            items.append(item)
        return items

    # Instance methods:

    # Should only save whole class for tests/restore etc as will cause data overwrites
    def save_group(self, group):
        print('Warning you are saving a whole class!')
        class_name = group.title()
        items = User.variables_list(class_name)
        for object in getattr(self, group + '_list'):
            for item in items:
                file = open('.\\data\\' + self.name + '\\' + group + '\\' + object.code + '_' + item[0] + '.llama', 'w')
                # Check if an array
                if item[1]:
                    comma = ''
                    for sub_object in getattr(object, item[0]):
                        file.write(comma + sub_object)
                        comma = ','
                # Else is a string
                else:
                    file.write(getattr(object, item[0]))
                file.close()

    def codes_from_data_directory(self, group):
        import os
        codes = []
        for root, dirs, file_names in os.walk('.\\data\\' + self.name + '\\' + group + '\\'):
            # Check how many characters code is
            n = 0
            for character in file_names[0]:
                if character == '_': break
                n += 1
            # Add just code from file name
            for file_name in file_names:
                codes.append(file_name[0:n])
        return list(dict.fromkeys(codes))

    def load_group(self, group):
        # Build ist of [variable_name, is_list?]
        class_name = group.title()
        items = User.variables_list(class_name)
        codes = self.codes_from_data_directory(group)
        object_list = []
        for code in codes:
            variables = []
            for item in items:
                file = open('.\\data\\' + self.name + '\\' + group + '\\' + code + '_' + item[0] + '.llama', 'r')
                variable = file.read()
                if item[1]:
                    variable = variable.split(',')
                file.close()
                variables.append(variable)
            # Set up object (like a dummy object), then add in variables to make object
            object = globals()[class_name]()
            n = 0
            for item in items:
                setattr(object, item[0], variables[n])
                n += 1
            object_list.append(object)
        setattr(self, group + '_list', object_list)

    def add_property(self, code, address):
        self.property_list.append(Property(code, address))

    def add_landlord(self, user, title, first_names, surname, note):
        self.landlord_list.append(Landlord(user, title, first_names, surname, note))

    def add_contact(self, user, type, address, note, number):
        self.contact_list.append(Contact(user, type, address, note, number))

    def add_task(self, user, property, message):
        self.task_list.append(Task(user, property, message))

    def add_action(self, user, property, message):
        self.action_list.append(Action(user, property, message))
