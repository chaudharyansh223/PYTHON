words = ["level", "radar", "python", "devops", "madam", "cloud"]
palindrom_words = []
for item in words:
    if item == item[::-1]:
        palindrom_words.append(item)
print("palindrom words are: ",palindrom_words)

        