import unittest

from two_pointers.pair_sum_sorted import pair_sum_sorted

class TestPairSumSorted(unittest.TestCase):
    def test_one(self):
        self.assertCountEqual(pair_sum_sorted([],0), [])
    def test_two(self):
        self.assertCountEqual(pair_sum_sorted([1],1), [])
    def test_three(self):
        self.assertCountEqual(pair_sum_sorted([2,3],5), [0,1])
    def test_four(self):
        self.assertCountEqual(pair_sum_sorted([2,4],5), [])

if __name__=='__main__':
    unittest.main()