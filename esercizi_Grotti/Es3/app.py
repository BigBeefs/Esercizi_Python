import streamlit as st
import pandas as pd



def disp_pari(num):
    '''Capisce se un numero è pari o dispari '''

    if (num%2) != 0:
        st.info('Questo numero è Dispari')
    else:
        st.info('Questo numero è Pari')   
      
        
def main():
    num = st.slider('Inserisci un numero',0,100)
    disp_pari(num)
    num1 = st.number_input('Inserisci un numero', min_value=0,max_value=100)
    disp_pari(num1)

if __name__ == "__main__":
    main()