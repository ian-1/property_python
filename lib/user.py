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
        self.properties = []
        self.property_win = win.property.PropertyWin()
        self.landlords = []
        self.landlord_win = win.landlord.LandlordWin()
        self.contacts = []
        self.contact_win = win.contact.ContactWin()
        self.tasks = []
        self.task_win = win.task.TaskWin()
        self.actions = []
        self.action_win = win.action.ActionWin()
        # Load in data from files for above
        Action.load(self)
        Property.load(self)
        Landlord.load(self)
        Contact.load(self)
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

    def add_property(self, code, address):
        self.properties.append(Property(code, address))

    def add_landlord(self, user, title, first_names, surname, note):
        self.landlords.append(Landlord(user, title, first_names, surname, note))

    def add_contact(self, user, type, address, note, number):
        self.contacts.append(Contact(user, type, address, note, number))

    def add_task(self, property, message):
        self.tasks.append(Task(property, message))

    def add_action(self, property, message):
        self.actions.append(Action(property, message))
