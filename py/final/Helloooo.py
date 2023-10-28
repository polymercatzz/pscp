"""Helloooo"""
def main(word):
    """Helloooo"""
    last = "aeiouAEIOU"
    for i, letter in enumerate(word[-1::-1]):
        if letter in last:
            last = letter
            posi = len(word)-i
            break
    if last != "aeiouAEIOU":
        print(word[:posi-1]+last*4+word[posi:])
    else:
        print(word)
main(input())
