class User:
    def __init__(self):
        self.name = None
        self.gender = None
        self.age = None
        self.location = None
        self.total_bill_paid = 0
        self.current_ride = None

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_gender(self, gender):
        self.gender = gender

    def get_gender(self):
        return self.gender

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def add_bill_paid(self, amount):
        self.total_bill_paid += amount

    def get_total_bill_paid(self):
        return self.total_bill_paid

    def set_current_ride(self, current_ride):
        self.current_ride = current_ride

    def get_current_ride(self):
        return self.current_ride

