"""FourDirections"""
def main():
    word = input()
    print("  *  ")*len(word)
    for i in word:
        if i == "U"