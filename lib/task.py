from datetime import date
import pickle

class Task():
    def __init__(self, property, message):
        self.date = str(date.today())
        self.property = property
        self.message = message

    # Class methods:

    def save(user):
        file = '.\\data\\tasks\\' + user.name + '.llama'
        with open(file, 'wb') as config_dictionary_file:
            pickle.dump(user.tasks, config_dictionary_file)

    def load(user):
        file = '.\\data\\tasks\\' + user.name + '.llama'
        with open(file, 'rb') as config_dictionary_file:
            user.tasks = pickle.load(config_dictionary_file)

    # Instance methods:

    def update(self, type, value):
        if type == 'date': self.date = value
        if type == 'property': self.property = value
        if type == 'message': self.message = value
