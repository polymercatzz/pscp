"""Tuple's Sad life"""
def main():
    """Tuple's Sad life"""
    word = input().split(" ")
    find_ = input()
    posi = word.index(find_)
    print(((str(posi)+" ")*word.count(find_)+"\n")*word.count(find_), end="")
main()
