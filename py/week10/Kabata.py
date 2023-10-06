"""Kabata"""
def main(num):
    """Kabata"""
    for _ in range(num):
        word = input()
        if "baka" in word:
            print('no')
            continue
        word = word.replace("bakka", "")
        word = word.replace("ba", "")
        word = word.replace("ka", "")
        word = word.replace("ta", "")
        if word == "":
            print("yes")
        else:
            print("no")
main(int(input()))
