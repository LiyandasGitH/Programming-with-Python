

def main():
    file_name = input("Enter the name of the file here: ").strip().lower()
    media_type(file_name)

def media_type(name):
    # use same logic as "startswith() but opposite
    if name.endswith(".gif"):
        print("image/gif")
    elif name.endswith(".jpg") or name.endswith(".jpeg"):
        print("image/jpeg")
    elif name.endswith(".png"):
        print("image/png")
    elif name.endswith(".pdf"):
        print("application/pdf")
    elif name.endswith(".txt"):
        print("text/plain")
    elif name.endswith(".zip"):
        print("file/zip")
    else:
        print("application/octet-stream")

main()


# list of common media types
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types/Common_types

