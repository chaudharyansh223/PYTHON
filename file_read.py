modified_file_content = []
def read():
    with open("app.log", "r") as file:
        for line in file:
            if line.startswith("ERROR:"):
                new_line = line.replace("ERROR: ", "")
                modified_line = new_line.strip()
                modified_file_content.append(modified_line)
    print(modified_file_content)
read()
