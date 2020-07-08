from lib.action import Action
from lib.property import Property
from lib.landlord import Landlord
import win.action
import win.property
import win.landlord

class User():
    def __init__(self, name):
        self.name = name
        self.root = False
        self.actions = []
        self.action_win = win.action.ActionWin()
        self.properties = []
        self.property_win = win.property.PropertyWin()
        self.landlords = []
        self.landlord_win = win.landlord.LandlordWin()
        # Load in data from files for above
        Action.load_actions(self)
        Property.load_properties(self)
        Landlord.load_landlords(self)
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

    def add_action(self, property, message):
        self.actions.append(Action(property, message))

    def add_property(self, code, address):
        self.properties.append(Property(code, address))

    def add_landlord(self, user, title, first_names, surname, note):
        self.landlords.append(Landlord(user, title, first_names, surname, note))
