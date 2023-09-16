"""Key"""
def main():
    """Key"""
    num = input()
    sum_13 = 0
    for i in num:
        sum_13 += int(i)
    sum_13 += (10*int(num[-3:]))
    if sum_13 < 1000:
        sum_13 += 1000
    print(str(sum_13)[-4:])
main()
