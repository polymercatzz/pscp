"""[Midterm 2021] Squid Game"""
def main():
    """[Midterm 2021] Squid Game"""
    power_a = 0
    power_b = 0
    for _ in range(10):
        power_a += int(input())
    for _ in range(10):
        power_b += int(input())
    if power_a > power_b:
        print('B')
    elif power_a < power_b:
        print('A')
    else:
        print("AB")
main()
