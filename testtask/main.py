import os
import pandas as pd
df = pd.DataFrame()

list_of_all_files = []
for i in os.walk(os.getcwd()):
    list_of_all_files.append(i)
    
list_of_folder_names = []
for file in list_of_all_files:
    for i in range(1, len(file[2]) + 1):
        list_of_folder_names.append(file[0].split('\\')[-1])
        
list_of_file_names = []
for file in list_of_all_files:
    for item in file[2]:
        list_of_file_names.append(item.split('.')[0])
        
list_of_file_extensions = []
for file in list_of_all_files:
    for item in file[2]:
        if len(item.split('.')) == 1:
            list_of_file_extensions.append('file')
        else:
            list_of_file_extensions.append(item.split('.')[-1])
        
list_of_number = [i for i in range(1, len(list_of_file_names) + 1)]
        
df['Номер строки'] = list_of_number
df['Папка в которой лежит файл'] = list_of_folder_names
df['название файла'] = list_of_file_names
df['расширение файла'] = list_of_file_extensions

df.to_excel('result.xlsx',index = False)