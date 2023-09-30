"""BreachTheDoor"""
def main(word):
    """BreachTheDoor"""
    word = word.split(" ")
    result = []
    for test in word:
        if len(test) > 6:
            word_test = ""
            for i in test:
                if i.isalpha():
                    word_test += i
            if len(word_test) > 6:
                result.append(word_test)
    print(*result)
main(input())
