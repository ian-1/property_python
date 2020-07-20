from datetime import date

class Landlord():
    def __init__(self, user=False, title='', first_names='', surname='', note=''):
        self.date = str(date.today())
        # For dummy generation without user
        if user == False:
            self.code = ''
        # For non-dummy generation
        else:
            self.code = user.generate_code('landlord', 3)
        self.title = title
        self.first_names = first_names
        self.surname = surname
        self.contacts = []
        self.note = note

    def update(self, type, value):
        setattr(self, type, value)
