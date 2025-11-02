import re


url = input("URL: ").strip()
# searching url for regular expression
if matches := re.search(r"^https?://?(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, reIGNORECASE):
    # (?:www\.) - no longer classified as group(1)
    print(f"Username:", matches.group(1))




'''
url = input("URL: ").strip()
# searching url for regular expression
matches = re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$", url, reIGNORECASE)
# ("www\.") classified as group(1) , (.+) classified as group(2)
if matches:
    print(f"Username:", matches.group(2))
'''


'''
url = input("URL: ").strip()

username =re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")
'''


'''
url = input("URL: ").strip()

username =url.removeprefix("https://twitter.com/")
print(f"Userame: {username}")
'''

'''
url = input("URL: ").strip()
username =url.replace("https://twitter.com/", "")
print(f"Userame: {username}")
'''


