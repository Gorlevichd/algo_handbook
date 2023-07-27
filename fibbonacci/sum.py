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


def last_number_fibbonacci(number):
    period = 60
    reduced = number % period
    return fibbonacci_number(reduced) % 10


if __name__ == "__main__":
    n = int(input())
    result = last_number_fibbonacci(n + 2) - 1
    if result < 0:
        print(10 + result)
    else:
        print(result)