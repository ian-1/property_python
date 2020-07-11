from datetime import date
import pickle

class Contact():
    def __init__(self, user, type, address, note, number):
        self.date = str(date.today())
        self.code = Contact.code(user)
        self.type = type
        self.address = address
        self.note = note
        user.landlords[number].contacts.append(self.code)

    # Class methods:

    def save(user):
        file = '.\\data\\contacts\\' + user.name + '.llama'
        with open(file, 'wb') as config_dictionary_file:
            pickle.dump(user.contacts, config_dictionary_file)

    def load(user):
        file = '.\\data\\contacts\\' + user.name + '.llama'
        with open(file, 'rb') as config_dictionary_file:
            user.contacts = pickle.load(config_dictionary_file)

    def code(user):
        number = len(user.contacts) + 1
        post_code = ''
        if number < 10:
            post_code += '0'
        if number < 100:
            post_code += '0'
        if number < 1000:
            post_code += '0'
        if number < 10000:
            post_code += '0'
        post_code += str(number)
        code = 'PHONE' + post_code
        return code

    # Instance methods:

    def update(self, data_type, value):
        if data_type == 'type': self.type = value
        if data_type == 'address': self.address = value
        if data_type == 'note': self.note = value
