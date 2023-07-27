from copy import deepcopy
import math


def two_elements(array):
    a = deepcopy(array)
    n = len(array)
    ## Base
    if n == 2:
        if a[0] > a[1]:
            return (0, 1)
        return (1, 0)
 
    ## Recursion
    m = []
    w = []
    for i in range(n // 2):
        if a[2 * i] < a[2 * i + 1]:
            temp = a[2 * i + 1]
            a[2 * i + 1] = a[2 * i]
            a[2 * i] = temp
            m.append(1)
        else:
            m.append(0)
        w.append(a[2 * i])

    j, k = two_elements(w)
    j_swap = m[j]
    k_swap = m[k]
    j = 2 * j
    k = 2 * k
    if a[j + 1] > a[k]:
        k = j + 1
        k_swap = 0 - j_swap
    return (j + j_swap, k + k_swap)

if __name__ == "__main__":
    length = int(input())
    arr = list(map(int, input().split()))
    array_pad = [0] * (2 ** math.ceil(math.log2(len(arr))))
    for i, _ in enumerate(arr):
        array_pad[i] = arr[i]
    j_, k_ = two_elements(array_pad)
    print(arr[j_] * arr[k_])