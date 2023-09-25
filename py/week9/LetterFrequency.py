"""LetterFrequency"""
def main(word):
    """LetterFrequency"""
    result = {}
    ans = []
    for i in word:
        i = i.lower()
        if i.isalpha():
            result[i] = result.get(i, 0) + 1
    for many in result.items():
        ans.append(many)
    ans.sort(key=lambda x: x[1], reverse=True)
    print(ans[0][0])
main(input())
