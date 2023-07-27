def find_three_elements(n, array):
    array.sort()
    three_biggest = array[-3:]
    two_lowest = array[:2]
    neg_top = two_lowest[0] * two_lowest[1] * three_biggest[-1]
    pos_top = three_biggest[0] * three_biggest[1] * three_biggest[2]
    if neg_top > pos_top:
        return neg_top
    else:
        return pos_top


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(find_three_elements(n, arr))