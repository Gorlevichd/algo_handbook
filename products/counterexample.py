if __name__ == "__main__":
    n = int(input())
    if n > 5:
        print("Yes")
        counterexample = [n] + [i for i in range(1, n)]
        print(*counterexample)
    else:
        print("No")