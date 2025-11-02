import re



def main():
    print(parse(input("HTML: ")))


def parse(s):
# True - <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
# True - <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# False - <iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>
    # https://youtu.be/xvFZjo5PgG0
    match = re.search(r'.+src="https?://(?:www\.)?youtube\.com/embed/(.+?)"', s)
    if match:
        link = "https://youtu.be/" + match.group(1)
        return link

    else:
        return None
    #match = re.search(r"^https?://?(?:www\.)?youtube\.com/embed/(a-zA-Z0-9)"$, s, reIGNORECASE):



...


if __name__ == "__main__":
    main()
