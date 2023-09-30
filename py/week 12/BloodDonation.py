"""BloodDonation"""
def main(age, weight, times, licen=False):
    """BloodDonation"""
    if age == 17 or 60 <= age <= 70:
        if input() == "False":
            licen = True
    age_check = 17 <= age <= 70
    if licen:
        age_check = False
    weight_check = weight >= 45
    time_check = True
    if times == 0 and age > 55:
        time_check = False
    if age_check and weight_check and time_check:
        print("Yes")
    else:
        print("No")
main(int(input()), int(input()), int(input()))
