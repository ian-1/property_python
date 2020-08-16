from datetime import date

class Contact():
    def __init__(self, user=False, data={}):
        self.date = str(date.today())
        # For dummy generation without user
        if user == False:
            self.code = ''
        # For non-dummy generation
        else:
            self.code = user.generate_code('contact', 4)
            user.landlord_list[data.get('number', '')].contacts.append(self.code)
        self.type = data.get('type', '')
        self.address = data.get('enter', '')
        self.note = data.get('note', '')

    def update(self, type, value):
        setattr(self, type, value)
