import unittest

from hash_map_and_sets.pair_sum_unsorted import pair_sum_unsorted

class TestPairSumUnsorted(unittest.TestCase):
    def test_one(self):
        self.assertCountEqual(pair_sum_unsorted([],0), [])
    def test_two(self):
        self.assertCountEqual(pair_sum_unsorted([1],1), [])
    def test_three(self):
        self.assertCountEqual(pair_sum_unsorted([2,3],5), [0,1])
    def test_four(self):
        self.assertCountEqual(pair_sum_unsorted([2,4],5), [])
    def test_five(self):
        self.assertCountEqual(pair_sum_unsorted([-1,3,4,2],3), [0,2])

if __name__=='__main__':
    unittest.main()