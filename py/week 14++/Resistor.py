"""Resistor"""
def main(color1, color2, color3, color4):
    """Resistor"""
    line12 = {"Black":"0", "Brown":"1", "Red":"2", "Orange":"3", "Yellow":"4", "Green":"5", \
            "Blue":"6", "Purple":"7", "Grey":"8", "White":"9"}
    line3 = {"Black":1, "Brown":10, "Red":100, "Orange":1000, "Yellow":10000, "Green":100000, \
            "Blue":1000000, "Purple":10000000, "Gold":0.1, "Silver":0.01}
    line4 = {"Brown":0.01, "Red":0.02, "Green":0.005, \
            "Blue":0.0025, "Purple":0.001, "Grey":0.0005, "Gold":0.05, "Silver":0.1}
    result = [line12.get(color1), line12.get(color2), line3.get(color3), line4.get(color4)]
    if None in result:
        print("Error")
    else:
        print("%.4f"%(int(result[0]+result[1])*result[2]*(1-result[3])))
        print("%.4f"%(int(result[0]+result[1])*result[2]*(1+result[3])))
main(input(), input(), input(), input())
