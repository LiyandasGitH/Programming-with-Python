SHOWS = [
    " Avater: the last airbender",
    "Ben 10",
    "Arthur",
    " Spongebob Sqaurepants",
    "Phineas and ferb",
    "Kim possible",
    "Jimmy Neutron ",
    "the Proud family"
]


def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.title().strip())


    print(', '.join(cleaned_shows))


main()
