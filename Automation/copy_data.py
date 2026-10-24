import os
import shutil
import datetime

source_file_path = "/mnt/c/Users/HP/Desktop/python/python_learning/devops/bkp/date.txt"
destination_path = os.path.join("/mnt/c/Users/HP/Desktop/python/python_learning/devops/", "backup_dir")
if not os.path.exists(destination_path):
    os.makedirs(destination_path)
    print("destination directory successfully created")
time = datetime.datetime.now().strftime("%Y-%m-%d")
file_name = f"date_{time}.txt"
destination_file_path = os.path.join(destination_path, file_name)
shutil.copy(source_file_path, destination_file_path)
print("file content successfully backuped")



