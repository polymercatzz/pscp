"""VerticalHistogram"""
def main(word):
    """VerticalHistogram"""
    dict_letter = {}
    for i in word:
        dict_letter[i] = dict_letter.get(i, 0)+1
    dict_letter = dict(sorted(dict_letter.items(), key=lambda x: (x[0].isupper(), ord(x[0]))))
    for i in range(max(dict_letter.values()), 0, -1):
        print("%03d"%i, end=" ")
        for value in dict_letter.values():
            if value >= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print("   ", *dict_letter.keys())
main(input())
