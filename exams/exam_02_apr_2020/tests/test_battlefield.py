import unittest

from project.battle_field import BattleField
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattleField(unittest.TestCase):
    def setUp(self) -> None:
        attacker = Advanced('name')
        enemy = Advanced('enemy')
        self.test_battlefield = BattleField()

    def test_fight_if_one_of_the_players_is_dead_should_raise(self):
        attacker = Advanced('name')
        enemy = Beginner('enemy')
        pass

    def test_fight_if_beginner_should_increase_health_with_40_points(self):
        pass


if __name__ == '__main__':
    unittest.main()
