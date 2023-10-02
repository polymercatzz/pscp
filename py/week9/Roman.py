"""Roman"""
def main(word):
    """Roman"""
    roman = {"M":1000, "D":500, "C":100, "L":50, "X":10, \
            "V":5, "I":1}
    result = 0
    for i, letter in enumerate(word):
        if word[i] == word[-1]:
            result += roman.get(letter)
        elif roman.get(word[i]) >= roman.get(word[i+1]):
            result += roman.get(letter)
        else:
            result -= roman.get(letter)
    print(result)
main(input())
