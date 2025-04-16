#tratare de ejecutar las funciones importando la lib streamlit
#ejecutar las app con el comando streamlit run nombredelarchivo.py enter en el terminal

import streamlit as st


def main():
    st.write('## COMPARADOR DE NUMEROS')
    num1 = st.number_input('Ingresa el primer numero: ')
    num2 = st.number_input('Ingresa el segundo numero: ')


    def comparador():
        if (num1 > num2):
            st.write(f'El {num1} si es mayor que {num2}'),
        elif(num1 < num2):
            st.write(f'El {num1} No es mayor que {num2}'),
        else:
            st.write(f'Los numeros {num1} y {num2} son iguales'),
    comparador()
main()
