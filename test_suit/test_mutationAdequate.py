from unittest import TestCase
from isTriangle import Triangle
import unittest

class test_mutationAdequate(TestCase):

    def test_INVALID_a(self):
        a = -1
        b = 1
        c = 1
        self.assertEqual(Triangle.classify(a,b,c), Triangle.Type.INVALID)

    def test_INVALID_all_negative(self):
        a = -1
        b = -1
        c = -1
        self.assertEqual(Triangle.classify(a,b,c), Triangle.Type.INVALID)
    
    def test_INVALID_b(self):
        a = 1
        b = -1
        c = 1
        self.assertEqual(Triangle.classify(a,b,c), Triangle.Type.INVALID)

    def test_INVALID_c(self):
        a = 1
        b = -1
        c = 1
        self.assertEqual(Triangle.classify(a,b,c), Triangle.Type.INVALID)

    def test_INVALID_a0(self):
        a = 0
        b = 1
        c = 1
        self.assertEqual(Triangle.classify(a,b,c), Triangle.Type.INVALID)

    def test_INVALID_b0(self):
        a = 1
        b = 0
        c = 1
        self.assertEqual(Triangle.classify(a,b,c), Triangle.Type.INVALID)

    def test_INVALID_c0(self):
        a = 1
        b = 1
        c = 0
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

    def test_c_equal_INVALID(self):
        a = 6
        b = 8
        c = 14
        self.assertEqual(Triangle.classify(a,b,c), Triangle.Type.INVALID)
    
    def test_b_equal_INVALID(self):
        a = 6
        b = 14
        c = 8
        self.assertEqual(Triangle.classify(a,b,c), Triangle.Type.INVALID)
    
    def test_a_equal_INVALID(self):
        a = 14
        b = 6
        c = 8
        self.assertEqual(Triangle.classify(a,b,c), Triangle.Type.INVALID)
    
    def test_c_less_INVALID(self):
        a = 6
        b = 6
        c = 13
        self.assertEqual(Triangle.classify(a, b, c), Triangle.Type.INVALID)
    
    def test_a_less_INVALID(self):
        a = 13
        b = 6
        c = 6
        self.assertEqual(Triangle.classify(a, b, c), Triangle.Type.INVALID)

    def test_b_less_INVALID(self):
        a = 6
        b = 13
        c = 6
        self.assertEqual(Triangle.classify(a, b, c), Triangle.Type.INVALID)
    
    def test_ISOSCELES_c_equal(self):
        a = 4
        b = 4
        c = 8
        self.assertEqual(Triangle.classify(a, b, c), Triangle.Type.INVALID)
    
    def test_ISOSCELES_b_equal(self):
        a = 4
        b = 8
        c = 4
        self.assertEqual(Triangle.classify(a, b, c), Triangle.Type.INVALID)
    
    def test_ISOSCELES_a_equal(self):
        a = 8
        b = 4
        c = 4
        self.assertEqual(Triangle.classify(a, b, c), Triangle.Type.INVALID)
    
    def test_SCALENE_invalid_c(self):
        a = 2
        b = 3
        c = 5
        self.assertEqual(Triangle.classify(a, b, c), Triangle.Type.INVALID)
    
    def test_SCALENE_invalid_c(self):
        a = 5
        b = 3
        c = 2
        self.assertEqual(Triangle.classify(a, b, c), Triangle.Type.INVALID)
    
    def test_SCALENE_invalid_c(self):
        a = 5
        b = 2
        c = 3
        self.assertEqual(Triangle.classify(a, b, c), Triangle.Type.INVALID)
    
    def test_c_less_INVALID_equal(self):
        a = 6
        b = 6
        c = 12
        self.assertEqual(Triangle.classify(a, b, c), Triangle.Type.INVALID)
    
    def test_a_less_INVALID_equal(self):
        a = 12
        b = 6
        c = 6
        self.assertEqual(Triangle.classify(a, b, c), Triangle.Type.INVALID)

    def test_b_less_INVALID_equal(self):
        a = 6
        b = 12
        c = 6
        self.assertEqual(Triangle.classify(a, b, c), Triangle.Type.INVALID)

    def test_c_invalid_SCALENE(self):
        a = 1
        b = 2
        c = 5
        self.assertEqual(Triangle.classify(a, b, c), Triangle.Type.INVALID)
    
    def test_a_invalid_SCALENE(self):
        a = 5
        b = 2
        c = 1
        self.assertEqual(Triangle.classify(a, b, c), Triangle.Type.INVALID)
    
    def test_b_invalid_SCALENE(self):
        a = 1
        b = 5
        c = 2
        self.assertEqual(Triangle.classify(a, b, c), Triangle.Type.INVALID)
if __name__ == '__main__':
    unittest.main()