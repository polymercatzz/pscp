"""[Recommended] RunGame"""
def main(dot):
    """[Recommended] RunGame"""
    result = abs(dot[0])
    for i, key in enumerate(dot[1:-1]):
        result += abs(key-dot[i])
    print(result)
main(list(map(int, input().split()))+[0])
