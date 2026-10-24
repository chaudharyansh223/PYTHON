count = 0
try:
    with open("note.txt", "r") as file:
        for line in file:
            new_line = line.strip(line)
            count+=1
        print("file isn't empty and total lines are:", count)
except FileNotFoundError as e:
    print("file not found")
finally:
    print("operation finished")


