"""[Recommend] Elo"""
def main():
    """[Recommend] Elo"""
    ra_ = int(input())
    rb_ = int(input())
    word = input()
    ea_ = 1/(1+10**((rb_-ra_)/400))
    eb_ = 1-ea_
    if word == "A":
        print("%.2f"%ea_)
    else:
        print("%.2f"%eb_)

main()
