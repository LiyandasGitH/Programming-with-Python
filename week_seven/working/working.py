import re



def main():
    print(convert(input("Hours: ")))


def convert(s):
    # 9 AM to 5 PM -> 09:00 to 17:00
    # 9:00 AM to 5:00 PM -> 09:00 to 17:00
    # 10:30 PM to 8:20 AM -> 22:30 to 08:50
    #time = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2})? (AM|PM)$", s, re.IGNORECASE)
    time = re.search(
        r"^(\d{1,2})(?::(\d{2}))?\s+(AM|PM)\s+to\s+(\d{1,2})(?::(\d{2}))?\s+(AM|PM)$",
        s, re.IGNORECASE,
    )

    if not time:
        raise ValueError


    hour1, min1, midday1, hour2, min2, midday2 = time.groups()

    hour1 = int(hour1)
    hour2 = int(hour2)
    min1 = int(min1) if min1 else 0
    min2 = int(min2) if min2 else 0


    if min1 >= 60 or min2 >= 60:
        raise ValueError

    if midday1.upper() == "AM":
        if hour1 == 12:
            hour1 = 0

    elif midday1.upper() == "PM":
        if hour1 != 12:
            hour1 += 12

    if midday2.upper() == "AM":
        if hour2 == 12:
            hour2 = 0

    if midday2.upper() == "PM":
        if hour2 != 12:
            hour2 += 12

    return f"{hour1:02}:{min1:02} to {hour2:02}:{min2:02}"



if __name__ == "__main__":
    main()



'''
    if time:
        # ValueErrors
        if time.group(2):
            if int(time.group(2)) >= 60:
                raise ValueError
        if time.group(5):
            if int(time.group(5)) >= 60:
                raise ValueError

        # time1
        hour1 = int(time.group(1))
        if time.group(3) == "PM":
            hour1 += 12
        elif time.group(3) == "AM" and hour1 == 12:
            hour1 -= 12

        if time.group(2) == None:
            time1 = f"{hour1:02}:00"
        else:
            time1 = f"{hour1:02}:{time.group(2)}"


        # time2
        hour2 = int(time.group(4))
        if time.group(6) == "PM":
            hour2 += 12
        elif time.group(6) == "AM" and hour2 == 12:
            hour2 -= 12

        if time.group(5) == None:
            time2 = f"{hour2:02}:00"
        else:
            time2 = f"{hour2:02}:{time.group(5)}"



        # return 24 hr format
        time = f"{time1} to {time2}"
        return time


    else:
        raise ValueError
'''
