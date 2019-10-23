from timeit import default_timer as timer

import numpy as np
from numba import vectorize


@vectorize(['float32(float32, float32)'], target='cuda')
def power(a, b):
    return a ** b


def main():
    vec_size = 100000000
    a = b = np.array(np.random.sample(vec_size), dtype=np.float32)
    c = np.zeros(vec_size, dtype=np.float32)
    start = timer()
    c = power(a, b)
    duration = timer() - start
    print(duration)


if __name__ == '__main__':
    main()
