import os
import shutil

from_dir = "C:/Users/avipa/Downloads"
to_dir = "Document_Files"

list_of_files = os.listdir(from_dir)
#print(list_of_files)
for file in list_of_files:
    name, ext = os.path.splitext(file)
    print(ext)
    if ext == "":
        continue
    if ext in ['.zip','.exe','.pdf','.jpg','.mov','.png','.msi','.docx','.pptx','.ini']:
        path1 = from_dir + '/' + file
        path2 = to_dir + '/' + "Document_Files"
        path3 = to_dir + '/' + "Document_Files" + '/' + file

    if os.path.exists(path2):
          print("Moving " + file + ".....")
          shutil.move(path1, path3)

    else:
          os.makedirs(path2)
          print("Moving " + file + ".....")
          shutil.move(path1, path3)  