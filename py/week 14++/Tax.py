"""Tax"""
def main(years, car_cc):
    """Tax"""
    price = 0
    check_y = {6:0.9, 7:0.8, 8:0.7, 9:0.6}
    check_cc = [[600, min(600, car_cc), 0.5], [1800, min(1200, car_cc-600), 1.5], \
                [1800, car_cc-1800, 4]]
    for i in range(3):
        if car_cc <= check_cc[i][0]:
            price += check_cc[i][1]*check_cc[i][2]
            break
        else:
            price += check_cc[i][1]*check_cc[i][2]
    if years >= 6:
        price *= check_y.get(years, 0.5)
    print("%.2f"%price)
main(int(input()), int(input()))
