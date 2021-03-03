class Trainer:
    ID = 1
    name: str

    def __init__(self, name):
        self.name = name
        self.id = Trainer.ID
        Trainer.ID += 1

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Trainer.ID
