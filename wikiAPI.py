import wikipedia

while True:
    input = input("Question: ")
    # Set language eg. chinese
    # wikipedia.set_lang("zh")
    print(wikipedia.summary(input, sentences=2))
