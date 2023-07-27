def string_sum(length, a_str, b_str):
    result_string = ""
    for i in range(length):
        result_string += a_str[i] + b_str[i]
    print(result_string)


if __name__ == "__main__":
    length = int(input())
    a_str = str(input())
    b_str = str(input())

    string_sum(length, a_str, b_str)