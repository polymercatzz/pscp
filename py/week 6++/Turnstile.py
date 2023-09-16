"""Turnstile"""
def main():
    """Turnstile"""
    turn = 0
    coin = False
    while True:
        word = input()
        if word == "END":
            break
        elif word == 'P' and coin:
            coin = False
            turn += 1
        elif word == "C":
            coin = True
    print(turn)
main()
