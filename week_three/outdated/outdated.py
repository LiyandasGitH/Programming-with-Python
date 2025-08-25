

months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

def main():
    while True:
        date_entered = input("Date: ").strip()

        try:
            if "," in date_entered:
                month_day, year = date_entered.split(",")
                month_name, day = month_day.strip().split(" ")
                month = months.get(month_name)
                month = int(month)
                day = int(day)
                year = int(year)

            elif "/" in date_entered:
                month, day, year = date_entered.split("/")
                month = int(month)
                day = int(day)
                year = int(year)

            else:
                return ValueError

            if not(1 <= month <= 12 and 1 <= day <= 31):
                return ValueError

            # make year have 4 digits, month have 2 and day have 2
            print(f"{year:04d}-{month:02d}-{day:02d}")
            break

        except ValueError:
            continue
        except KeyError:
            continue



if __name__ == "__main__":
    main()

'''
def main():
    while True:
            # date = input("Date: ").strip()
        try:



        except ValueError:


if __name__ == "__main__":
    main()
'''

