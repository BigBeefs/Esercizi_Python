import streamlit as st
import pandas as pd
import datetime as dt
from datetime import timedelta

def checkAge():
    '''Fa la differenza di anni tra la data di oggi e la data immessa nell'input'''
    d = st.date_input('Data di nascita ("Età minima 19 anni")',dt.date.today()-timedelta(6939))
    today = dt.date.today()
    years = today.year - d.year
    if today.month < d.month or (today.month == d.month and today.day < d.day):
        years -= 1
    return years

def controlloPatente(diffYears,patente):
    '''Controlla se si ha i requisiti per avere la macchina a noleggio'''
    if diffYears >= 19 and patente == 'Si':
        exit = st.success('Puoi avere la macchina')
        return exit
    elif diffYears< 19:
        exit = st.error('Cresci regazzì!!')
    else:
        exit = st.error('Prenditi la patente SFIGATO!!')
        return exit
    
    
def main():
    st.title('Noleggio Auto')
    patente = st.radio('Hai la patente?',('Si','No'))
    # checkAge()
    diffYears = checkAge()

    controlloPatente(diffYears,patente)

if __name__ == "__main__":
    main()