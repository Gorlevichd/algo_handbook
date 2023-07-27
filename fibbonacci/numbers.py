def fibbonacci_number(n):
    if n <= 1:
        return n
    fibbonacci_array = [0] * n
    for i in range(n):
        if i <= 1:
            fibbonacci_array[i] = i
        else:
            fibbonacci_array[i] = fibbonacci_array[i - 1] + fibbonacci_array[i - 2]
    return fibbonacci_array[n - 1] + fibbonacci_array[n - 2]


if __name__ == "__main__":
    n = int(input())
    print(fibbonacci_number(n))