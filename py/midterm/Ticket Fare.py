"""Ticket Fare"""
def main():
    """Ticket Fare"""
    num_n = int(input())
    num_a = int(input())
    num_b = int(input())
    num_c = int(input())
    num_d = int(input())
    num_e = int(input())
    num_f = int(input())
    num_g = int(input())
    price = 0
    if num_f > num_g:
        num_f, num_g = num_g, num_f
    sta = abs(num_g-num_f)
    if num_g <= num_n:
        price += num_b
        sta -= num_a
        if sta >= num_c:
            price += num_d*num_c
            sta -= num_c
        elif sta > 0:
            price += num_d*sta
            sta = 0
        if sta > 0:
            price += num_e*sta
        print(price)
    else:
        print("Error")
main()
