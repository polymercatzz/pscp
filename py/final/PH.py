"""PH"""
def main(ph_):
    """PH"""
    if ph_ < 0 or ph_ > 14:
        print("error")
    elif ph_ > 7:
        print("akaline")
    elif ph_ < 7:
        print("acidic")
    else:
        print("neutral")
main(float(input()))
