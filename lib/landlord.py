from datetime import date

class Landlord():
    def __init__(self, user=False, title='', first_names='', surname='', note=''):
        self.date = str(date.today())
        # For dummy generation without user
        if user == False:
            self.code = ''
        # For non-dummy generation
        else:
            self.code = Landlord.code(user, surname)
        self.title = title
        self.first_names = first_names
        self.surname = surname
        self.contacts = []
        self.note = note

    # Class methods:

    def code(user, surname):
        surname = surname + 'xxxx'
        code = surname[0:4].upper()
        number = 0
        for landlord in user.landlord_list:
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
