"""Parity"""
def main():
    """Parity"""
    num = input()
    word = input()
    result = 0
    for i in num:
        result += int(i)
    if word == "Even":
        if result%2 == 0:
            print(num+"0")
        else:
            print(num+"1")
    elif word == "Odd":
        if result%2 == 0:
            print(num+"1")
        else:
            print(num+"0")
main()
