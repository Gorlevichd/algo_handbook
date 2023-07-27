def string_creator(fifty, twenty, ten, five, one):
    string = "50 " * fifty + "20 " * twenty + "10 " * ten + "5 " * five + "1 " * one
    return string.strip()

def optimal_change(money):
    fifty = money // 50
    money -= 50 * fifty
    twenty = (money) // 20
    money -= 20 * twenty
    ten = (money) // 10
    money -= 10 * ten
    five = (money) // 5
    money -= 5 * five
    print(fifty + twenty + ten + five + money)
    print(string_creator(fifty, twenty, ten, five, money))


if __name__ == "__main__":
    money_ = int(input())
    optimal_change(money_)