import streamlit as st
import random
import os

st.set_page_config(page_title="Mi Jardín Botánico", page_icon="🌿")

# BASE DE DATOS CORREGIDA (33 PLANTAS)
plantas = [
    {"id": "1", "comun": "Níspero"}, {"id": "2", "comun": "Olivo"}, {"id": "3", "comun": "Drago"},
    {"id": "4", "comun": "Yuca"}, {"id": "5", "comun": "Naranjo"}, {"id": "6", "comun": "Cítrico"},
    {"id": "7", "comun": "Yuca de jardín"}, {"id": "8", "comun": "Aspidistra"}, {"id": "9", "comun": "Geranio"},
    {"id": "10", "comun": "Agave"}, {"id": "11", "comun": "Pino de Norfolk"}, {"id": "12", "comun": "Araucaria"},
    {"id": "13", "comun": "Evónimo"}, {"id": "14", "comun": "Maguey morado"}, {"id": "15", "comun": "Laurel"},
    {"id": "16", "comun": "Palmera abanico"}, {"id": "17", "comun": "Limonero"}, {"id": "18", "comun": "Flor de Pascua"},
    {"id": "19", "comun": "Aloe Vera"}, {"id": "20", "comun": "Naranjo"}, {"id": "21", "comun": "Cica"},
    {"id": "22", "comun": "Cinta"}, {"id": "23", "comun": "Costilla de Adán"}, {"id": "24", "comun": "Hibisco"},
    {"id": "25", "comun": "Ficus caucho"}, {"id": "26", "comun": "Buganvilla"}, {"id": "27", "comun": "Potus"},
    {"id": "28", "comun": "Sansevieria"}, {"id": "29", "comun": "Romero"}, {"id": "30", "comun": "Diente de león"},
    {"id": "31", "comun": "Árbol del cielo"}, {"id": "32", "comun": "Aligustre"}, {"id": "33", "comun": "Madreselva"}
]

# Inicialización del estado del juego
if 'puntos' not in st.session_state:
    st.session_state.puntos = 0
    st.session_state.lista_juego = plantas.copy()
    random.shuffle(st.session_state.lista_juego)
    st.session_state.indice = 0

# Pantalla de fin de juego
if st.session_state.indice >= len(st.session_state.lista_juego):
    st.balloons()
    st.title("🏆 ¡Examen Terminado!")
    st.write(f"Has identificado correctamente las 33 plantas.")
    if st.button("Reiniciar Juego"):
        st.session_state.puntos = 0
        st.session_state.indice = 0
        random.shuffle(st.session_state.lista_juego)
        st.rerun()
else:
    p = st.session_state.lista_juego[st.session_state.indice]
    
    st.title("🌿 ¿Qué planta es?")
    st.write(f"Planta {st.session_state.indice + 1} de 33 | Puntos: {st.session_state.puntos}")

    # EL TRUCO DEL NOMBRE DOBLE: Buscamos .jpg.jpg
    nombre_archivo = f"{p['id']}.jpg.jpg"
    
    if os.path.exists(nombre_archivo):
        st.image(nombre_archivo, use_container_width=True)
    else:
        st.error(f"No encuentro la imagen: {nombre_archivo}")
        st.info("Revisa que en tu GitHub las fotos se llamen exactamente así.")

    # Formulario de respuesta
    with st.form("quiz", clear_on_submit=True):
        rta = st.text_input("Escribe el nombre común:").strip().lower()
        boton = st.form_submit_button("Comprobar")
        
        if boton:
            # Quitamos tildes para que sea más fácil acertar
            def normalizar(texto):
                return texto.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
            
            if normalizar(rta) == normalizar(p['comun'].lower()):
                st.success(f"✅ ¡Correcto! Es un {p['comun']}")
                st.session_state.puntos += 1
                st.session_state.indice += 1
                st.button("Siguiente Planta ➡️")
            else:
                st.error(f"❌ Casi... la respuesta era: {p['comun']}")
                st.session_state.indice += 1
                st.button("Continuar ➡️")
