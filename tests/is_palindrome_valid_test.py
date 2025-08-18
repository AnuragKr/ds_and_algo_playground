import unittest

from arrays.is_palindrome_valid import is_palindrome_valid

class IsPalindromeValid(unittest.TestCase):
    def test_one(self):
        self.assertEqual(is_palindrome_valid(""), True)
    def test_two(self):
        self.assertEqual(is_palindrome_valid("a"), True)
    def test_three(self):
        self.assertEqual(is_palindrome_valid("aa"), True)
    def test_four(self):
        self.assertEqual(is_palindrome_valid("ab"), False)
    def test_five(self):
        self.assertEqual(is_palindrome_valid("!, (?)"), True)
    def test_six(self):
        self.assertEqual(is_palindrome_valid("12.02.2021"), True)
    def test_seven(self):
        self.assertEqual(is_palindrome_valid("hello, world!"), False)
    def test_eight(self):
        self.assertEqual(is_palindrome_valid("21.02.2021"), False)

if __name__=='__main__':
    unittest.main()