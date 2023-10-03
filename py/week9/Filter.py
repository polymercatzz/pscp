"""Filter"""
import json
def main(word, num):
    """Filter"""
    score = json.loads(word)
    result = []
    for key, item in score.items():
        if item >= num:
            result.append(key+"\t"+"%.2f"%item)
    result.sort()
    if not result:
        result.append("Nope")
    print(*result, sep="\n")
main(input(), float(input()))
