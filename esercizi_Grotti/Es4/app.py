import streamlit as st
import pandas as pd
import numpy as np

def findDiv(numb):
    '''Capisce se il numero selezionato è un numero perfetto'''

    div = np.array([],int)
    for i in range(1,numb-1):
        if numb % i == 0:
            div = np.append(div,i)

    if np.sum(div) == numb:
        st.success('Numero Perfetto')
    else:
        st.error('Non è un numero perfetto')

def main():
    st.title('Trova un Numero Perfetto')
    numb = st.number_input('Scegli un numero: ',1,1000,28)
    findDiv(numb)
    numb1 = st.slider('Scegli un numero: ',1,50,5)
    findDiv(numb1)

if __name__ == "__main__":
    main()