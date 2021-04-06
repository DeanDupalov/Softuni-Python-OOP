import unittest

from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(unittest.TestCase):

    def setUp(self) -> None:
        self.test_hardware = Hardware('Test_name', 'Heavy', 100, 100)

    def test_init_hardware(self):
        attrs = ['name', 'type', 'capacity', 'memory', 'software_components']
        for attr in attrs:
            self.assertTrue(hasattr(self.test_hardware, attr))

        self.assertEqual('Test_name', self.test_hardware.name)
        self.assertEqual('Heavy', self.test_hardware.type)
        self.assertEqual(100, self.test_hardware.capacity)
        self.assertEqual(100, self.test_hardware.memory)
        self.assertEqual([], self.test_hardware.software_components)

    def test_hardware_install_with_valid_software_obj__should_add_it_to_software_components(self):
        light_software = Software('test', 'Light', 10, 10)
        test_software = Software('test_express', 'Express', 10, 10)
        self.test_hardware.install(light_software)
        self.assertEqual(1, len(self.test_hardware.software_components))
        self.test_hardware.install(test_software)
        self.assertEqual(2, len(self.test_hardware.software_components))

    def test_hardware_install_when_not_enough_memory__should_raise(self):
        light_software = Software('test', 'Light', 10, 1000)
        with self.assertRaises(Exception) as ex:
            self.test_hardware.install(light_software)

        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_hardware_install_when_not_enough_capacity__should_raise(self):
        light_software = Software('test', 'Light', 1000, 10)
        with self.assertRaises(Exception) as ex:
            self.test_hardware.install(light_software)

        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_hardware_uninstall__should_remove_from_software_components(self):
        light_software = Software('test', 'Light', 10, 10)
        self.test_hardware.install(light_software)
        self.test_hardware.uninstall(light_software)
        self.assertEqual(0, len(self.test_hardware.software_components))


if __name__ == '__main__':
    unittest.main()
