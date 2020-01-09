# Taxi Booking System
from abc import ABC, abstractmethod
from random import randrange
from typing import List


"""
------------------------------------------------------------------------------
FACTORY PATTERN FOR DIFFERENT TYPES OF USERS (DRIVER, CUSTOMER AND OPERATOR)
------------------------------------------------------------------------------
"""


class Creator(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a User class. The Creator's subclasses usually provide the
    implementation of this method.
    """

    @abstractmethod
    def factory_method(self):
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        pass

    def some_operation(self) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating users. Usually, it contains some core business logic
        that relies on User objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of user from it.
        """

        # Call the factory method to create a User object.
        user = self.factory_method()

        # Now, use the user.
        result = f"Creator: The same creator's code has just worked with {user.operation()}"

        return result


"""
Concrete Creators override the factory method in order to change the resulting
user's type.
"""


class DriverCreator(Creator):
    """
    Note that the signature of the method still uses the abstract user type,
    even though the concrete user is actually returned from the method. This
    way the Creator can stay independent of concrete user classes.
    """

    def factory_method(self):
        return Driver()


class CustomerCreator(Creator):
    def factory_method(self):
        return Customer()


class OperatorCreator(Creator):
    def factory_method(self):
        return Operator()


class User(ABC):
    """
    The User interface declares the operations that all concrete users
    must implement.
    """

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def set_id(self, new_id):
        self.id = new_id

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    @abstractmethod
    def operation(self) -> str:
        pass


"""
Concrete Users provide various implementations of the User interface.
"""


class Driver(User):

    def __init__(self, driver_id, driver_name, car_id, admin_id):
        super().__init__(driver_id, driver_name)
        self.car_id = car_id
        self.admin_id = admin_id

    def operation(self) -> str:
        return "{Result of the Driver}"

    def view_customer_details(self):
        pass

    def view_location(self):
        pass

    def view_prev_trips(self):
        pass

    def contact_details_customer(self):
        pass

    def chat(self):
        pass


class Customer(User):

    def __init__(self, customer_id, customer_name, customer_contact, customer_address):
        super().__init__(customer_id, customer_name)
        self.customer_contact = customer_contact
        self.customer_address = customer_address

    def operation(self) -> str:
        return "{Result of the Customer}"

    def view_taxi(self):
        pass

    def view_location(self):
        pass

    def view_driver_details(self):
        pass

    def view_bill(self):
        pass

    def book_taxi(self):
        pass

    def give_feedback(self):
        pass

    def chat(self):
        pass


class Operator(User):

    def __init__(self, operator_id, operator_name):
        super().__init__(operator_id, operator_name)

    def operation(self) -> str:
        return "{Result of the Operator}"

    def view_transaction(self):
        pass

    def view_billing(self):
        pass

    def contact_customer(self):
        pass

    def view_customer_details(self):
        pass

    def view_driver_details(self):
        pass

    def chat(self):
        pass


"""
------------------------------------------------------------------------------
END
------------------------------------------------------------------------------
"""


class Car:
    """
    This class defines car object.
    """
    def __init__(self, car_id, car_type, car_desc):
        self.car_id = car_id
        self.car_type = car_type
        self.car_desc = car_desc

    def get_car_id(self):
        return self.car_id

    def set_car_id(self, new_car_id):
        self.car_id = new_car_id

    def get_car_type(self):
        return self.car_type

    def set_car_type(self, new_car_type):
        self.car_type = new_car_type

    def get_car_desc(self):
        return self.car_desc

    def set_car_desc(self, new_car_desc):
        self.car_desc = new_car_desc


class Booking:
    """
    This class defines booking object.
    """
    def __init__(self, booking_id, book_status, customer_id, driver_id, location_id, travel_time):
        self.booking_id = booking_id
        self.book_status = book_status
        self.customer_id = customer_id
        self.driver_id = driver_id
        self.location_id = location_id
        self.travel_time = travel_time

    def get_booking_id(self):
        return self.booking_id

    def set_booking_id(self, new_booking_id):
        self.booking_id = new_booking_id

    def get_book_status(self):
        return self.book_status

    def set_book_status(self, new_book_status):
        self.book_status = new_book_status

    def get_customer_id(self):
        return self.customer_id

    def set_customer_id(self, new_customer_id):
        self.customer_id = new_customer_id

    def get_driver_id(self):
        return self.driver_id

    def set_driver_id(self, new_driver_id):
        self.driver_id = new_driver_id

    def get_location_id(self):
        return self.location_id

    def set_location_id(self, new_location_id):
        self.location_id = new_location_id

    def get_travel_time(self):
        return self.travel_time

    def set_travel_time(self, new_travel_time):
        self.travel_time = new_travel_time

    @staticmethod
    def arrange_booking():
        print("arranged")


class Chat:
    """
    This class defines chat object.
    """
    def __init__(self, chat_id, booking_id, customer_id, operator_id, driver_id, chat_messages):
        self.chat_id = chat_id
        self.booking_id = booking_id
        self.customer_id = customer_id
        self.operator_id = operator_id
        self.driver_id = driver_id
        self.chat_messages = chat_messages

    def get_chat_id(self):
        return self.chat_id

    def set_chat_id(self, new_chat_id):
        self.chat_id = new_chat_id

    def get_booking_id(self):
        return self.booking_id

    def set_booking_id(self, new_booking_id):
        self.booking_id = new_booking_id

    def get_customer_id(self):
        return self.customer_id

    def set_customer_id(self, new_customer_id):
        self.customer_id = new_customer_id

    def get_operator_id(self):
        return self.operator_id

    def set_operator_id(self, new_operator_id):
        self.operator_id = new_operator_id

    def get_driver_id(self):
        return self.driver_id

    def set_driver_id(self, new_driver_id):
        self.driver_id = new_driver_id

    def get_chat_messages(self):
        return self.chat_messages

    def add_new_chat_message(self, new_message):
        self.chat_messages.append(new_message)


class Rating:
    """
    This class defines rating object.
    """
    def __init__(self, rating_id, customer_id, booking_id, driver_id, rating_point=0, feedback=''):
        self.rating_id = rating_id
        self.customer_id = customer_id
        self.booking_id = booking_id
        self.driver_id = driver_id
        self.rating_point = rating_point
        self.feedback = feedback

    def get_rating_id(self):
        return self.rating_id

    def set_rating_id(self, new_rating_id):
        self.rating_id = new_rating_id

    def get_customer_id(self):
        return self.customer_id

    def set_customer_id(self, new_customer_id):
        self.customer_id = new_customer_id

    def get_booking_id(self):
        return self.booking_id

    def set_booking_id(self, new_booking_id):
        self.booking_id = new_booking_id

    def get_driver_id(self):
        return self.driver_id

    def set_driver_id(self, new_driver_id):
        self.driver_id = new_driver_id

    def get_rating_point(self):
        return self.rating_point

    def set_rating_point(self, new_rating_point):
        self.rating_point = new_rating_point

    def get_feedback(self):
        return self.feedback

    def set_feedback(self, new_feedback):
        self.feedback = new_feedback


class Payment:
    """
    This class defines payment object.
    """
    def __init__(self, payment_id, booking_id, payment_method, total_amount=0):
        self.payment_id = payment_id
        self.booking_id = booking_id
        self.payment_method = payment_method
        self.total_amount = total_amount

    def get_payment_id(self):
        return self.payment_id

    def set_payment_id(self, new_payment_id):
        self.payment_id = new_payment_id

    def get_booking_id(self):
        return self.booking_id

    def set_booking_id(self, new_booking_id):
        self.booking_id = new_booking_id

    def get_payment_method(self):
        return self.payment_method

    def set_payment_method(self, new_payment_method):
        self.payment_method = new_payment_method

    def get_total_amount(self):
        return self.total_amount

    def set_total_amount(self, new_total_amount):
        self.total_amount = new_total_amount

    @staticmethod
    def generate_bill():
        print("success!!!")


class Location:
    """
    This class defines location object.
    """
    def __init__(self, location_id, booking_id, origin_latlng=(), destination_latlng=(), current_latlng=()):
        self.location_id = location_id
        self.booking_id = booking_id
        self.origin_latlng = origin_latlng
        self.destination_latlng = destination_latlng
        self.current_latlng = current_latlng

    def get_location_id(self):
        return self.location_id

    def set_location_id(self, new_location_id):
        self.location_id = new_location_id

    def get_booking_id(self):
        return self.booking_id

    def set_booking_id(self, new_booking_id):
        self.booking_id = new_booking_id

    def get_origin_latlng(self):
        return self.origin_latlng

    def set_origin_latlng(self, new_origin_latlng):
        self.origin_latlng = new_origin_latlng

    def get_destination_latlng(self):
        return self.destination_latlng

    def set_destination_latlng(self, new_destination_latlng):
        self.destination_latlng = new_destination_latlng

    def get_current_latlng(self):
        return self.current_latlng

    def set_current_latlng(self, new_current_latlng):
        self.current_latlng = new_current_latlng

    @staticmethod
    def calculate_distance():
        print("distance: ")


"""
------------------------------------------------------------------------------
OBSERVER PATTERN FOR LOCATION UPDATE NOTIFICATIONS
------------------------------------------------------------------------------
"""


class Observer(ABC):
    """
    The Observer interface declares the update method, used by NotificationManagers.
    """

    @abstractmethod
    def update(self) -> None:
        """
        Receive update from notification_manager.
        """
        pass


class NotificationManager(ABC):
    """
    The NotificationManager interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the NotificationManager.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the NotificationManager.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass


class ConcreteNotificationManager(NotificationManager):
    """
    The NotificationManager owns some important state and notifies observers when the state
    changes.
    """

    _state: int = None
    """
    For the sake of simplicity, the NotificationManager's state, essential to all
    subscribers, is stored in this variable.
    """

    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def attach(self, observer: Observer) -> None:
        print("NotificationManager: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("NotificationManager: Notifying observers...")
        for observer in self._observers:
            observer.update()

    def update_information(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a NotificationManager can
        really do. NotificationManagers commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """

        print("\nNotificationManager: location updated.")
        self._state = randrange(0, 10)

        print(f"NotificationManager: My state has just changed to: {self._state}")
        self.notify()


"""
User Observers react to the updates issued by the NotificationManager they had been
attached to.
"""


class CustomerObserver(Observer):
    def update(self, notification_manager: NotificationManager) -> None:
        if notification_manager._state < 3:
            print("CustomerObserver: Reacted to the event")


class DriverObserver(Observer):
    def update(self, notification_manager: NotificationManager) -> None:
        if notification_manager._state == 0 or notification_manager._state >= 2:
            print("DriverObserver: Reacted to the event")


class OperatorObserver(Observer):
    def update(self, notification_manager: NotificationManager) -> None:
        if notification_manager._state == 0 or notification_manager._state >= 2:
            print("OperatorObserver: Reacted to the event")


"""
------------------------------------------------------------------------------
END
------------------------------------------------------------------------------
"""
