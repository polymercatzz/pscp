"""Diginity"""
def main():
    """Diginity"""
    result = 0
    while True:
        num = input()
        if num == "0":
            break
        while len(num) > 1:
            result = 0
            for i in num:
                result += int(i)
            num = str(result)
        if len(num) == 1:
            result = num
        print(result)

main()
