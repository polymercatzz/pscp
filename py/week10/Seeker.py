"""Seeker"""
def main():
    """Seeker"""
    word = input()
    num = "0"
    result = 0
    for i in word:
        if i.isnumeric():
            num += i
        else:
            result += int(num)
            num = "0"
    print(result+int(num))
main()
