import os
import shutil

from_dir = "C:/Users/LENOVO/Downloads"
to_dir = "C:/whitehatjr/downloeded pdfs"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for i in list_of_files:
    name,extension = os.path.splitext(i)
    # print(name)
    # print(extension)
    if extension == '':
        continue
    if extension in ['.txt','.doc','.docx','.pdf']:
        path1 = from_dir + '/' + i
        path2 = to_dir + '/' + "pdf_files"
        path3 = to_dir + '/' + "pdf_files" + '/' + i
       # print(path1)
       # print(path3)
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else :
            os.makedirs(path2)
            shutil.move(path1,path3)

        
    