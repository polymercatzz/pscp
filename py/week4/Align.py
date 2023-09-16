"""Align"""
def main():
    """Align"""
    long = int(input())
    r_l_c = input()
    word = input()
    space = long-len(word)
    if r_l_c == "left":
        print(word+space*" ")
    elif r_l_c == "center":
        maigang = space%2
        space = space//2
        print((space+maigang)*" "+word+space*" ")
    else:
        print(space*" "+word)
main()
