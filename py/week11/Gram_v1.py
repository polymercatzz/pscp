"""Gram_v1"""
def main(word):
    """Gram_v1"""
    result = [word[i:i+2] for i in range(len(word)-1)]
    print(max(result, key=result.count), result.count(max(result, key=result.count)), sep="\n")
main(input())
