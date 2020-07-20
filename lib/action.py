from datetime import date

class Action():
    def __init__(self, user=False, property='', message=''):
        self.date = str(date.today())
        # For dummy generation without user
        if user == False:
            self.code = ''
        # For non-dummy generation
        else:
            self.code = user.generate_code('action', 7)
        self.property = property
        self.message = message

    def update(self, type, value):
        setattr(self, type, value)
