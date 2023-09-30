"""PrasomSib"""
def main(num):
    """PrasomSib"""
    num = list(num)
    count = 0
    for i in range(len(num)):
        result = 0
        order = i
        while result < 10:
            result += int(num[order])
            order += 1
            if order > len(num)-1:
                break
        if result == 10:
            count += 1
    print(count)
main(input())
