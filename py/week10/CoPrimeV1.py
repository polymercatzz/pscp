"""CoPrimeV1"""
def main(num1, num2):
    """CoPrimeV1"""
    while num2 != 0:
        num1, num2 = num2, num1%num2
    if num1 == 1:
        print("YES")
    else:
        print("NO")
    print(num1)
main(int(input()), int(input()))
