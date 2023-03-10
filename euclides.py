"""
This is a interpretation of the Euclidies' Algorithm to look for the Greatest Common Divisor(GCD)
between two integers.
"""


# based on 0 < b < a 
def find_gcd(a: int, b: int) -> int:
    # just get the max, min in case they are not sorted
    max, min = (a, b) if a > b else (b, a)

    remainder = max % min

    if remainder == 1:
        return 1
    elif remainder == 0:
        return min
    else:
        return find_gcd(min, remainder)


from unittest import TestCase


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


if __name__ == "__main__":
    from utils import mesure_execution_time
    mesure_execution_time(
        method_name="Euclides' Algorithm",
        action=find_gcd
    )