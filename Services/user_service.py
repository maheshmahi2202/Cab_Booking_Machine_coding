from Cab_booking.models.users import User


class UserService:
    user_details = {}

    def add_user(self, name, gender, age):
        user = User()
        user.set_name(name)
        user.set_gender(gender)
        user.set_age(age)
        self.__class__.user_details[user.get_name()] = user
        return user

    def update_user_location(self, name, loc):
        user = self.__class__.user_details[name]
        user.set_location(loc)




