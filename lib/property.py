from datetime import date

class Property():
    def __init__(self, user=False, data={}):
        self.code = data.get('code', '')
        self.address = data.get('address', '')
        self.date = str(date.today())
        self.landlords = []

    # Class methods:

    def address_from_code(user, code):
        address = 'Unknown Address'
        for property in user.property_list:
            if property.code == code:
                address = property.address
        return address

    def number_from_code(user, code):
        number = 0
        for property in user.property_list:
            if property.code == code:
                return number
            number += 1
        return False

    # Instance methods:

    def update(self, type, value):
        setattr(self, type, value)

    def add_landlord(self, user, code):
        landlord_code = False
        # keep code if matches a landlord
        for landlord in user.landlord_list:
            if code == landlord.code:
                landlord_code = landlord.code
        # loose code if already added to property
        for code in self.landlords:
            if landlord_code == code:
                landlord_code = False
        if landlord_code != False:
            self.landlords.append(landlord_code)

    def landlord_list(self, user):
        list = ''
        number = 0
        for landlord_code in self.landlords:
            for landlord in user.landlord_list:
                if landlord_code == landlord.code:
                    if number > 0 : list += ', '
                    list += landlord.title + ' ' + landlord.first_names + ' ' + landlord.surname
                    number += 1
        return number, list
