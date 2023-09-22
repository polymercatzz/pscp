"""GCD_v2"""
def main(num1, num2):
    """GCD_v2"""
    while num2 != 0:
        num1, num2 = num2, num1%num2
    print(num1)
main(int(input()), int(input()))
