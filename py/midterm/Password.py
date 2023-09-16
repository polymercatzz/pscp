"""Password"""
import math
def main():
    """Password"""
    word = input()
    pool = 0
    lower = True
    uper = True
    num = True
    special = True
    for i in word:
        if i.isupper() and uper:
            uper = False
            pool += 26
        elif i.islower() and lower:
            lower = False
            pool += 26
        elif i.isnumeric() and num:
            pool += 10
            num = False
        elif i in "~`!@#$%^&*()_-+=[]{}|\\/:;\"\'<>.,?" and special:
            pool += 32
            special = False
    entropy = int(math.log2(pool**len(word)))
    print(entropy)
    if entropy < 28:
        print("Very Weak")
    elif entropy <= 35:
        print("Weak")
    elif entropy <= 59:
        print("Reasonable")
    elif entropy <= 127:
        print("Strong")
    else:
        print("Very Strong")
main()
