#tratare de ejecutar las funciones importando la lib streamlit
#ejecutar las app con el comando streamlit run nombredelarchivo.py enter en el terminal
import streamlit as st

st.title('CUENTA HASTA CIEN')
cuenta = st.slider('Desplaza la barra hasta la cantidad que requieras.')
st.write(f'Lo desplazaste hasta {cuenta}')

for i in range(cuenta):
    st.button(f'{i}')


