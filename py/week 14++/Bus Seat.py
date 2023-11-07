"""Bus Seat"""
def main(row, col, people):
    """Bus Seat"""
    for i in range(row, 0, -1):
        for j in range(col):
            seat = i+(j*row)
            print("XX" if seat == int(people) else "%02d"%seat, end=" ")
        print("" if i%2 == 0 else "\n")
main(int(input()), int(input()), input())
