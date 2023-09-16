"""spike"""
def main(num1, num2, num3, num4, num5):
    """spike"""
    num6 = int(input())
    num7 = int(input())
    num8 = int(input())
    if num1 >= num2 and num1 >= num3 and num1 >= num4 and num1 >= num5 and \
        num1 >= num6 and num1 >= num7 and num1 >= num8:
        print(num1)
    elif num2 >= num1 and num2 >= num3 and num2 >= num4 and num2 >= num5 and \
        num2 >= num6 and num2 >= num7 and num2 >= num8:
        print(num2)
    elif num3 >= num1 and num3 >= num2 and num3 >= num4 and num3 >= num5 and \
        num3 >= num6 and num3 >= num7 and num3 >= num8:
        print(num3)
    elif num4 >= num1 and num4 >= num2 and num4 >= num3 and num4 >= num5 and \
        num4 >= num6 and num4 >= num7 and num4 >= num8:
        print(num4)
    elif num5 >= num1 and num5 >= num2 and num5 >= num4 and num5 >= num3 and \
        num5 >= num6 and num5 >= num7 and num5 >= num8:
        print(num5)
    elif num6 >= num1 and num6 >= num2 and num6 >= num4 and num6 >= num5 and \
        num6 >= num3 and num6 >= num7 and num6 >= num8:
        print(num6)
    elif num7 >= num1 and num7 >= num2 and num7 >= num4 and num7 >= num5 and \
        num7 >= num6 and num7 >= num3 and num7 >= num8:
        print(num7)
    elif num8 >= num1 and num8 >= num2 and num8 >= num4 and num8 >= num5 and \
        num8 >= num6 and num8 >= num7 and num8 >= num3:
        print(num8)
main(int(input()), int(input()), int(input()), int(input()), int(input()))
