import re

locations = {"+1": "Umited States and Canada", "+62": "Indonesia", "+505": "Nicaragua"}

def main():
    pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    # pattern of international numbers
    # ?P<> - allows to name specific groups
    number = input("Numbers: ")

    match = re.search(pattern, number)
    if match:
        country_code = match.group("country_code")
        print(locations[country_code])
    else:
        print("Invalid")



main()
