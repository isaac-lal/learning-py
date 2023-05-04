# freeCodeCamp.org: Learn Python - Full Course for Beginners [Tutorial] (4:08:29)

class Student:

    def __init__(self, name, major, gpa): # define a class, then initialize a function with parameters for the class
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False