
emojies = {
    ":1st_place_medal:": "🥇",
    ":2nd_place_medal:": "🥈",
    ":money_bag:": "💰",
    ":smile_cat:": "😸",
    ":thumbs_down:": "👎",
    ":thumbs_up:": "👍",
    ":raising_hands:": "🙌",
    ":raised_hand:": "✋",
    ":raised_fist:": "✊",
    ":raised_back_of_hand:": "🤚",
    ":earth_africa:": "🌍",
    ":earth_asia:": "🌏",
    ":earth_americas:": "🌎",
    ":globe_showing_europe_africa:": "🌍"
}

def main():
    emoji = input("Input: ").strip("_")
    output(emoji)

def output(emoji):
    if emoji in emojies:
        print(f"Output: {emojies[emoji]}")
    else:
        pass

main()


# https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias
