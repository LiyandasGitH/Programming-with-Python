import sys
import csv
from tabulate import tabulate


def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")


    filename = sys.argv[1]


    if not filename.endswith("csv"):
        sys.exit("Not a CSV file")

    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            headers = reader.fieldnames
            if headers is None:
                sys.exit("CSV file is invalid")


            if "Sicilian Pizza" in headers:
                pizza_key = "Sicilian Pizza"
            elif "Regular Pizza" in headers:
                pizza_key = "Regular Pizza"
            else:
                sys.exit("Pizza column not found")

            table = []
            for row in reader:
                table.append({
                    pizza_key: row[pizza_key],
                    "Small": row["Small"],
                    "Large": row["Large"]
                })

            print(tabulate(table, headers="keys", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")
    except KeyError:
        sys.exit("One or more expected columns missing")



if __name__ == "__main__":
    main()


