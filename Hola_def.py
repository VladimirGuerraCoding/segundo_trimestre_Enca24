#tratare de ejecutar las funciones importando la lib streamlit
#ejecutar las app con el comando streamlit run nombredelarchivo.py enter en el terminal

import streamlit as st

def main():
        def saludo():
                nombre = 'Vladimir'
                st.write(f'## !Hola {nombre} vas a programar muy bien!')
                st.success('EXITOSO VAMOS PA LANTE')

    
        saludo()

main()
