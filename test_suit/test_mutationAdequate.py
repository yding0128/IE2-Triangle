from unittest import TestCase
from isTriangle import Triangle
import unittest

class test_mutationAdequate(TestCase):

    def test_positive_INVALID(self):
        a = 6
        b = 8
        c = 13
        self.assertEqual(Triangle.classify(a,b,c), Triangle.Type.SCALENE)

if __name__ == '__main__':
    unittest.main()