"""HorizontalHistogram"""
def main(word):
    """HorizontalHistogram"""
    dict_letter = {}
    for i in word:
        dict_letter[i] = dict_letter.get(i, 0)+1
    dict_letter = dict(sorted(dict_letter.items(), key=lambda x: (x[0].isupper(), ord(x[0]))))
    for key, item in dict_letter.items():
        print(key, ":", end=" ")
        for i in range(1, item+1):
            if i % 5 == 1 and  i > 1:
                print("|", end="")
            print("-", end="")
        print()
main(input())
