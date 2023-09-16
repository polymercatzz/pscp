"""[Midterm 2021] iPhone 13 Again"""
def main():
    """[Midterm 2021] iPhone 13 Again"""
    word = input()
    size = input()
    result = 0
    if word == "iPhone 13 mini":
        result += 25900
    elif word == "iPhone 13":
        result += 29900
    elif word == "iPhone 13 Pro":
        result += 38900
    elif word == "iPhone 13 Pro Max":
        result += 42900
    else:
        result = "Not Available"
    if size == "128 GB" and result != "Not Available":
        result += 0
    elif size == "256 GB" and result != "Not Available":
        result += 4000
    elif size == "512 GB" and result != "Not Available":
        result += 12000
    elif size == "1 TB" and result >= 38900:
        result += 20000
    else:
        result = "Not Available"
    print(result)
main()
