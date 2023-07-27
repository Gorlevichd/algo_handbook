def string_creator(tens, fifths, ones):
    string = "10 " * tens + "5 " * fifths + "1 " * ones
    return string.strip()

def possible_change(tens, fifths, ones):
    result = []
    for ten_n in range(tens + 1):
        for fifth_n in range(fifths + 2 * ten_n + 1):
                result.append(
                     (tens - 1 * ten_n,
                      fifths + 2 * ten_n - 1 * fifth_n, 
                      ones + 5 * fifth_n)
                      )
    return result


if __name__ == "__main__":
    money_ = int(input())
    tens = money_ // 10
    fifths = (money_ % 10) // 5
    ones = (money_ % 5)
    results = possible_change(tens, fifths, ones)
    print(len(results))
    for result in results:
         print(result[0] + result[1] + result[2], string_creator(result[0], result[1], result[2]))