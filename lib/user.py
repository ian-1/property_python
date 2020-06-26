from lib.action import Action
from lib.property import Property

class User():
    def __init__(self, name):
        self.name = name
        self.actions = []
        self.properties = []
        # Load in data from files for above
        Action.load_actions(self)
        Property.load_properties(self)
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
