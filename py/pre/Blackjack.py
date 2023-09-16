"Blackjack"
def main():
    "main"
    mcard = int(input())
    result = 0
    card_a = False
    for mcard in range(mcard):
        card = input()
        if card == "A":
            card_a = True
            result += 1
        elif card == "J" or card == "Q" or\
card == "K":
            result += 10
        else:
            result += int(card)
    if card_a and result+10 <= 21:
        result += 10
    print(result)
main()
