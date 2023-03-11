from unittest import TestCase

from euclides import find_gcd


class TestSuie(TestCase):
    def test_multiples(self):
        a, b = (10, 5)
        assert find_gcd(a, b) == 5

    def test_primes_numbers(self):
        a, b = (23, 7)
        assert find_gcd(a, b) == 1

    def test_big_numbers(self):
        a, b = (512*3*4, 512*2*4)
        assert find_gcd(a,b) == 512*4
