"""ham"""
def main(word1, word2):
    """ham"""
    print(len([i for i in range(len(word1)) if word1[i] != word2[i]]))
main(input(), input())
