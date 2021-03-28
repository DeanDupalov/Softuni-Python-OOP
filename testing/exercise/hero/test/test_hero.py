import unittest

from project.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self) -> None:
        self.hero = Hero('Hero', 10, 100.0, 2)
        self.enemy = Hero('Enemy', 5, 100.0, 2)

    def test_battle_enemy_name_is_equal_to_hero_name__should_raise(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        expected = "You cannot fight yourself"
        self.assertEqual(expected, ex.exception.args[0])

    def test_battle__when_battle_begins_hero_health_equal_to_zero_or_below__should_raise(self):
        test_hero = Hero('test_name', 10, 0.0, 2)
        with self.assertRaises(Exception) as context:
            test_hero.battle(self.enemy)
        expected = "Your health is lower than or equal to 0. You need to rest"
        actual = context.exception.args[0]
        self.assertEqual(expected, actual)

    def test_battle__when_battle_begins_enemy__health_equal_to_zero_or_below__should_raise(self):
        test_enemy = Hero('test_enemy', 10, 0.0, 2)
        with self.assertRaises(Exception) as context:
            self.hero.battle(test_enemy)
        expected = "You cannot fight test_enemy. He needs to rest"
        actual = context.exception.args[0]
        self.assertEqual(expected, actual)

    def test_battle_hero_damage(self):
        actual = self.hero.damage * self.hero.level
        expected = 20
        self.assertEqual(expected, actual)

    def test_battle_enemy_damage(self):
        actual = self.enemy.damage * self.enemy.level
        expected = 10
        self.assertEqual(expected, actual)

    def test_battle__hero_health_should_decrease_with_enemy_damage(self):
        self.hero.battle(self.enemy)
        actual = self.hero.health
        expected = 90.0
        self.assertEqual(expected, actual)

    def test_battle__enemy_health_should_decrease_with_hero_damage(self):
        self.enemy.battle(self.hero)
        actual = self.enemy.health
        expected = 80.0
        self.assertEqual(expected, actual)

    def test_battle__when_hero_and_enemy_health_equal_or_below_zero_should_return_draw(self):
        hero = Hero('hero', 10, 10.0, 2)
        enemy = Hero('enemy', 10, 10.0, 2)
        actual = hero.battle(enemy)
        expected = 'Draw'

        self.assertEqual(expected, actual)

    def test_battle__after_attack_hero_health_equal_to_zero_or_below__should_return_you_lose(self):
        hero = Hero('hero', 10, 10.0, 2)
        enemy = Hero('enemy', 10, 50.0, 2)
        actual = hero.battle(enemy)
        expected = "You lose"

        self.assertEqual(expected, actual)
        self.assertEqual(enemy.level, 11)
        self.assertEqual(enemy.health, 35)
        self.assertEqual(enemy.damage, 7)

    def test_battle__after_attack__enemy__health_equal_to_zero_or_below__should_return_you_win(self):
        hero = Hero('hero', 10, 50.0, 2)
        enemy = Hero('enemy', 10, 10.0, 2)
        actual = hero.battle(enemy)
        expected = "You win"

        self.assertEqual(expected, actual)
        self.assertEqual(hero.level, 11)
        self.assertEqual(hero.health, 35)
        self.assertEqual(hero.damage, 7)

    def test_str(self):
        expected = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"

        actual = self.hero.__str__()
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
