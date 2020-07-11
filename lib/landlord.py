from datetime import date
import pickle

class Landlord():
    def __init__(self, user, title, first_names, surname, note):
        self.date = str(date.today())
        self.code = Landlord.code(user, surname)
        self.title = title
        self.first_names = first_names
        self.surname = surname
        self.contacts = []
        self.note = note

    # Class methods:

    def save(user):
        file = '.\\data\\landlords\\' + user.name + '.llama'
        with open(file, 'wb') as config_dictionary_file:
            pickle.dump(user.landlords, config_dictionary_file)

    def load(user):
        file = '.\\data\\landlords\\' + user.name + '.llama'
        with open(file, 'rb') as config_dictionary_file:
            user.landlords = pickle.load(config_dictionary_file)

    def code(user, surname):
        surname = surname + 'xxxx'
        code = surname[0:4].upper()
        number = 0
        for landlord in user.landlords:
            if code == landlord.code[0:4]:
                number += 1
        post_code = ''
        if number < 10:
            post_code += '0'
        if number < 100:
            post_code += '0'
        post_code += str(number)
        code += post_code
        return code

    # Instance methods:

    def update(self, type, value):
        if type == 'date': self.date = value
        if type == 'title': self.title = value
        if type == 'first_names': self.first_names = value
        if type == 'surname': self.surname = value
        if type == 'note': self.note = value
