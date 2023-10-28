"""Socks"""
def main(word):
    """Socks"""
    result = []
    dict_word = {}
    for i in word:
        dict_word[i] = dict_word.get(i, 0)+1
    for key, value in sorted(dict_word.items()):
        if (key*2+" ")*(value//2) != "":
            result.extend(((key*2+" ")*(value//2)).split(" "))
            result.remove("")
    if result:
        print(*result)
        print(len(result))
    else:
        print("None")
        print(0)
main(input())
