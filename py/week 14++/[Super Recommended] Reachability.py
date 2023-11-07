"""[Super Recommended] Reachability"""
import json
def main(node, word):
    """[Super Recommended] Reachability"""
    result = node.get(word)
    all_res = result.copy()
    while result:
        test = result.copy()
        for i in test:
            data = node.get(i)
            for j in data:
                if j not in all_res:
                    result.extend(j)
                    all_res.extend(j)
        result.pop(0)
    print(sorted(set(all_res+[word])))
main(json.loads(input().replace("'", '"')), input())
