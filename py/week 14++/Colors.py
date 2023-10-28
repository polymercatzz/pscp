"""Colors"""
def main(color):
    """Colors"""
    all_color = {"BlueYellow":"Green", "RedYellow":"Orange", "BlueRed":"Violet", "Red"*2:"Red", \
                "Blue"*2:"Blue", "Yellow"*2:"Yellow"}
    print(all_color.get(color[0]+color[1], "Error"))
main(sorted([input() for _ in range(2)]))
