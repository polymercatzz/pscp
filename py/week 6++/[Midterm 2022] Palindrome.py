"""[Midterm 2022] Palindrome"""
def main(num, time):
    """[Midterm 2022] Palindrome"""
    for _ in range(num):
        if len(time) == 4:
            if time[0] > time[3]:
                time = time[:3]+time[0]
            else:
                time = time[:2]+str(int(time[2])+1)+time[0]
            if time[2] == "6":
                time = str(int(time[0])+1)+":0"+str(int(time[0])+1)
            if len(time) > 4:
                time = "10:00"
        if len(time) == 5:
            if int(time[-4::-1]) > int(time[3:]):
                time = time[:3]+time[-4::-1]
            else:
                time = str(int(time[:2])+1)+":"+str(int(time[:2])+1)[::-1]
            if 15 < int(time[:2]) < 20:
                time = "20:02"
            if int(time[:2]) == 24:
                time = "0:00"
        print(time)
main(int(input()), input())
