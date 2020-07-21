from datetime import date

class Contact():
    def __init__(self, user=False, type='', address='', note='', number=''):
        self.date = str(date.today())
        # For dummy generation without user
        if user == False:
            self.code = ''
        # For non-dummy generation
        else:
            self.code = user.generate_code('contact', 4)
            user.landlord_list[number].contacts.append(self.code)
        self.type = type
        self.address = address
        self.note = note

    def update(self, type, value):
        setattr(self, type, value)
