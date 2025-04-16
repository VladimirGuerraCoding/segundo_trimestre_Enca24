#tratare de ejecutar las funciones importando la lib streamlit
#ejecutar las app con el comando streamlit run nombredelarchivo.py enter en el terminal

import streamlit as st
import numpy as np


def main():
    st.write('## OPERADOR MATEMATICO DE NUMEROS')
    num1 = st.number_input('Ingresa el primer numero: ')
    num2 = st.number_input('Ingresa el segundo numero: ')
    
    operacion = st.text_input('Selecciona la operacion a realizar')
    st.write(operacion)

    match operacion:
        case 'suma':
            num1 + num2
            st.write(f'La suma de  {num1} + {num2} es:'),
        case 'resta':
            num1 - num2
            st.write(f'La resta de  {num1} - {num2} es:'),
        case 'multiplicacion':
            num1 * num2
            st.write(f'El producto de  {num1} * {num2} es:'),
        case 'division':
            num1 / num2
            st.write(f'La division de  {num1} / {num2} es:'),
        case _:
            st.write(f'OPERACION NO VALIDA SELECCIONA suma, resta, multiplicacion o division'),
main()