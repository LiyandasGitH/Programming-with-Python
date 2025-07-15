emoticon = "v.v" # global variable


def main():
    global emoticon # can modify value of variable as side effect
    say("Is anyone there?")
    emoticon = ":D"
    say("Oh, hi!")



def say(phrase):
    print(phrase + " " + emoticon)


main()
