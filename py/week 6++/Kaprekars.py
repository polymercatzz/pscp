"""Kaprekars"""
def maknoi(word):
    """find kamak kanoi"""
    num = str(word//1000)
    num2 = str((word%1000)//100)
    num3 = str((word%100)//10)
    num4 = str(word%10)
    if num > num2:
        num, num2 = num2, num
    if num > num3:
        num, num3 = num3, num
    if num > num4:
        num, num4 = num4, num
    if num2 > num3:
        num2, num3 = num3, num2
    if num2 > num4:
        num2, num4 = num4, num2
    if num3 > num4:
        num3, num4 = num4, num3
    return int(num+num2+num3+num4), int(num4+num3+num2+num)
def main():
    """Kaprekars"""
    num = int(input())
    count = 0
    while num != 6174:
        kanoi, kamak = maknoi(num)
        num = kamak-kanoi
        count += 1
    print(count)
main()
