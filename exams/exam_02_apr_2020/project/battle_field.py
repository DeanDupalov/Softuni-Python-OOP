from project.player.player import Player


class BattleField:

    @staticmethod
    def __get_sum_health_point_deck(player):
        result = 0
        for card in player.card_repository:
            result += card.health_points
        return result

    @staticmethod
    def fight(attacker: Player, enemy: Player):
        # for p in [attacker, enemy]:
        #     if p.is_dead:
        #         raise ValueError("Player is dead!")
        #     if p.__class__.__name__ == "Beginner":
        #         p.health += 40
        #         for card in p.card_repository:
        #             card.damage_points += 30
        #
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        if attacker.__class__.__name__ == "Beginner":
            attacker.health += 40
            for card in attacker.card_repository.cards:
                card.damage_points += 30

        if enemy.__class__.__name__ == "Beginner":
            enemy.health += 40
            for card in enemy.card_repository.cards:
                card.damage_points += 30

        for card in attacker.card_repository.cards:
            attacker.health += card.health_points

        for card in enemy.card_repository.cards:
            enemy.health += card.health_points

        for card in attacker.card_repository.cards:
            enemy.take_damage(card.damage_points)

        for card in enemy.card_repository.cards:
            attacker.take_damage(card.damage_points)
