from datetime import date
import pickle
import os

items = ['code',
         'address',
         'date',
         'landlords']

class Property():
    def __init__(self, code, address, date=str(date.today()), landlords=[]):
        self.code = code
        self.address = address
        self.date = date
        self.landlords = landlords
        self.items = [['code', self.code],
                      ['address', self.address],
                      ['date', self.date],
                      ['landlords', self.landlords]]

    # Class methods:

    def save(user):
        #file = '.\\data\\properties\\' + user.name + '.llama'
        #with open(file, 'wb') as config_dictionary_file:
        #    pickle.dump(user.properties, config_dictionary_file)

        for property in user.properties:
            for item in property.items:
                file = open('.\\data\\' + user.name + '\\properties\\' + property.code + '_' + item[0] + '.llama', 'w')
                if item[0] == 'landlords':
                    comma = ''
                    for landlord in item[1]:
                        file.write(comma + landlord)
                        comma = ','
                else:
                    file.write(item[1])
                file.close()

    def load(user):
        # file = '.\\data\\properties\\' + user.name + '.llama'
        # with open(file, 'rb') as config_dictionary_file:
        #     user.properties = pickle.load(config_dictionary_file)

        properties = []
        for root, dirs, files in os.walk('.\\data\\' + user.name + '\\properties\\'):
            for filename in files:
                properties.append(filename[0:6])
        properties = list(dict.fromkeys(properties))
        for property in properties:
            objects = []
            for item in items:
                file = open('.\\data\\' + user.name + '\\properties\\' + property + '_' + item + '.llama', 'r')
                object = file.read()
                if item == 'landlords':
                    object = object.split(',')
                file.close()
                objects.append(object)
            user.properties.append(Property(objects[0], objects[1], objects[2], objects[3]))

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

    def update(self, type, value):
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
