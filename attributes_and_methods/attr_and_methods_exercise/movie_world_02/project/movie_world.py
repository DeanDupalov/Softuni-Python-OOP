from typing import List
from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    name: str
    customers: List

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    def __repr__(self):
        result = ''
        for i, c in enumerate(self.customers):
            result += f'{str(c)}\n'

        for i, d in enumerate(self.dvds):
            result += f'{str(d)}\n'

        return result

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer):
        if MovieWorld.CUSTOMER_CAPACITY > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if MovieWorld.DVD_CAPACITY > len(self.dvds):
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        current_customer = [c for c in self.customers if c.id == customer_id][0]
        current_dvd = [d for d in self.dvds if d.id == dvd_id][0]

        if current_dvd in current_customer.rented_dvds:
            return f"{current_customer.name} has already rented {current_dvd.name}"

        if current_dvd.is_rented:
            return "DVD is already rented"

        if current_dvd.age_restriction > current_customer.age:
            return f"{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie"


        current_customer.rented_dvds.append(current_dvd)
        current_dvd.is_rented = True
        return f"{current_customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        current_customer = [c for c in self.customers if c.id == customer_id][0]
        current_dvd = [d for d in self.dvds if d.id == dvd_id][0]
        if current_dvd not in current_customer.rented_dvds:
            return f"{current_customer.name} does not have that DVD"

        current_customer.rented_dvds.remove(current_dvd)
        current_dvd.is_rented = False

        return f"{current_customer.name} has successfully returned {current_dvd.name}"


# from movie_world_02.project.customer import Customer
# from movie_world_02.project.dvd import DVD
#
# c1 = Customer("John", 16, 1)
# c2 = Customer("Anna", 55, 2)
#
# d1 = DVD("Black Widow", 1, 2020, "April", 18)
# d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)
#
# movie_world = MovieWorld("The Best Movie Shop")
#
# movie_world.add_customer(c1)
# movie_world.add_customer(c2)
#
# movie_world.add_dvd(d1)
# movie_world.add_dvd(d2)
#
# print(movie_world.rent_dvd(1, 1))
# print(movie_world.rent_dvd(2, 1))
# print(movie_world.rent_dvd(1, 2))
#
# print(movie_world)
