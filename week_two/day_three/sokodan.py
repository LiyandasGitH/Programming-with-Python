def main():
    history = []

    while True:
        action = input("Action: ")

        if action == "Undo" or action == "UNDO" or action == "undo":
            undone = history.pop()
            print(f"Undone: {undone}")
        elif action == "Restart" or action == "restart" or action == "RESTART":
            history.clear()
        else:
            history.append(action)
            print(history)
main()
