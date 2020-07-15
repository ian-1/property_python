from datetime import date
import pickle

class Task():
    def __init__(self, property, message):
        self.date = str(date.today())
        self.due = str(date.today())
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

    def date_in_days(date_str):
        day = int(date_str[9:10])
        months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        month = int(date_str[6:7])
        day += months[month - 1]
        year = int(date_str[0:4])
        day += year * 365
        return day

    def date_length(start_str, end_str):
        start_in_days = Task.date_in_days(start_str)
        end_in_days = Task.date_in_days(end_str)
        return end_in_days - start_in_days

    # Instance methods:

    def update(self, type, value):
        if type == 'date': self.date = value
        if type == 'due': self.due = value
        if type == 'property': self.property = value
        if type == 'message': self.message = value
