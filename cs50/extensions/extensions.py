ext = input("Enter file name> ").lower().strip()

image_ext = (".gif", ".jpg", ".jpeg", ".png")
app_ext = (".pdf",".zip")


if ext.endswith(".gif"):
    print("image/gif")
elif ext.endswith(".jpg"):
    print("image/jpeg")
elif ext.endswith(".jpeg"):
    print("image/jpeg")
elif ext.endswith(".png"):
    print("image/png")
elif ext.endswith(".pdf"):
    print("application/pdf")
elif ext.endswith(".zip"):
    print("application/zip")
elif ext.endswith(".txt"):
    print("text/plain")
else:
    print("application/octet-stream")