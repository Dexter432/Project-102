import os
import shutil
from_dir="C:/Users/Marcelo/Downloads/Aula"
to_dir="C:/Users/Marcelo/Documents/Arquivos_Documentos"
list_of_files = os.listdir(from_dir)
###print(list_of_files)
for file in list_of_files:
    name,extension=os.path.splitext(file)
    if extension in [".txt", ".doc", ".docx", ".pdf"]:
        path1= from_dir+"/"+file
        path2= to_dir+"/"+"arquivo"
        path3= path2+"/"+file
        if os.path.exists(path2):
            print("Movendo" + file +".....")
            shutil.move(path1,path3)
        else:
             os.makedirs(path2)
             print("Movendo"+ file +".....")
             shutil.move(path1,path3)