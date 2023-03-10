"""
Interpretation of find_gcd Greatest Common Divisor using factorial descomposition
"""

import typing


def max_and_min(a: int, b: int) -> typing.Tuple[int, int]:
    return (a, b) if a > b else (b, a)


class GCDStrategies:
    @staticmethod
    def method_1(a: int, b: int) -> int:
        max, min = max_and_min(a, b)
        match = 0

        for i in range(1, min + 1):
            if max % i == 0 and min % i == 0 and match < i:
                match = i

        return match

    def method_2(a: int, b: int) -> int:
        max, min = max_and_min(a, b)
        accumulator, factor = 1, 1

        while factor < min:
            factor += 1
            if max % factor == 0 and min % factor == 0:
                accumulator = accumulator * factor
                max = max / factor
                min = min / factor
                factor = 1

        return accumulator

    def method_3(a: int, b: int) -> int:
        max, min = max_and_min(a, b)
        factor = 1
        while factor < min:
            factor += 1
            if max % factor == 0 and min % factor == 0:
                return factor * GCDStrategies.method_3(max / factor, min / factor)
        return 1


from unittest import TestCase


class TestDescomposition(TestCase):
    def test_multiples(self):
        a, b = (10, 5)
        assert GCDStrategies.method_1(a, b) == 5
        assert GCDStrategies.method_2(a, b) == 5

    def test_primes_numbers(self):
        a, b = (23, 7)
        assert GCDStrategies.method_1(a, b) == 1
        assert GCDStrategies.method_2(a, b) == 1

    def test_big_numbers(self):
        a, b = (512 * 3 * 4, 512 * 2 * 4)
        assert GCDStrategies.method_1(a,b) == 512 * 4
        assert GCDStrategies.method_2(a, b) == 512 * 4


if __name__ == "__main__":
    from utils import mesure_execution_time

    mesure_execution_time(
        method_name="Factorial Descomposition 1",
        action=GCDStrategies.method_1,
    )

    mesure_execution_time(
        method_name="Factorial Descomposition 2",
        action=GCDStrategies.method_2,
    )

    mesure_execution_time(
        method_name="Factorial Descomposition 3",
        action=GCDStrategies.method_3,
    )
