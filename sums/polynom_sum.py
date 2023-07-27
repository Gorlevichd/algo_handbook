def SumOfTwoPolynoms(power_a, a_coef, power_b, b_coef):
    if power_a >= power_b:
        for i in range(0, power_b + 1):
            a_coef[(len(a_coef) - len(b_coef)) + i] += b_coef[i]
        print(power_a)
        print(*a_coef)
    if power_b > power_a:
        for i in range(0, power_a + 1):
            b_coef[(len(b_coef) - len(a_coef)) + i] += a_coef[i]
        print(power_b)
        print(*b_coef)


if __name__ == "__main__":
    pow_a = int(input())
    a_cf = list(map(int, input().split()))
    pow_b = int(input())
    b_cf = list(map(int, input().split()))

    SumOfTwoPolynoms(pow_a, a_cf, pow_b, b_cf)