import unittest
from hello import add, add_numpy
from hello import multiply, multiply_numpy

class TestHello(self, unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(2, add(1,1))
        self.assertEqual(0, add(1, -1))

    def test_add_numpy(self):
        self.assertEqual(2,add_numpy(1,1))
        self.assertEqual(4, add_numpy(-1, 5))

    def test_multiply(self):
        self.assertEqual(4, multiply(2,2))
        self.assertEqual(0, multiply(0, 10))
        self.assertEqual(0, multiply(0, 20))

    def test_multiply_numpy():
        self.assertEqual(4, multiply_numpy(2,2))
        self.assertEqual(0, multiply_numpy(0, 10))
        self.assertEqual(0, multiply_numpy(0, 20))

if __name__ == '__main__':
    unittest.main()



