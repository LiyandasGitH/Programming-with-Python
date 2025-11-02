import sys
import csv


def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")


    filename = sys.argv[1]
    namefile = sys.argv[2]

    if not filename.endswith("csv"):
        sys.exit("Not a CSV file")


    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            with open(namefile, "w") as file2:
                writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in reader:
                    row["first"] = row.pop("name")
                    last_name, first_name = row["first"].split(", ")
                    row["first"] = first_name
                    row["last"] = last_name
                    writer.writerow(row)


    except FileNotFoundError as e:
        sys.exit(f"Could not read {e}")



if __name__ == "__main__":
    main()
