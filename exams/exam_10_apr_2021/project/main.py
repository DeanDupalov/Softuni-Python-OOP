from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.controller import Controller


def test():
    fresh_aqua = FreshwaterAquarium('FreshAquarium')
    print(fresh_aqua.calculate_comfort())
    controller = Controller()

    print(controller.add_aquarium('FreshwaterAquarium', 'FreshAquarium'))
    print(controller.add_fish("FreshAquarium","FreshwaterAquarium"))
    print(controller.calculate_value('FreshAquarium'))



if __name__ == '__main__':
    test()

# import unittest
#
#
# class TestController(unittest.TestCase):
#     def setUp(self) -> None:
#         self.controller = Controller()
#
#     def test_add(self):
#         pass
#
#
# if __name__ == '__main__':
#     unittest.main()