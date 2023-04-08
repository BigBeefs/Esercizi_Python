import streamlit as st
import pandas as pd

def confrontoNum(numb1,numb2,numb3):
    '''Individua il numero maggiore e minore dei 3'''

    if numb1>=numb2 and numb1>=numb3 and numb2<=numb3:
        st.write('"',numb1,'" è il numero più grande, "',numb2,'" è il numero più piccolo')
    elif numb1>=numb2 and numb1>=numb3 and numb3<=numb2:
        st.write('"',numb1,'" è il numero più grande, "',numb3,'" è il numero più piccolo')
    elif numb2>=numb1 and numb2>=numb3 and numb1<=numb3:
        st.write('"',numb2,'" è il numero più grande, "',numb1,'" è il numero più piccolo')
    elif numb2>=numb1 and numb2>=numb3 and numb3<=numb1:
        st.write('"',numb2,'" è il numero più grande, "',numb1,'" è il numero più piccolo')
    elif numb3>=numb1 and numb3>=numb2 and numb1<=numb2:
        st.write('"',numb3,'" è il numero più grande, "',numb1,'" è il numero più piccolo')
    elif numb3>=numb1 and numb3>=numb2 and numb2<=numb1:
        st.write('"',numb3,'" è il numero più grande, "',numb2,'" è il numero più piccolo')
def main():
    numb1 = st.slider('Inserisci un numero 1: ',0,100)
    numb2 = st.slider('Inserisci un numero 2: ',0,100)
    numb3 = st.slider('Inserisci un numero 3: ',0,100)
    confrontoNum(numb1,numb2,numb3)
    

if __name__ == "__main__":
    main()