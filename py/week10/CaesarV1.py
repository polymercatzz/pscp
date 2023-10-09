"""CaesarV1"""
def main(num, word):
    """CaesarV1"""
    result = ""
    letter_upper = [chr(ord("A") + i) for i in range(26)]
    letter_lower = [chr(ord("a") + i) for i in range(26)]
    for i in word:
        if i.islower():
            result += (letter_lower[(letter_lower.index(i)+num)%26])
        elif i.isupper():
            result += (letter_upper[(letter_upper.index(i)+num)%26])
        else:
            result += i
    print(result)
main(int(input()), input())
