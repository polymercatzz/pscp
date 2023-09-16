# "Triangle I"
# def main():
#     "Triangle I"
#     stick_1 = float(input())
#     stick_2 = float(input())
#     stick_3 = float(input())
#     if stick_1 > stick_2 and stick_1 > stick_3:
#         dis = stick_1**2-(stick_2**2+stick_3**2)
#     elif stick_2 > stick_1 and stick_2 > stick_3:
#         dis = stick_2**2-(stick_1**2+stick_3**2)
#     else:
#         dis = stick_3**2-(stick_1**2+stick_2**2)
#     if abs(dis) <= 0.01:
#         print("Yes")
#     else:
#         print("No")

# main()
#เดาว่าน่าจะติดตรง0 00 1 != 1000 เดานะ

def main():
    # num1 = int(input())
    # num2 = int(input())
    # num3 = int(input())

    num1 = str(input())
    num2 = str(input())
    num3 = str(input())

    l3_num1 = str(num1) + str(num2) + str(num3)
    l3_num2 = str(num1) + str(num3) + str(num2)
    l3_num3 = str(num2) + str(num1) + str(num3)
    l3_num4 = str(num2) + str(num3) + str(num1)
    l3_num5 = str(num3) + str(num1) + str(num2)
    l3_num6 = str(num3) + str(num2) + str(num1)

    # print(l3_num1)
    # print(l3_num2)
    # print(l3_num3)
    # print(l3_num4)
    # print(l3_num5)
    # print(l3_num6)

    ans = compare(l3_num1, l3_num2)
    ans = compare(l3_num3, ans)
    ans = compare(l3_num4, ans)
    ans = compare(l3_num5, ans)
    ans = compare(l3_num6, ans)

    print(ans)


def compare(x, y):
    if int(x) > int(y):
        return x
    else:
        return y
    
main()
