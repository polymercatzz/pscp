"""Easy Histogram"""
def main(word):
    """Easy Histogram"""
    letters = []
    for i in word:
        if i.isalpha() and i in word:
            count = word.count(i)
            word = word.replace(i, "")
            letters.append(i+" = %d"%count)
    letters.sort(key=lambda x: (x.lower(), x.isupper()))
    print(*letters, sep="\n")
main(input())
