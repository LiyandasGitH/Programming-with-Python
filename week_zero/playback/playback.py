# Ask user for input
playback_input = input("Enter text here: ")

''' Use built in str.replace() function '''
# Replace each space w/ "..."
speed = playback_input.replace(" ", "...")
''' (" ") = sep=' '   '''
# Return at slower speed
print(speed)
