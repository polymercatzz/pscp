"""MissingCard"""
def main():
    """MissingCard"""
    list_card = []
    for i in ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']:
        for j in ['S', 'H', 'D', 'C']:
            list_card.append(i+j)
    for _ in range(51):
        list_card.remove(input())
    print(*list_card)
main()
