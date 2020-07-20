from datetime import date
import pickle

class Contact():
    def __init__(self, user=False, type='', address='', note='', number=''):
        self.date = str(date.today())
        # For dummy generation without user
        if user == False:
            self.code = ''
        # For non-dummy generation
        else:
            self.code = Contact.code(user)
            user.landlord_list[number].contacts.append(self.code)
        self.type = type
        self.address = address
        self.note = note

    # Class methods:

    def code(user):
        number = len(user.contact_list) + 1
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
        setattr(self, type, value)
