import requests
import streamlit as st
import time
import subprocess
import bcrypt


ip = requests.get('http://checkip.amazonaws.com').text.strip()
print("Hola, he entrado  a tu página, mi IP es: {}".format(ip))

users = ['Pablo', 'Pepe', 'Jairo']
password = "HnKWYGvA6pCKpO3Kbz"
salt = bcrypt.gensalt()

hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)


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

col1, col2 = st.columns(2, gap='large')

# Boton
if col1.button('Log in'):
    print('Intento de login hecho con estas credenciales: P:{} | U:{} | IP: {}'.format(input_password, name, ip))

    if name == "":
        st.error("No has introduccido un nombre válido. \nSolo se aceptan letras, no simbolos.")

    else:
        if name in users:
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                st.success("Has iniciado sesión correctamente, redirigiendo de forma segura...")
                bar = st.progress(0)

                for progres in range(101):
                    time.sleep(0.1)
                    bar.progress(progres, text='Redirection progress')
                try:
                    subprocess.Popen(['streamlit', 'run', 'chat.py'])
                    print("Accediendo al chat..")
                except:
                    st.error("Ha ocurrido un error...")
            else:
                if input_password == "":
                    st.error('No has introducido contraseña')
                else:
                    st.error('Contraseña Incorrecta...')

        else:
            st.error('Usuario no encontrado')

elif col2.button('Acerca de CHAT SEGURO '):
    subprocess.Popen(['streamlit', 'run', 'Acerca.py'])

else:
    st.write("")
