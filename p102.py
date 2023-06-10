import os
import shutil

source="C:/Users/Mauli/Desktop/image_files"
destination="C:/Users/Mauli/Desktop"

file=os.listdir(source)
for i in file:
    name,ext=os.path.splitext(i)
    if ext=='':
        continue
    if ext in ['.txt', '.doc', '.docx', '.pdf']:
        path1=source + '/' + i
        path2=destination + '/' + 'docs_files'
        path3=destination + '/' + 'docs_files' + "/" + i

        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("moving")
            shutil.move(path1,path3)