from Cab_booking.Services.user_service import UserService
from Cab_booking.Services.driver_service import DriverService
from Cab_booking.Services.cab_service import CabService
from Cab_booking.models.status import Status

UserService().add_user("Abhishek", "M", 23)
UserService().update_user_location("Abhishek", (0,0))
UserService().add_user("Rahul", "M", 23)
UserService().update_user_location("Abhishek", (10,0))
UserService().add_user("Nandu", "F", 23)
UserService().update_user_location("Abhishek", (15, 6))

DriverService().add_driver("Driver1", "M", 34, "Swift, KA-01-P-1234", (10,1))
DriverService().update_driver_status("Driver1", Status.AVAILABLE)
DriverService().add_driver("Driver2", "M", 34, "Swift, KA-01-P-1234", (11,10))
DriverService().update_driver_status("Driver2", Status.AVAILABLE)
DriverService().add_driver("Driver3", "M", 34, "Swift, KA-01-P-1234", (5,3))
DriverService().update_driver_status("Driver3", Status.AVAILABLE)

CabService().find_ride("Abhishek", (0,0), (20,1))
CabService().find_ride("Rahul", (10,0), (15,3))
CabService().choose_ride("Rahul", "Driver1")

DriverService().update_driver_status("Driver1", Status.UN_AVAILABLE)
CabService().find_ride("Nandu", (15,6), (20,4))

CabService().total_earnings()

