def gcd_backwards_fast(a, b, n):
    a_new = a + b
    if a_new <= n:
        return gcd_backwards_fast(a_new, a, n)
    if a % a == b:
        return [a, a]
    return [b, a]

if __name__ == "__main__":
    n_ = int(input())
    print(*gcd_backwards_fast(1, 0, n_))
