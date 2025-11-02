import re

def main():
    code = input("Hexdecimal colour code: ")
    # begins w/ "#"
    # composed of 6 characters
        # 0-9 & A-F


    pattern = r"^#[a-fA-F0-9]{6}$"
    match = re.search(pattern, code)
    if match:
        print(f"Valid. Matches with {match.group()}")
    else:
        print("Invalid")




main()
