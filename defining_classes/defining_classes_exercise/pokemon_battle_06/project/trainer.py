from project.pokemon import Pokemon


class Trainer:
    name: str

    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemon:
            return "This pokemon is already caught"
        self.pokemon.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        if pokemon_name not in map(lambda h: h.name, self.pokemon):
            return "Pokemon is not caught"
        current_pokemon = [p for p in self.pokemon if p.name == pokemon_name][0]
        self.pokemon.remove(current_pokemon)
        return f"You have released {pokemon_name}"

    def trainer_data(self):
        result = f'Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n'
        for p in self.pokemon:
            result += f'- {p.pokemon_details()}\n'

        return result


# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())
