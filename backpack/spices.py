def find_max(relative_list):
    current_max = 0
    current_index = 0
    for i, relative_price in enumerate(relative_list):
        if relative_price > current_max:
            current_max = relative_price
            current_index = i
    return current_max, current_index


def optimal_spices(capacity, relative_list, weight_list):
    value = 0
    for _ in range(len(relative_list)):
        max_price, max_index = find_max(relative_list)
        take_amount = min(capacity, weight_list[max_index])
        capacity -= take_amount
        value += take_amount * max_price
        del relative_list[max_index]
        del weight_list[max_index]
        if capacity == 0 or len(relative_list) == 0:
            return value


if __name__ == "__main__":
    n, capacity = map(int, input().split())
    price_list = []
    weight_list = []
    relative_list = []
    for i in range(n):
        price, weight = map(int, input().split())
        price_list.append(price)
        weight_list.append(weight)
        relative_list.append(price / weight)
    print(optimal_spices(capacity, relative_list, weight_list))
