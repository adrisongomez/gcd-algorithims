from unittest import TestCase

from descomposition import GCDStrategies


class TestDescomposition(TestCase):
    def test_multiples(self):
        a, b = (10, 5)
        assert GCDStrategies.method_1(a, b) == 5
        assert GCDStrategies.method_2(a, b) == 5
        assert GCDStrategies.method_3(a, b) == 5

    def test_primes_numbers(self):
        a, b = (23, 7)
        assert GCDStrategies.method_1(a, b) == 1
        assert GCDStrategies.method_2(a, b) == 1
        assert GCDStrategies.method_3(a, b) == 1

    def test_big_numbers(self):
        a, b = (512 * 3 * 4, 512 * 2 * 4)
        assert GCDStrategies.method_1(a,b) == 512 * 4
        assert GCDStrategies.method_2(a, b) == 512 * 4
        assert GCDStrategies.method_3(a, b) == 512 * 4
