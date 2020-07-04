from datetime import date
import pickle

class Landlord():
    def __init__(self, property, message):
        self.date = str(date.today())
        self.property = property
        self.message = message

    # Class methods:

    def save_landlords(user):
        file = '.\\data\\landlords\\' + user.name + '.llama'
        with open(file, 'wb') as config_dictionary_file:
            pickle.dump(user.landlords, config_dictionary_file)

    def load_landlords(user):
        file = '.\\data\\landlords\\' + user.name + '.llama'
        with open(file, 'rb') as config_dictionary_file:
            user.landlords = pickle.load(config_dictionary_file)

    # Instance methods:

    def update_landlord(self, type, value):
        if type == 'date': self.date = value
        if type == 'property': self.property = value
        if type == 'message': self.message = value
