from Cab_booking.models.status import Status


class Driver:
    def __init__(self):
        self.name = None
        self.gender = None
        self.age = None
        self.car_details = None
        self.location = None
        self.status = Status.UN_AVAILABLE
        self.earning = 0

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

    def set_car_details(self, car_details):
        self.car_details = car_details

    def get_car_details(self):
        return self.car_details

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def add_earning(self, amount):
        self.earning += amount

    def get_earning(self):
        return self.earning
