import unittest
from quick_keyboard import KeyMonitor
from pynput import keyboard


class MyTestCase(unittest.TestCase):
    def create_base(self):
        pass

    def test_get_combination(self):
        print('input combination alt + shift (left)')
        keys = KeyMonitor()
        comb = keys.get_combination()
        self.assertTrue((keyboard.Key.alt_l in comb) and (keyboard.Key.shift_l in comb))


if __name__ == '__main__':
    unittest.main()
