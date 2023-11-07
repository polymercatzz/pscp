"""Guess"""
def main():
    """Guess"""
    ans = list(range(0, 101))
    while True:
        hint = input().split(" ")
        if hint == ["END"]:
            break
        dict_hint = {"YES":{"<":list(range(0, int(hint[1]))), \
                    ">":list(range(int(hint[1])+1, 101))}, \
                    "NO":{"<":list(range(int(hint[1]), 101)), ">":list(range(0, int(hint[1])+1))}}
        if hint[0] != "=":
            ans = set(ans) & set(dict_hint.get(hint[2]).get(hint[0]))
        else:
            if hint[2] == "NO":
                ans = set(ans) - {int(hint[1])}
            else:
                ans = set(ans) & {int(hint[1])}
    print(*sorted(ans))
main()
