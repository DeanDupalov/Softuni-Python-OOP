class CardRepository:
    count: int
    cards: list

    def __init__(self):
        self.count = 0
        self.cards = []  # collection of cards

    def __len__(self):
        return len(self.cards)

    def add(self, card):
        if card.name in map(lambda c: c.name, self.cards):
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        self.cards.remove(self.find(card))
        self.count -= 1

    def find(self, name: str):
        return [c for c in self.cards if name == c.name][0]
