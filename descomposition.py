"""
Interpretation of find_gcd Greatest Common Divisor using factorial descomposition
"""


from utils import max_and_min, mesure_execution_time


class GCDStrategies:
    @staticmethod
    def method_1(a: int, b: int) -> int:
        max, min = max_and_min(a, b)
        match = 0

        for i in range(1, min + 1):
            if max % i == 0 and min % i == 0 and match < i:
                match = i

        return match

    @staticmethod
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

    @staticmethod
    def method_3(a: int, b: int) -> int:
        max, min = max_and_min(a, b)
        factor = 1
        while factor < min:
            factor += 1
            if max % factor == 0 and min % factor == 0:
                return factor * GCDStrategies.method_3(max / factor, min / factor)
        return 1


if __name__ == "__main__":
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
