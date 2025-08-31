import unittest

from two_pointers.largest_container import largest_container

class LargestContainer(unittest.TestCase):
    def test_one(self):
        self.assertEqual(largest_container([]), 0)
    def test_two(self):
        self.assertEqual(largest_container([1]), 0)
    def test_three(self):
        self.assertEqual(largest_container([0,1,0]), 0)
    def test_four(self):
        self.assertEqual(largest_container([3,3,3,3]), 9)
    def test_five(self):
        self.assertEqual(largest_container([1,2,3]), 2)
    def test_six(self):
        self.assertEqual(largest_container([3,2,1]), 2)

if __name__=='__main__':
    unittest.main()