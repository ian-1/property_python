from datetime import date
import pickle

class Property():
    def __init__(self, code, address):
        self.date = str(date.today())
        self.code = code
        self.address = address
        self.landlords = []

    # Class methods:

    def save_properties(user):
        file = '.\\data\\properties\\' + user.name + '.llama'
        with open(file, 'wb') as config_dictionary_file:
            pickle.dump(user.properties, config_dictionary_file)

    def load_properties(user):
        file = '.\\data\\properties\\' + user.name + '.llama'
        with open(file, 'rb') as config_dictionary_file:
            user.properties = pickle.load(config_dictionary_file)

    def address_from_code(user, code):
        address = 'Unknown Address'
        for property in user.properties:
            if property.code == code:
                address = property.address
        return address

    def number_from_code(user, code):
        number = 0
        for property in user.properties:
            if property.code == code:
                return number
            number += 1
        return False

    # Instance methods:

    def update_property(self, type, value):
        if type == 'date': self.date = value
        if type == 'code': self.code = value
        if type == 'address': self.address = value

    def add_landlord(self, user, code):
        landlord_code = False
        # save code if matches a landlord
        for landlord in user.landlords:
            if code == landlord.code:
                landlord_code = landlord.code
        # wipe code if already added to property
        for code in self.landlords:
            if landlord_code == code:
                landlord_code = False
        if landlord_code != False:
            self.landlords.append(landlord_code)

    def landlord_list(self, user):
        list = ''
        number = 0
        for landlord_code in self.landlords:
            for landlord in user.landlords:
                if landlord_code == landlord.code:
                    if number > 0 : list += ', '
                    list += landlord.title + ' ' + landlord.first_names + ' ' + landlord.surname
                    number += 1
        return number, list
