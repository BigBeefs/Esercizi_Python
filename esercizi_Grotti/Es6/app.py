import pandas as pd
import os
import glob
import openpyxl

def createOneCsv():
    '''Seleziona tutti i file di tipo .csv dalla cartella file.csv e li raggruppa tutti in un unico file .csv'''

    csv_files = glob.glob('../Es5/file/file_csv/*.csv')
    df_concat = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True)
    df_concat.to_csv("../Es5/file/unicoCsv.csv")
    print('Nuovo file.csv creato')

def createOneXlsx():
    '''Seleziona tutti i file di tipo .xlsx dalla cartella file.xlsx e li raggruppa tutti in un unico file .xlsx'''

    xlsx_files = glob.glob('../Es5/file/file_xlsx/*.xlsx')
    df_concat = pd.concat([pd.read_excel(file) for file in xlsx_files], ignore_index=True)
    df_concat.to_csv("../Es5/file/unicoXlsx.xlsx")
    print('Nuovo file.xlsx creato')

def main():
    createOneCsv()
    createOneXlsx()

if __name__ == "__main__":
    main()