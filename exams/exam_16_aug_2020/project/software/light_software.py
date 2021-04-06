from project.software.software import Software


class LightSoftware(Software):
    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, type="Light", capacity_consumption=int(capacity_consumption * 1.5),
                         memory_consumption=int(memory_consumption * 0.5))
