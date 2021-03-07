class Zoo:
    def __init__(self, name: str, budget, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget < price:  # + animal.get_needs():
            return "Not enough budget"

        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price  # + animal.get_needs()
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        result = [w for w in self.workers if w.name == worker_name]
        if not result:
            return f"There is no {worker_name} in the zoo"

        current_worker = result[0]
        self.workers.remove(current_worker)
        return f"{worker_name} fired successfully"

    def __get_workers_total_salary(self):
        total_salary = 0
        for w in self.workers:
            total_salary += w.salary

        return total_salary

    def __get_money_needed_to_tend_all_animals(self):
        amount = 0
        for a in self.animals:
            amount += a.get_needs()

        return amount

    @staticmethod
    def __get_list_of_animals_by_name(name, all_animals):
        result = [a for a in all_animals if a.__class__.__name__ == name]
        return result

    @staticmethod
    def __get_list_of_workers_by_name(name, all_workers):
        result = [w for w in all_workers if w.__class__.__name__ == name]
        return result

    def pay_workers(self):
        total_salary = self.__get_workers_total_salary()
        if total_salary > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= total_salary
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        money_needed = self.__get_money_needed_to_tend_all_animals()
        if money_needed > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= money_needed
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = self.__get_list_of_animals_by_name('Lion', self.animals)
        tigers = self.__get_list_of_animals_by_name('Tiger', self.animals)
        cheetahs = self.__get_list_of_animals_by_name('Cheetah', self.animals)
        result = f"You have {len(self.animals)} animals" + '\n'
        result += f"----- {len(lions)} Lions:" + "\n" + "\n".join(map(str, lions)) + "\n"
        result += f"----- {len(tigers)} Tigers:" + "\n" + "\n".join(map(str, tigers)) + "\n"
        result += f"----- {len(cheetahs)} Cheetahs:" + "\n" + "\n".join(map(str, cheetahs))
        return result

    def workers_status(self):
        keepers = self.__get_list_of_workers_by_name('Keeper', self.workers)
        caretakers = self.__get_list_of_workers_by_name('Caretaker', self.workers)
        vets = self.__get_list_of_workers_by_name('Vet', self.workers)
        result = f"You have {len(self.workers)} workers" + "\n"
        result += f"----- {len(keepers)} Keepers:" + "\n" + "\n".join(map(str, keepers)) + "\n"
        result += f"----- {len(caretakers)} Caretakers:" + "\n" + "\n".join(map(str, caretakers)) + "\n"
        result += f"----- {len(vets)} Vets:" + "\n" + "\n".join(map(str, vets))
        return result

# from encapsulation.wild_cat_zoo_1.project.lion import Lion
# from encapsulation.wild_cat_zoo_1.project.cheetah import Cheetah
# from encapsulation.wild_cat_zoo_1.project.tiger import Tiger
# from encapsulation.wild_cat_zoo_1.project.keeper import Keeper
# from encapsulation.wild_cat_zoo_1.project.caretaker import Caretaker
# from encapsulation.wild_cat_zoo_1.project.vet import Vet
#
# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4),
#            Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68),
#            Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280),
#            Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Fireing worker
# print(zoo.fire_worker("Adam"))
#
# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())
