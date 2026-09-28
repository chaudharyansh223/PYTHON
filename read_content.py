def read_csv():
    with open("file.csv", "r") as file:
        return file.readlines()
        
def write_content(lines):
    with open("active_dev", "w") as file:
        for line in lines:
            line = line.strip()
            if line.startswith("id"):
                continue
            id,username,role,status = line.split(",")
            if role == "developer" and status == "active":
            
                    file.write(f"ID: {id} | {username}\n")
def main():
    data = read_csv()
    write_content(data)
if __name__ == "__main__":
     main()
