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

        if hardware_name not in map(lambda h: h.name, System._hardware):
            return "Hardware does not exist"
        current_hardware = [h for h in System._hardware if h.name == hardware_name][0]
        current_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            current_hardware.install(current_software)
            System._software.append(current_software)
        except Exception as context:
            return str(context)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):

        if hardware_name not in map(lambda h: h.name, System._hardware):
            return "Hardware does not exist"

        current_hardware = [h for h in System._hardware if h.name == hardware_name][0]
        current_software = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            current_hardware.install(current_software)
            System._software.append(current_software)
        except Exception as context:
            return str(context)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        current_hardware = [h for h in System._hardware if h.name == hardware_name]
        current_software = [s for s in System._software if s.name == software_name]
        if not current_software or not current_hardware:
            return "Some of the components do not exist"

        current_hardware[0].uninstall(current_software[0])

    @staticmethod
    def analyze():
        total_memory = sum([h.memory for h in System._hardware])
        total_capacity = sum([h.capacity for h in System._hardware])
        total_used_memory = sum([s.memory_consumption for s in System._software])
        total_used_space = sum([s.capacity_consumption for s in System._software])
        result = [f"System Analysis",
                  f"Hardware Components: {len(System._hardware)}",
                  f"Software Components: {len(System._software)}",
                  f"Total Operational Memory: {total_used_memory} / {total_memory}",
                  f"Total Capacity Taken: {total_used_space} / {total_capacity}"]
        return "\n".join(result)

    @staticmethod
    def system_split():
        result = [hardware.__repr__() for hardware in System._hardware]
        return ''.join(result)





