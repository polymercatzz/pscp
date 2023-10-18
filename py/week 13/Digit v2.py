"""Digit v2"""
def main(word):
    """Digit v2"""
    result = 0
    dict_word = {"hundred":3, "thousand":4, "zero":1, "one":1, "two":1, "three":1, \
                "four":1, "five":1, "six":1, "seven":1, "eight":1, "nine":1}
    for i in word:
        if result < dict_word.get(i, 2):
            result = dict_word.get(i, 2)
    print(result)
main(input().split(" "))
