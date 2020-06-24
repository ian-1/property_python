from lib.action import Action

class User():
    def __init__(self, name):
        self.name = name
        self.actions = []

    def add_action(self, property, message):
        self.actions.append(Action(property, message))
