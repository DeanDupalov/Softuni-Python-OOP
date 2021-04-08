# from project.card.magic_card import MagicCard
# from project.card.trap_card import TrapCard
# from project.controller import Controller
# from project.player.advanced import Advanced
# from project.player.beginner import Beginner
#
#
# def test():
#     bg = Beginner('test_username')
#     ad = Advanced('advanced')
#     mgc = MagicCard('test_magic')
#     trap = TrapCard('test_trap')
#     mgc_2 = MagicCard('test_magic2')
#     tra2 = TrapCard('test_trap2')
#
#     controller = Controller()
#     print(ad.card_repository.add(MagicCard('MAGIC_TEST')))
#     print(controller.add_player('Beginner', 'test_username'))
#     print(controller.add_player('Advanced', 'advanced'))
#     print(controller.add_card('Magic', 'test_magic'))
#     print(bg.card_repository.add(mgc_2))
#     print(ad.card_repository.add(trap))
#
#     print(controller.add_player())
#     print(controller.add_player(bg))
#
#     print(controller.card_repository.add(mgc_2))
#     print(controller.card_repository.add(trap))
#     # print(controller.add_card('Trap', 'test_trap'))
#     print(controller.add_card('Trap', 'test_trap2'))
#     print(controller.report())
#
#
#
# if __name__ == '__main__':
#     test()