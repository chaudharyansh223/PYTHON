import os

source_dir_path = "/mnt/c/Users/HP/Desktop/python/python_learning/devops/size"
total_size = 0
for files in os.listdir(source_dir_path):
    full_file_path = os.path.join(source_dir_path, files)
    if os.path.isfile(full_file_path):
        total_size+= os.path.getsize(full_file_path)
size_limit = 50 * 1024 * 1024
size_limit_mb = size_limit / (1024 * 1024)
total_size_in_mb = total_size / (1024 * 1024)
if total_size > size_limit:
    print(f"source dir {source_dir_path} size exceeds {size_limit_mb} limit")
else:
    print(f"source_dir {source_dir_path} is safe, it didn't exceed the {size_limit_mb} size limit and total size of dir is: {total_size_in_mb}")
