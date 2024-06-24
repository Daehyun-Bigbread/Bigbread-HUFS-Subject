# subclass system
class ReservationSystem:
    def bookRoom(self, roomType):
        print(f"Booking a {roomType} room")

class CleaningService:
    def cleanRoom(self, roomID):  
        print(f"Scheduling cleaning for room {roomID}")

class DiningService:
    def orderFood(self, roomNumber, foodItem):
        print(f"Ordering {foodItem} for room {roomNumber}")

class CustomerRequests:
    def requestItem(self, roomNumber, item):
        print(f"Requesting {item} for room {roomNumber}")

# facace class
class HotelFacade:
    def __init__(self):
        self.reservation = ReservationSystem()
        self.cleaning = CleaningService()
        self.dining = DiningService()
        self.requests = CustomerRequests()

    def bookRoom(self, roomType):
        self.reservation.bookRoom(roomType)

    def cleanRoom(self, roomID):
        self.cleaning.cleanRoom(roomID)

    def orderFood(self, roomNumber, foodItem):
        self.dining.orderFood(roomNumber, foodItem)

    def requestItem(self, roomNumber, item):
        self.requests.requestItem(roomNumber, item)

hotelFacade = HotelFacade()
hotelFacade.bookRoom("Deluxe")
hotelFacade.cleanRoom(101)
hotelFacade.orderFood(101, "Pizza")
hotelFacade.requestItem(101, "Extra Pillow")
