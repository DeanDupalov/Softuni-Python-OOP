from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, type="Power", capacity=int(capacity * 0.25), memory=int(memory * 1.75))
