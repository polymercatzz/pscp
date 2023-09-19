"""FourDirections"""
def main(line1="", line2="", line3="", line4=""):
    """main"""
    direct = input()
    print("  *   "*len(direct))
    for i in direct:
        if i == "U":
            line1 += " ***  "
            line2 += "* * * "
            line3 += "  *   "
            line4 += "  *   "
        elif i == "D":
            line1 += "  *   "
            line2 += "* * * "
            line3 += " ***  "
            line4 += "  *   "
        elif i == "L":
            line1 += " *    "
            line2 += "***** "
            line3 += " *    "
            line4 += "  *   "
        elif i == "R":
            line1 += "   *  "
            line2 += "***** "
            line3 += "   *  "
            line4 += "  *   "
    print(line1, line2, line3, line4, sep="\n")
main()
