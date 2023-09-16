"""Virus I"""
def main():
    """Virus I"""
    word = input()
    num = 0
    for _ in word:
        if _ == _.lower():
            num += 1
    print(num)
main()
