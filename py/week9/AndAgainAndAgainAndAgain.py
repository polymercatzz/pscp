"""AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
def main(word):
    """AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
    word = word.split(" ")
    result = []
    for word_list in word:
        find = 0
        word_result = ""
        count = 1
        for i in word_list:
            if i.isalpha() and i.lower() in "AEIOUaeiou":
                find += 1
                word_result += i
            elif i.isalpha():
                word_result += i
            if find >= 2 and count == len(word_list):
                result.append(word_result)
            count += 1
    result.sort()
    if not result:
        result.append("Nope")
    print(*result, sep="\n")
main(input())
