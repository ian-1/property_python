from datetime import date

class Action():
    def __init__(self, property, message):
        self.date = date.today()
        self.property = property
        self.message = message
