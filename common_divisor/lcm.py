def gcd(a, b):
    if (a == 0) or (b == 0):
        return max(a, b)
    if a >= b:
        return gcd(a % b, b)
    return gcd(a, b % a)


def lcm(a, b):
    return (a * b) // gcd(a, b)


if __name__ == "__main__":
    a_, b_ = map(int, input().split())
    print(int(lcm(a_, b_)))