def main():
    user_time = input("What time is it? ")
    time = convert(user_time)

    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
         print("lunch time")
    elif 18.0 <= time <= 19.0:
         print("dinner time")


def convert(user_time):
        hours, minutes = user_time.split(":")
        hours = int(hours)
        minutes = int(minutes)

        return hours + minutes / 60

if __name__ == "__main__":
    main()

'''
def meal(time):
    if time <= 7:00 and time <= 8:00:
    print("breakfast time")
    if time <= 12:00 and time <=13:00:
    print("lunch time")
    if time <= 18:00 and time <=19:00:
    print("dinner time")
'''


