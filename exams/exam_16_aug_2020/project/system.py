from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        if hardware_name not in map(lambda x: x.name, System._hardware):
            return "Hardware does not exist"
        hardware = [h for h in System._hardware if h.name == hardware_name][0]
        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(software)

        except Exception as ex:
            return str(ex)
        System._software.append(software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        if hardware_name not in map(lambda x: x.name, System._hardware):
            return "Hardware does not exist"
        hardware = [h for h in System._hardware if h.name == hardware_name][0]
        software = LightSoftware(name, capacity_consumption, memory_consumption)

        try:
            hardware.install(software)

        except Exception as ex:
            return str(ex)

        System._software.append(software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        if hardware_name not in map(lambda x: x.name, System._hardware) \
                or software_name not in map(lambda x: x.name, System._software):
            return "Some of the components do not exist"

        hardware = [h for h in System._hardware if h.name == hardware_name][0]
        software = [s for s in System._software if s.name == software_name][0]
        hardware.uninstall(software)

    @staticmethod
    def __get_total_memory():
        return sum([h.memory for h in System._hardware])

    @staticmethod
    def __get_total_capacity():
        return sum([h.capacity for h in System._hardware])

    @staticmethod
    def __get_used_memory():
        return sum([h.installed_software_memory for h in System._hardware])

    @staticmethod
    def __get_used_capacity():
        return sum([h.installed_software_capacity for h in System._hardware])

    @staticmethod
    def analyze():
        result = [
            'System Analysis',
            f'Hardware Components: {len(System._hardware)}',
            f'Software Components: {len(System._software)}',
            f'Total Operational Memory: {System.__get_used_memory()} / {System.__get_total_memory()}',
            f'Total Capacity Taken: {System.__get_used_capacity()} / {System.__get_total_capacity()}',
        ]
        return '\n'.join(result)

    @staticmethod
    def system_split():
        result = [str(h) for h in System._hardware]
        return ''.join(result)
