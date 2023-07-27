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


def difference_fibbonacci(number1, number2):
    difference = last_number_fibbonacci(number1 + 2) - last_number_fibbonacci(number2 + 1)
    if difference < 0:
        return (10 + difference)
    return difference


if __name__ == "__main__":
    m, n = map(int, input().split())
    print(difference_fibbonacci(n, m))