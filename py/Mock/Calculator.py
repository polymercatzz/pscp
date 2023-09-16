"""Calculator"""
def main():
    """how many press"""
    num = int(input())
    word = ""
    if num == 1:
        print(1)
    else:
        for i in range(1, num+1):
            word += str(i)+"+"
        print(len(word))
main()
