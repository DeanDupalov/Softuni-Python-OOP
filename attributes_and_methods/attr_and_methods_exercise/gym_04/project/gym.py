class Gym:

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def __get_subscription(self, subscription_id):
        return [subscription for subscription in self.subscriptions if subscription.id == subscription_id][0]

    def __get_customer(self, customer_id):
        return [customer for customer in self.customers if customer.id == customer_id][0]

    def __get_equipment(self, equipment_id):
        return [equipment for equipment in self.equipment if equipment.id == equipment_id][0]

    def __get_trainer(self, trainer_id):
        return [trainer for trainer in self.trainers if trainer.id == trainer_id][0]

    def __get_plan(self, plan_id):
        return [plan for plan in self.plans if plan.id == plan_id][0]

    def subscription_info(self, subscription_id: int):
        current_subscription = self.__get_subscription(subscription_id)
        current_customer = self.__get_customer(current_subscription.customer_id)
        current_trainer = self.__get_trainer(current_subscription.trainer_id)
        current_plan = self.__get_plan(current_subscription.exercise_id)
        current_equipment = self.__get_equipment(current_subscription.exercise_id)

        result = current_subscription.__repr__() + '\n' + current_customer.__repr__() \
                 + '\n' + current_trainer.__repr__() + '\n' + current_equipment.__repr__() \
                 + '\n' + current_plan.__repr__()
        return result


from gym_04.project.customer import Customer
from gym_04.project.equipment import Equipment
from gym_04.project.exercise_plan import ExercisePlan
from gym_04.project.subscription import Subscription
from gym_04.project.trainer import Trainer
# #
# from project.customer import Customer
# from project.equipment import Equipment
# from project.exercise_plan import ExercisePlan
# from project.gym import Gym
# from project.subscription import Subscription
# from project.trainer import Trainer

# customer = Customer("John", "Maple Street", "john.smith@gmail.com")
# equipment = Equipment("Treadmill")
# trainer = Trainer("Peter")
# subscription = Subscription("14.05.2020", 1, 1, 1)
# plan = ExercisePlan(1, 1, 20)
#
# gym = Gym()
#
# gym.add_customer(customer)
# gym.add_equipment(equipment)
# gym.add_trainer(trainer)
# gym.add_plan(plan)
# gym.add_subscription(subscription)
#
# print(Customer.get_next_id())
#
# print(gym.subscription_info(1))

