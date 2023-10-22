from unittest import TestCase
from isTriangle import Triangle
import unittest

class test_decisionCoverage(TestCase):

    def test_INVALID(self):
        a = -1
        b = 1
        c = 1
        self.assertEqual(Triangle.classify(a,b,c), Triangle.Type.INVALID)
    
    def test_EQUILATERAL(self):
        a = 1
        b = 1
        c = 1
        self.assertEqual(Triangle.classify(a,b,c), Triangle.Type.EQUILATERAL)
    
    def test_ISOSCELES_1(self):
        a = 2
        b = 2
        c = 1
        self.assertEqual(Triangle.classify(a,b,c), Triangle.Type.ISOSCELES)
    
    def test_ISOSCELES_2(self):
        a = 2
        b = 1
        c = 2
        self.assertEqual(Triangle.classify(a,b,c), Triangle.Type.ISOSCELES)

    def test_ISOSCELES_3(self):
        a = 1
        b = 2
        c = 2
        self.assertEqual(Triangle.classify(a,b,c), Triangle.Type.ISOSCELES)
    
    def test_trian1_INVALID(self):
        a = 2
        b = 2
        c = 4
        self.assertEqual(Triangle.classify(a,b,c), Triangle.Type.INVALID)
    
    def test_SCALENE(self):
        a = 6
        b = 8
        c = 10
        self.assertEqual(Triangle.classify(a,b,c), Triangle.Type.SCALENE)
    
    def test_positive_INVALID(self):
        a = 6
        b = 8
        c = 14
        self.assertEqual(Triangle.classify(a,b,c), Triangle.Type.INVALID)
    
if __name__ == '__main__':
    unittest.main()