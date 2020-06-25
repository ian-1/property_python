from datetime import date
import pickle

class Property():
    def __init__(self, action, message):
        self.date = str(date.today())
        self.action = action
        self.message = message

    def update_property(self, type, value):
        if type == 'date': self.date = value
        if type == 'action': self.action = value
        if type == 'message': self.message = value

    def save_properties(user):
        file = '.\\data\\properties\\' + user.name + '.llama'
        with open(file, 'wb') as config_dictionary_file:
            pickle.dump(user.properties, config_dictionary_file)

    def load_properties(user):
        file = '.\\data\\properties\\' + user.name + '.llama'
        with open(file, 'rb') as config_dictionary_file:
            user.properties = pickle.load(config_dictionary_file)
