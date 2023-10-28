"""Difference"""
import json
def main(lst1, lst2):
    """Difference"""
    result = {}
    for i in set(lst1+lst2):
        if abs(lst1.count(i)-lst2.count(i)) > 0:
            result[i] = abs(lst1.count(i)-lst2.count(i))
    if result:
        for i in sorted(result.items()):
            print(*i)
    else:
        print("ONAJI DAYO!")
main(json.loads(input()), json.loads(input()))
