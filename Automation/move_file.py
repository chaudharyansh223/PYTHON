import os
import shutil
destination_path = "/mnt/c/Users/HP/Desktop/python/python_learning/devops/BackupFolder/"
source_path = "/mnt/c/Users/HP/Desktop/python/python_learning/devops/logfile/file.txt"
if not os.path.exists(destination_path):
    os.makedirs(destination_path)
destination_file_path = "/mnt/c/Users/HP/Desktop/python/python_learning/devops/BackupFolder/file.txt"
shutil.move(source_path, destination_file_path)
