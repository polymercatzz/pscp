"""WordSequence II"""
def main(word, word2):
    """WordSequence II"""
    for i in range(max(len(word), len(word2))+1):
        print(word2[:i]+word[i:])
main(input(), input())
