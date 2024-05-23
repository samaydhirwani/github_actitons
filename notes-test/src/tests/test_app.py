
import unittest
from notes-test/src.main.app import add, subtract

class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(1, 0), 1)

    def test_subtract(self):
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(2, 2), 0)
        self.assertEqual(subtract(2, 3), -1)

if __name__ == '__main__':
    unittest.main()
