"""[Recommended] Dart"""
def main(data):
    """[Recommended] Dart"""
    score = {2:5, 4:4, 6:3, 8:2, 10:1}
    result = 0
    for num in data:
        for key in score:
            if (num[0]**2+num[1]**2)**0.5 <= key:
                result += score[key]
                break
    print(result)
main([list(map(int, input().split())) for i in range(int(input()))])
