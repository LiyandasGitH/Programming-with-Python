import re
#.#.#.#

# 232.321.232.321


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # cancel out leading zeros test
    valid = re.search(r"^(0|[1-9][0-9]{0,2})\."
                      r"(0|[1-9][0-9]{0,2})\."
                      r"(0|[1-9][0-9]{0,2})\."
                      r"(0|[1-9][0-9]{0,2})$", ip)
    if valid:
        for i in range(1, 5):
            if int(valid.group(i)) > 255:
                return False
        return True
    else:
        return False


...


if __name__ == "__main__":
    main()
