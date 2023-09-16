"time"
def main():
    "time"
    time_ = int(input())
    if time_ < 864000000:
        second = time_
        min_ = second//60
        second = second%60
        hour = min_//60
        min_ = min_%60
        day = hour//24
        hour = hour%24
        print("%04d:%02d:%02d:%02d"%(day, hour, min_, second))
    else:
        print("ERR_:__:__:__")
main()
