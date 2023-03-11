import sys
import time
import typing


def mesure_execution_time(method_name: str ,action: typing.Callable[[int, int], int]):
    a, b = int(sys.argv[1]), int(sys.argv[2])

    # get the end time
    start = time.time()
    response =action(a,b)
    final = time.time()

    # get the execution time
    delta_time =final - start

    print(f"Method:\t{method_name}\nGCD on ({a}, {b}):\t{response}.\nExecution time (µs):\t{'%4.4f' % (delta_time*1e+6)}.\n+=============================+\n")

def max_and_min(a: int, b: int) -> typing.Tuple[int, int]:
    return (a, b) if a > b else (b, a)