"Shorten"
def main():
    """Shorten"""
    word = ""
    while True:
        num = int(input())
        if num == -1:
            break
        else:
            word = word+str(num)
    for i in  len(word):
        sum = word[1+i] - word[0+i]
        if sum == 1:
main()
