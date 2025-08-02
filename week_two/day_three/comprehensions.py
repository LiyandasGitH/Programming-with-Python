'''
def main():
    counts = {}
    words = get_words("notes.txt")
    lowercase_words = [word.lower() for word in word if len(word) > 4]

    for word in lowercase_words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    save_counts(counts)
main()
'''

def main():
    words = get_words("notes.txt")
    lowercase_words = [word.lower() for word in word if len(word) > 4]

    counts = {words: lowercase_words.count(word) for word in lowercase_words}
    save_counts(counts)

main()
