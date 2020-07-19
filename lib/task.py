from datetime import date

class Task():
    def __init__(self, user=False, property='', message=''):
        self.date = str(date.today())
        # For dummy generation without user
        if user == False:
            self.code = ''
        # For non-dummy generation
        else:
            self.code = Task.code(user)
        self.due = str(date.today())
        self.property = property
        self.message = message

    # Class methods:

    def code(user):
        number = len(user.task_list) + 1
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
        post_code += str(number)
        code = 'TASK' + post_code
        return code

    def date_in_days(date_str):
        day = int(date_str[8:10])
        months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        month = int(date_str[5:7])
        day += months[month - 1]
        year = int(date_str[0:4])
        day += year * 365
        return day

    def date_length(start_str, end_str):
        start_in_days = Task.date_in_days(start_str)
        end_in_days = Task.date_in_days(end_str)
        return end_in_days - start_in_days

    # Instance methods:

    def update(self, type, value):
        if type == 'date': self.date = value
        if type == 'due': self.due = value
        if type == 'property': self.property = value
        if type == 'message': self.message = value
