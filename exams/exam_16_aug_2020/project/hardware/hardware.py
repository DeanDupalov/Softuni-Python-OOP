from project.software.software import Software


class Hardware:
    name: str
    type: str  # ("Heavy" or "Power")
    capacity: int
    memory: int

    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    # def install(self, software: Software):
    #     if self.capacity < software.capacity_consumption or self.memory < software.memory_consumption:
    #         raise Exception("Software cannot be installed")
    #     self.software_components.append(software)
    def install(self, software):
        if self.can_install(software):
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def can_install(self, software):
        has_space = sum(
            [s.capacity_consumption for s in self.software_components]) + software.capacity_consumption <= self.capacity
        has_memory = sum(
            [s.memory_consumption for s in self.software_components]) + software.memory_consumption <= self.memory
        return has_memory and has_space

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)

    @property
    def installed_software_memory(self):
        return sum([s.memory_consumption for s in self.software_components])

    @property
    def installed_software_capacity(self):
        return sum([s.capacity_consumption for s in self.software_components])

    def __software_components_str_list(self):
        if self.software_components:
            return ", ".join(map(str, self.software_components))
        return 'None'

    def __repr__(self):
        result = [
            f'Hardware Component - {self.name}',
            f'Express Software Components: {len([s for s in self.software_components if s.type == "Express"])}',
            f'Light Software Components: {len([s for s in self.software_components if s.type == "Light"])}',
            f'Memory Usage: {self.installed_software_memory} / {self.memory}',
            f'Capacity Usage: {self.installed_software_capacity} / {self.capacity}',
            f'Type: {self.type}',
            f'Software Components: {self.__software_components_str_list()}',
        ]
        return '\n'.join(result)
