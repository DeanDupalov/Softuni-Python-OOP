class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml: int):
        if self.content + ml > Glass.capacity:
            return f"Cannot add {ml} ml"

        self.content += ml
        return f"Glass filled with {ml} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        return f"{Glass.capacity - self.content} ml left"


