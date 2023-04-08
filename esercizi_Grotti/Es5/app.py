import pandas as pd
import streamlit as st
import numpy as np
import openpyxl
import os



def createCsv(df):
    '''Crea tanti file .csv quanti elementi della colonna Territorio'''

    for i in df.Territorio:
        dfState=df.loc[df['Territorio'] == i]
        i=i.replace("'", "")
        i=i.replace("/", "")
        i=i.replace(" ", "_")
        i=i.replace("-", "_")
        dfState.to_csv("file/file_csv/"+i+".csv")
    print('File .csv creati con successo')

def creatXlsx(df):
    '''Crea tanti file .xlsx quanti elementi della colonna Territorio'''

    for i in df.Territorio:
        dfState=df.loc[df['Territorio'] == i]
        i=i.replace("'", "")
        i=i.replace("/", "")
        i=i.replace(" ", "_")
        i=i.replace("-", "_")
        dfState.to_excel("file/file_xlsx/"+i+".xlsx")
    print('File .xlsx creati con successo')
    
        
def deleteCsv():
    '''Cancella tutti i file della cartella file.csv'''

    dir = 'file/file_csv'
    for file in os.scandir(dir):
        os.remove(file.path)
    print('File .csv eliminiati con successo')
    
def deleteXlsx():
    '''Cancella tutti i file della cartella file.xlsx'''

    dir = 'file/file_xlsx'
    for file in os.scandir(dir):
        os.remove(file.path)
    print('File .xlsx eliminiati con successo')

def main():
    df = pd.read_csv('energia.csv')
    crea = True
    if crea == True:
        createCsv(df)
        creatXlsx(df)

    else:
        deleteCsv()
        deleteXlsx()


if __name__ == "__main__":
    main()