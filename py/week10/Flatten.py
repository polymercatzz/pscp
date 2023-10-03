"""Flatten"""
import json
def main(word):
    """Flatten"""
    word = json.loads(word)
    result = []
    for i in word:
        if isinstance(i, list):
            word.extend(i)
        else:
            result.append(i)
    result.sort(reverse=True)
    print(result)
main(input())
