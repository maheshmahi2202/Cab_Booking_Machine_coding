from Cab_booking.models.driver import Driver


class DriverService:
    all_drivers = {}

    def add_driver(self, name, gender, age, car_details, loc):
        driver = Driver()
        driver.set_name(name)
        driver.set_gender(gender)
        driver.set_age(age)
        driver.set_car_details(car_details)
        driver.set_location(loc)
        self.__class__.all_drivers[driver.get_name()] = driver
        return driver

    def update_driver_status(self, name, status):
        driver = self.__class__.all_drivers[name]
        driver.set_status(status)