def gcd(a, b):
    if (a == 0) or (b == 0):
        return max(a, b)
    if a >= b:
        return gcd(a % b, b)
    return gcd(a, b % a)
    

if __name__ == "__main__":
    a_, b_ = map(int, input().split())
    print(gcd(a_, b_))