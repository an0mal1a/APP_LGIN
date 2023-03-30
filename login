import re
import string
import streamlit as st
import time
import subprocess




users = ['Pablo', 'Pepe', 'Jairo']
passwords = {'Pablo': "HnKWYGvA6pCKpO3Kbz", 'Pepe': ",", 'Jairo': ","}

# Titulo
title = 'LOGIN'
st.title(title)


#Ocultar el menú y el footer
hide_streamlit_style  = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Preguntamos nombre
name = st.text_input("Introduce tu nombre", key='-01-')

# Contraseña
input_password = st.text_input('Introduce tu contraseña', "", type='password')

# Boton
if st.button('Log in'):
    print('Intento de login hecho con estas credenciales: P:{} | U:{} '.format(input_password, name))

    if name == "":
        st.error("No has introduccido un nombre válido. \nSolo se aceptan letras, no simbolos.")

    else:
        if name in users:
            if input_password == passwords[name]:
                st.success("Has iniciado sesión correctamente, redirigiendo de forma segura...")
                bar = st.progress(0)

                for progres in range(101):
                    time.sleep(0.1)
                    bar.progress(progres, text='Redirection progress')
                try:
                    subprocess.Popen(['streamlit', 'run', 'chat.py'])
                except FileNotFoundError:
                    st.error("Ha ocurrido un error...")
            else:
                if input_password == "":
                    st.error('No has introducido contraseña')
                else:
                    st.error('Contraseña Incorrecta...')

        else:
            st.error('Usuario no encontrado')

elif st.button('Registrarse'):
    subprocess.Popen(['streamlit', 'run', 'register.py'])

else:
    st.write("")
