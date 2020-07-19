from datetime import date

class Action():
    def __init__(self, user=False, property='', message=''):
        self.date = str(date.today())
        # For dummy generation without user
        if user == False:
            self.code = ''
        # For non-dummy generation
        else:
            self.code = Action.code(user)
        self.property = property
        self.message = message

    # Class methods:

    def code(user):
        number = len(user.action_list) + 1
        post_code = ''
        if number < 10:
            post_code += '0'
        if number < 100:
            post_code += '0'
        if number < 1000:
            post_code += '0'
        if number < 10000:
            post_code += '0'
        if number < 100000:
            post_code += '0'
        if number < 1000000:
            post_code += '0'
        if number < 10000000:
            post_code += '0'
        post_code += str(number)
        code = 'ACTION' + post_code
        return code

    # Instance methods:

    def update(self, type, value):
        if type == 'date': self.date = value
        if type == 'property': self.property = value
        if type == 'message': self.message = value
