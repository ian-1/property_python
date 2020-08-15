from datetime import date

class Landlord():
    def __init__(self, user=False, data={}):
        self.date = str(date.today())
        # For dummy generation without user
        if user == False:
            self.code = ''
        # For non-dummy generation
        else:
            self.code = user.generate_code('landlord', 3)
        self.title = data.get('title', '')
        self.first_names = data.get('first_names', '')
        self.surname = data.get('surname', '')
        self.note = data.get('note', '')
        self.contacts = []

    def update(self, type, value):
        setattr(self, type, value)
