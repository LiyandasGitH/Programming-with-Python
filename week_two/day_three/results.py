results = ["Mario", "Luigi", "Princess", "Yoshi", "Koopa Troopa", "Toad", "Bowser", "Donkey Kong Jr."]

results.remove("Bowser")
# insert() add at the index of choice in list
results.insert(0, "Bowser")
# reverse() starts list back to front
results.reverse()

'''
results = ["Mario", "Luigi"]
# append() adds to our list
results.append("Princess")
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")

results.append(["Bowser", "Donkey Kong Jr."])
# remove() removes list in list
results.remove(["Bowser", "Donkey Kong Jr."])
# extend() adds new list to original list
results.extend(["Bowser", "Donkey Kong Jr."])
'''
print(results)
