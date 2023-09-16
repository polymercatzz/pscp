"""Run Length Decoding"""
def main(word):
    """Run Length Decoding"""
    same = ""
    for i in word:
        if i.isnumeric():
            same = same+i
        else:
            print(int(same)*i, end="")
            same = ""
main(input())
