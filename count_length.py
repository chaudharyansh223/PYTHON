text = "cloud computing and cyber security architecture"
new_text = text.split(" ")
character_length = {}
for word in new_text:
    if len(word) >= 5:
        character_length.update({word: len(word)})
print(character_length)