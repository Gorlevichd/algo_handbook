def find_min(price_list):
    current_min = price_list[0]
    current_index = 0
    for i, price in enumerate(price_list):
        if price < current_min:
            current_min = price
            current_index = i
    return current_min, current_index


def diverse_souvenires(budget, price_list):
    amount = 0
    for _ in range(len(price_list)):
        min_price, min_index = find_min(price_list)
        if budget - min_price < 0:
            return amount
        budget = budget - min_price
        amount += 1
        del price_list[min_index]
        if len(price_list) == 0:
            return amount


if __name__ == "__main__":
    n, budget = map(int, input().split())
    price_list = []
    for i in range(n):
        price = int(input())
        price_list.append(price)
    print(diverse_souvenires(budget, price_list))
