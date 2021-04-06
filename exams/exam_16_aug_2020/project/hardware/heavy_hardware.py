from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, type="Heavy", capacity=capacity * 2, memory=int(memory*0.75))