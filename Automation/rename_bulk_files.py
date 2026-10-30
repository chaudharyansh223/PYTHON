import os

source_dir_path = "/mnt/c/Users/HP/Desktop/python/python_learning/devops/images"
for file_name in os.listdir(source_dir_path):
    if file_name.endswith(".jpg"):
        old_file_path = os.path.join(source_dir_path, file_name)
        new_file_name = f"proceed_{file_name}"
        new_file_path = os.path.join(source_dir_path, new_file_name)
        os.rename(old_file_path, new_file_path)
