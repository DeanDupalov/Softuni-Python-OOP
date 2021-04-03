import unittest

from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(unittest.TestCase):
    def setUp(self) -> None:
        self.hardware = Hardware('test_hardware', 'Power', 100, 200)

    def test_HardwareInitialization(self):
        hardware = Hardware('Test', 'Heavy', 100, 200)
        self.assertEqual(hardware.name, 'Test')
        self.assertEqual(hardware.type, 'Heavy')
        self.assertEqual(hardware.capacity, 100)
        self.assertEqual(hardware.memory, 200)
        self.assertEqual(len(hardware.software_components), 0)


    def test_HardwareInitialization_with_wrong_type_shouldRaise(self):
        with self.assertRaises(Exception) as context:
           Hardware('Test', 'Big', 100, 200)
        self.assertIsNotNone(context.exception)

    def test_HardwareInstall(self):
        test_software = Software('TestSoftware', 'Light', 20, 30)
        self.hardware.install(test_software)
        self.assertEqual(len(self.hardware.software_components), 1)

    def test_HardwareInstall_whenNotEnoughCapacityAndMemory_shouldRaise(self):
        test_software = Software('TestSoftware', 'Light', 200, 300)

        with self.assertRaises(Exception) as context:
            self.hardware.install(test_software)

        self.assertIsNotNone(context.exception)
        self.assertEqual(context.exception.__str__(), "Software cannot be installed")

    def test_HardwareUninstall(self):
        test_software = Software('TestSoftware', 'Light', 20, 30)
        test_software2 = Software('TestSoftware2', 'Light', 10, 30)

        self.hardware.install(test_software)
        self.hardware.install(test_software2)
        self.hardware.uninstall(test_software)
        self.assertEqual(len(self.hardware.software_components), 1)
        self.hardware.uninstall(test_software2)
        self.assertEqual(len(self.hardware.software_components), 0)


if __name__ == '__main__':
    unittest.main()
