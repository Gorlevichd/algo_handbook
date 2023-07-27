def ad_market(n, click_array, price_array):
    revenue = 0
    click_array = sorted(click_array, reverse=True)
    price_array = sorted(price_array, reverse=True)
    for i in range(n):
        revenue += click_array[i] * price_array[i]
    return revenue


if __name__ == "__main__":
    n = int(input())
    price_list = map(int, input().split())
    click_list = map(int, input().split())
    print(ad_market(n, click_list, price_list))