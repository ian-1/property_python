from datetime import date
import pickle

class Property():
    def __init__(self, code, address):
        self.date = str(date.today())
        self.code = code
        self.address = address

    def update_property(self, type, value):
        if type == 'date': self.date = value
        if type == 'code': self.code = value
        if type == 'address': self.address = value

    def save_properties(user):
        file = '.\\data\\properties\\' + user.name + '.llama'
        with open(file, 'wb') as config_dictionary_file:
            pickle.dump(user.properties, config_dictionary_file)

    def load_properties(user):
        file = '.\\data\\properties\\' + user.name + '.llama'
        with open(file, 'rb') as config_dictionary_file:
            user.properties = pickle.load(config_dictionary_file)