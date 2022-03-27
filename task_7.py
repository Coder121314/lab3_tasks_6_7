"""
module ccontains elements
for working with logistics system
"""


class Item:
    """
    class for items transported
    """

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self) -> str:
        """
        redefining str method
        """
        return f"The order {self.name} costs {self.price}"


class Vehicle:
    """
    class for vehicles transporting items
    """

    def __init__(self, vehicleNo: int, isAvailable: bool = True):
        self.vehicleNo = vehicleNo
        self.isAvailable = isAvailable


class Location:
    """
    class presenting location
    """

    def __init__(self, city: str, postoffice: int):
        self.city = city
        self.postoffice = postoffice


class Order:
    """
    class for customer orders
    """

    def __init__(
        self,
        user_name: str,
        city: str,
        postoffice: int,
        items: list,
        vehicle: None = None,
        orderId: int = None,
        location: Location = None,
    ):
        self.orderId = orderId or id(self)
        self.user_name = user_name
        self.location = location if location else Location(city, postoffice)
        self.items = items
        self.vehicle = vehicle
        self.city = city
        self.postoffice = postoffice
        print(self)

    def calculate_Amount(self) -> int:
        """
        method calculates the price of order
        """
        total = 0
        for elem in self.items:
            total += elem.price
        return total

    def assignVehicle(self, vehicle: Vehicle):
        """
        method assign vehicle
        for the order
        """
        self.vehicle = vehicle

    def __str__(self) -> str:
        """
        redefining str method
        """
        return f"Your order number is {id(self)}."


class LogisticSystem:
    """
    class that represents
    the logistics system
    """

    def __init__(self, vehicles: list, orders: list = None, id_dict: dict = None):
        self.orders = orders or []
        self.vehicles = [vehicle for vehicle in vehicles if vehicle.isAvailable is True]
        self.id_dict = id_dict or dict()
        for elem in self.orders:
            self.id_dict[elem.orderId] = True

    def enable_vehicle(self, vehicleId):
        """
        enable the vehicle
        for transporting orders
        """
        for vehicle in self.vehicles:
            if vehicleId == id(vehicle):
                vehicle.isAvailable = True

    def placeOrder(self, order: Order):
        """
        method places
        an order
        """
        self.orders.append(order)
        if (
            len([vehicle for vehicle in self.vehicles if vehicle.isAvailable is True])
            == 0
        ):  # no vehicles available
            print("There is no available vehicle to deliver an order.")
            return
        else:
            # check if the order has a defined vehicle
            # check if there is such a vehicle
            # if no, write so
            # if yes, assign this vehicle to the order

            # if the order doesn't have a defined vehicle,
            # assign the first in the list
            found = False
            if order.vehicle:
                for veh in self.vehicles:
                    if veh.vehicleNo == order.vehicle:
                        the_veh = veh
                        found = True
                if found is False:
                    print("There is no such vehicle to deliver an order.")
                    return
                else:
                    the_veh_idx = self.vehicles.index(the_veh)
                    del self.vehicles[the_veh_idx]  # it is already assigned here
            else:
                for idx, vehic in enumerate(self.vehicles):
                    if vehic.isAvailable is True:
                        order.assignVehicle(vehic)
                        del self.vehicles[idx]
                        break

            self.id_dict[order.orderId] = True

    def trackOrder(self, orderId: int) -> str:
        """
        method tracks order
        by id
        """
        import ctypes

        if orderId not in self.id_dict:
            print("No such order.")
            return
        obj = ctypes.cast(
            orderId, ctypes.py_object
        ).value  # access the Order object by id
        print(
            f"Your order #{orderId} is sent to {obj.city}. Total price: {obj.calculate_Amount()} UAH."
        )
        return f"Your order #{orderId} is sent to {obj.city}. Total price: {obj.calculate_Amount()} UAH."


def default_test():
    """
    default task test
    """
    vehicles = [Vehicle(1), Vehicle(2)]
    logSystem = LogisticSystem(vehicles)
    my_items = [Item("book", 110), Item("chupachups", 44)]
    my_order = Order(user_name="Oleg", city="Lviv", postoffice=53, items=my_items)
    curr_id = my_order.orderId
    # Your order number is 165488695(some id).

    logSystem.placeOrder(my_order)
    logSystem.trackOrder(curr_id)
    # # Your order #165488695(some id) is sent to Lviv. Total price: 154 UAH.

    my_items2 = [Item("flowers", 11), Item("shoes", 153), Item("helicopter", 0.33)]
    my_order2 = Order("Andrii", "Odessa", 3, my_items2)
    # Your order number is 234976475(some id).
    curr_id_2 = my_order2.orderId
    logSystem.placeOrder(my_order2)
    logSystem.trackOrder(curr_id_2)
    # Your order #234976475(some id) is sent to Odessa. Total price: 164.33 UAH.

    my_items3 = [Item("coat", 61.8), Item("shower", 5070), Item("rollers", 700)]
    my_order3 = Order("Olesya", "Kharkiv", 17, my_items3)
    # Your order number is 485932990(some id).
    logSystem.placeOrder(my_order3)
    # There is no available vehicle to deliver an order.
    logSystem.trackOrder(485932990)
    # No such order.
    print("...Successfully sent all possible orders")
    print()


def additional_test():
    """
    additional test showing
    the functionality of classes
    """
    vehicles = [Vehicle(34, False), Vehicle(11), Vehicle(9, True)]
    items = [Item("item 1", 61), Item("item 2", 50), Item("item 3", 3)]
    the_order = Order("person 1", "Kharkiv", 96, items)
    log_system = LogisticSystem(vehicles, [the_order])
    log_system.placeOrder(the_order)
    other_items = [Item("item 1", 303), Item("item 2", 59), Item("item 3", 6)]
    order_1 = Order(user_name="Maria", city="Kyiv", postoffice=3, items=other_items)
    curr_id = order_1.orderId
    # Your order number is 165488695(some id).

    log_system.placeOrder(order_1)
    log_system.trackOrder(curr_id)
    log_system.trackOrder(log_system.orders[0].orderId)

    extra_order = Order(
        user_name="Marta", city="Ternopli", postoffice=7, items=other_items
    )
    log_system.placeOrder(extra_order)
    wrong_order = 1234
    log_system.trackOrder(wrong_order)


if __name__ == "__main__":
    default_test()
    additional_test()
