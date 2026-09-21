file_read = {"status": "", "content": ""}
file_read_error = {}
def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            if content:
                    with open("content.txt", "w") as File:
                        File.write(content)
                    file_read["status"] = "succuess"
                    file_read["content"] = "read in content.txt"
                    return file_read
    except FileNotFoundError:
        file_read_error["status"] = "error"
        file_read_error["message"] = "file not found"
        return file_read_error
    finally:
        print("file read operation attempted")

print(read_file("missing_file.txt"))


                
