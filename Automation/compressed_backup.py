import shutil
import os
import datetime

def backup(source, destination):
    today = datetime.datetime.today()
    backup_file_name = os.path.join(destination,f"backup_{today}")
    shutil.make_archive(backup_file_name,"gztar",source)

source = "/mnt/c/Users/HP/Desktop/python/python_learning/devops/bkp/"
destination = "/mnt/c/Users/HP/Desktop/python/python_learning/devops/bkup"

backup(source,destination)
