import pandas as pd
from ConcatDataFrames import *
import openpyxl



folder = "C:/Users/cafra/OneDrive/Documents/concat_files/folder"

# files = []
#     # Obtiene la lista de archivos en la carpeta
# for file in os.listdir(folder):
#   # Verifica si el elemento es un archivo
#   if os.path.isfile(os.path.join(folder, file)):
#     files.append(os.path.join(folder, file))

# print(files)

myconcatdataframes =  ConcatDataFrames()

files = ConcatDataFrames.list_file_in_folder(folder)

print(files)

for file in files:
    df = pd.read_csv(file,sep=";")
    myconcatdataframes.add_dataframe(df)

result = myconcatdataframes.concat_dataframes()

print(result)

result.to_excel('dataframeconcat.xlsx',sheet_name='uff!')




# df = pd.read_csv('C:/Users/cafra/OneDrive/Documents/concat_files/folder\\ArchivoNo1.csv',sep=";")

# print(df.head())