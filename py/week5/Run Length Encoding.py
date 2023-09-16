"""Run Length Encoding"""
def same_lett(word):
    """Run Length Encoding"""
    same_word = ""
    result = ""
    count = 1
    for i in word+" ":
        if i == same_word:
            count += 1
        else:
            result += str(count) + same_word
            same_word = i
            count = 1
    print(result[1:])
same_lett(input())
