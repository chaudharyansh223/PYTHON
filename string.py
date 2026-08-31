text = "python is fast and python is simple because python is dynamic"
target_word = "python"

target_count = 0
new_text = text.split(" ")
for data in new_text:
    if target_word in data:
        target_count+=1
print(target_count)