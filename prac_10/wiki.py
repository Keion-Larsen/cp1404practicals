import wikipedia
search = input("Enter page title or search phrase: ")
while search != "":
    print(wikipedia.title(search))
    print(wikipedia.summary(search))
    print(wikipedia.url(search))
    search = input("Enter page title or search phrase: ")


