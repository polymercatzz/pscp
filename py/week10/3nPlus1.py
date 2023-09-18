"""3nPlus1"""
def main():
    """3nPlus1"""
    while True:
        result = 1
        num = int(input())
        if num == 0:
            break
        while num != 1:
            result += 1
            if num%2 == 0:
                num = num//2
            else:
                num = num*3+1
        print(result)
main()
