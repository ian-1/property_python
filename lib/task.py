from datetime import date

class Task():
    def __init__(self, user=False, data={}):
        self.date = str(date.today())
        # For dummy generation without user
        if user == False:
            self.code = ''
        # For non-dummy generation
        else:
            self.code = user.generate_code('task', 6)
        self.active = True
        self.staff = ''
        self.due = str(date.today())
        self.deadline = ''
        self.property = data.get('property_code', '')
        self.message = data.get('message', '')
        self.next = ''

    # Class methods:

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
        setattr(self, type, value)
