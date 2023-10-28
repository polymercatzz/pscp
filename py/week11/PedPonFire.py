"""PedPonFire"""
def main(num):
    """PedPonFire"""
    pair = []
    result = {}
    for _ in range(num):
        duck = int(input())
        result[duck] = result.get(duck, 0)+1
    wpair = int(input())
    ans = 0
    for key in set(result.keys()):
        if key not in pair and wpair-key != key:
            ans += result.get(wpair-key, 0)*result.get(key)
        elif wpair-key == key:
            ans += sum([i for i in range(result.get(wpair-key, 0))])
        pair.append(wpair-key)
    print(ans)
main(int(input()))
