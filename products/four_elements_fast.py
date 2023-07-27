def multiply_list(array):
    product = array[0]
    for number in array[1:]:
        product *= number
    return product

def four_elements_product_max(n, array):
    array.sort()
    four_biggest = array[-4:]
    four_lowest = array[:4]
    pos_top = multiply_list(four_biggest)
    neg_top = multiply_list(four_lowest)
    mix_top = multiply_list(four_biggest[-2:] + four_lowest[:2])
    return max((pos_top, neg_top, mix_top))

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(four_elements_product_max(n, arr))