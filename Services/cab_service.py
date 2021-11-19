import math
from Cab_booking.Services.user_service import UserService
from Cab_booking.Services.driver_service import DriverService
from Cab_booking.models.status import Status


class CabService:

    def find_distance(self, start, end):
        return int(math.sqrt((start[0]-end[0])**2 + (start[1]-end[1])**2))


    def find_ride(self, username, source, dest):
        user = UserService().__class__.user_details[username]
        user.set_current_ride((source, dest))
        available_drivers = []
        for driver in DriverService().__class__.all_drivers:
            driver_obj = DriverService().__class__.all_drivers[driver]
            if driver_obj.get_status() == Status.AVAILABLE:
                # import pdb;pdb.set_trace()
                distance = self.find_distance(source, driver_obj.get_location())
                if distance < 5:
                    available_drivers.append(driver_obj)
        if not available_drivers:
            print("No Drivers Found")

        else:
            for available_driver in available_drivers:
                print(available_driver.get_name())

    def choose_ride(self, username, drivername):
        print("Ride Started")

        driver = DriverService().__class__.all_drivers[drivername]
        user = UserService().__class__.user_details[username]
        # import pdb;pdb.set_trace()
        current_ride = user.get_current_ride()
        ride_cost = self.calculate_bill(current_ride[0], current_ride[1])
        user.add_bill_paid(ride_cost)
        driver.add_earning(ride_cost)
        user.set_location(current_ride[1])
        driver.set_location(current_ride[1])


    def calculate_bill(self, source, dest):
        distance = self.find_distance(source, dest)
        return distance

    def total_earnings(self):
        for driver in DriverService().__class__.all_drivers:
            driver_obj = DriverService().__class__.all_drivers[driver]
            print("{0} earn {1}".format(driver_obj.get_name(), driver_obj.get_earning()))
