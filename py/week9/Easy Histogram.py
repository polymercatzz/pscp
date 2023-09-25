"""Easy Histogram"""
def main(word):
    """Easy Histogram"""
    result = {}
    ans = []
    for i in word:
        if i.isalpha():
            result[i] = result.get(i, 0) + 1
    for letter, many in result.items():
        ans.append(letter+" = "+str(many))
    ans.sort(key=lambda x: (x.lower(), x.isupper()))
    print(*ans, sep="\n")
main(input())
