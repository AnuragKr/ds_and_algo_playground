import unittest

from two_pointers.triplet_sum import triplet_sum

class TestPairSumSorted(unittest.TestCase):
    def test_one(self):
        self.assertCountEqual(triplet_sum([]), [])
    def test_two(self):
        self.assertCountEqual(triplet_sum([0]), [])
    def test_three(self):
        self.assertCountEqual(triplet_sum([1,-1]), [])
    def test_four(self):
        self.assertCountEqual(triplet_sum([0,0,0]), [[0,0,0]])
    def test_five(self):
        self.assertCountEqual(triplet_sum([1,0,1]), [])
    def test_six(self):
        self.assertCountEqual(triplet_sum([0,0,1,-1,1,-1]), [[-1,0,1]])
    def test_seven(self):
        self.assertCountEqual(triplet_sum([0,-1,2,-3,1]), [[-3,1,2], [-1,0,1]])

if __name__=='__main__':
    unittest.main()