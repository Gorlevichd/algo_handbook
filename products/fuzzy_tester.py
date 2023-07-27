import numpy as np
import time
from biggest_elements_fast import max_pairwise_product_fast
from biggest_elements_slow import max_pairwise_product

for i in range(10000):
    n = int(np.random.randint(2, 2 * (10 * 5)))
    print("Test:", str(i))
    print(n)
    arr = list(map(int, np.random.randint(0, 2 * (10 ** 3), size = n)))

    start = time.time()
    result_fast = max_pairwise_product_fast(n, arr)
    end = time.time()
    print("Time elapsed, fast:", end - start)
    print("Result, fast:", result_fast)

    start = time.time()
    result_slow = max_pairwise_product(n, arr)
    end = time.time()
    print("Time elapsed, slow:", end - start)
    print("Result, slow:", result_slow)

    assert result_fast == result_slow
    print("OK")
    print("-------")



