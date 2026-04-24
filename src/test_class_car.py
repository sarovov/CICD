import unittest
from .car import Car

class TestCase(unittest.TestCase):
    def setUp(self):
        self.car = Car(model="BMW X5", fuel_capacity=80)

    def tearDown(self):
        pass

    def test_drive(self):
        self.car.refuel_car(20)
        self.car.drive(20)
        with self.assertRaises(Exception):
            self.car.drive(80000)

    def test_refuel(self):
        self.car.refuel_car(20)
        self.assertEqual(self.car.get_current_fuel_level(), 20)
        with self.assertRaises(Exception):
            self.car.refuel_car(80)
