text = "devops pipeline"
character = {}
new_text = text.replace(" ", "")
for alphabet in new_text:
    if alphabet not in character:
        character[alphabet] = character.get(alphabet, 0)+1
        continue
    character[alphabet]+=1
print(character)

    

