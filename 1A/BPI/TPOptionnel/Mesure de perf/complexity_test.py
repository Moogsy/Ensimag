from collections import defaultdict
from typing import Callable

import random
import time

from matplotlib import pyplot as plt

from main import insert_sort, merge_sort, select_sort


def generate_random_list(length: int) -> list[int]:
    """Generate a list of random numbers
    - Containing `length` numbers within the integer
    range [0, length - 1].
    """
    return random.choices(range(length), k=length)


def get_time(sorter: Callable[[list], None], li: list) -> float:
    li2 = li.copy()

    start = time.perf_counter()
    sorter(li2)
    stop = time.perf_counter()

    return stop - start


def main():
    ax: plt.Axes
    _, ax = plt.subplots() # type: ignore
    num_test = 500

    x_axis = list(range(num_test))
    sorters = [insert_sort, merge_sort, select_sort]
    times = defaultdict(list)

    for k in x_axis:
        li = generate_random_list(k)

        for sorter in sorters:
            times[sorter.__name__].append(get_time(sorter, li.copy()))

    for sorter in sorters:
        ax.plot(x_axis, times[sorter.__name__], label=sorter.__name__)

    ax.legend()
    ax.set_xlabel("Amount of elements")
    ax.set_ylabel("Sortime time")

    plt.show()


if __name__ == "__main__":
    main()
