import os
import shutil
import time

source_dir = "/mnt/c/Users/HP/Desktop/python/python_learning/devops/logs"
current_time = time.time()
for content in os.listdir(source_dir):
    source_file_path = os.path.join(source_dir, content)
    if os.path.isfile(source_file_path) and content.endswith(".log"):
        file_modified_time = os.path.getmtime(source_file_path)
        file_time = current_time - file_modified_time
        if file_time > 604800:
            os.remove(source_file_path)
            print("7 days older file removed")
        else:
            print(f"file {content} isn't older than 7 days")
