import streamlit as st
import random
import os
from PIL import Image, ImageOps

st.set_page_config(page_title="Mi Jardín Botánico", page_icon="🌿")

# LISTA ACTUALIZADA: 32 AHORA ES GRAMA
plantas = [
    {"id": "1", "comun": "Níspero", "extra": "Fruto: Pomo. Hoja: Perenne rugosa"},
    {"id": "2", "comun": "Olivo", "extra": "Fruto: Aceituna. Hoja: Elíptica"},
    {"id": "3", "comun": "Drago", "extra": "Savia roja. Hoja: Ensiforme"},
    {"id": "4", "comun": "Yuca", "extra": "Hoja lisa sin espina terminal"},
    {"id": "5", "comun": "Naranjo", "extra": "Fruto: Naranja. Hoja: Pecíolo alado"},
    {"id": "6", "comun": "Cítrico", "extra": "Frutal con aceites esenciales"},
    {"id": "7", "comun": "Yuca de jardín", "extra": "Hoja con espina terminal"},
    {"id": "8", "comun": "Aspidistra", "extra": "Hoja ancha de sombra"},
    {"id": "9", "comun": "Geranio", "extra": "Hoja circular lobulada"},
    {"id": "10", "comun": "Agave", "extra": "Roseta sin espinas laterales"},
    {"id": "11", "comun": "Flor de Pascua", "extra": "Brácteas rojas (Euphorbia)"},
    {"id": "12", "comun": "Araucaria", "extra": "Porte columnar muy estrecho"},
    {"id": "13", "comun": "Evónimo", "extra": "Arbusto. Hoja brillante serrada"},
    {"id": "14", "comun": "Araucaria", "extra": "Gimnosperma (Pino de Norfolk)"},
    {"id": "15", "comun": "Araucaria", "extra": "Tercer ejemplar de Araucaria"},
    {"id": "16", "comun": "Palmera abanico", "extra": "Hoja palmada con hilos"},
    {"id": "17", "comun": "Maguey morado", "extra": "Hoja bicolor (verde y púrpura)"},
    {"id": "18", "comun": "Laurel", "extra": "Hoja aromática culinaria"},
    {"id": "19", "comun": "Aloe Vera", "extra": "Medicinal. Hoja con dientes"},
    {"id": "20", "comun": "Naranjo", "extra": "Segundo ejemplar de naranjo"},
    {"id": "21", "comun": "Cica", "extra": "Gimnosperma. Semillas desnudas"},
    {"id": "22", "comun": "Cinta", "extra": "Hojas estoloníferas (malamadre)"},
    {"id": "23", "comun": "Costilla de Adán", "extra": "Hojas con agujeros"},
    {"id": "24", "comun": "Maguey morado", "extra": "Segundo ejemplar de Maguey"},
    {"id": "25", "comun": "Ficus caucho", "extra": "Hoja grande con látex"},
    {"id": "26", "comun": "Buganvilla", "extra": "Trepadora. Brácteas coloridas"},
    {"id": "27", "comun": "Potus", "extra": "Liana de interior variegada"},
    {"id": "28", "comun": "Sansevieria", "extra": "Hoja espada vertical"},
    {"id": "29", "comun": "Romero", "extra": "Arbusto aromático lineal"},
    {"id": "30", "comun": "Diente de león", "extra": "Inflorescencia amarilla"},
    {"id": "31", "comun": "Árbol del cielo", "extra": "Hoja compuesta muy larga"},
    {"id": "32", "comun": "Grama", "extra": "Agropyron. Gramínea de crecimiento rastrero"},
    {"id": "33", "comun": "Trébol", "extra": "Hoja trifoliada. Leguminosa"}
]

if 'puntos' not in st.session_state:
    st.session_state.update({'puntos':0, 'indice':0, 'respondido':False})
    st.session_state.lista = plantas.copy()
    random.shuffle(st.session_state.lista)

if st.session_state.indice < len(st.session_state.lista):
    p = st.session_state.lista[st.session_state.indice]
    st.title("🌿 Herbario Interactivo")
    st.write(f"Planta {st.session_state.indice + 1}/33 | Puntos: {st.session_state.puntos}")

    n_img = f"{p['id']}.jpg.jpg"
    if os.path.exists(n_img):
        img = ImageOps.exif_transpose(Image.open(n_img))
        st.image(img, use_container_width=True)
    else: st.error(f"Falta archivo: {n_img}")

    with st.form("q"):
        rta = st.text_input("¿Qué planta es?").strip().lower()
        if st.form_submit_button("Comprobar"):
            st.session_state.respondido = True
            def cl(t): return t.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
            # Aceptamos tanto 'grama' como 'agropyron' para la 32 por si acaso
            es_grama = (p['id'] == "32" and cl(rta) == "agropyron")
            
            if cl(rta) == cl(p['comun'].lower()) or es_grama:
                st.success(f"✅ ¡Correcto! Es {p['comun']}")
                st.session_state.puntos += 1
            else: st.error(f"❌ Es {p['comun']}")
            st.info(f"🧬 {p['extra']}")

    if st.session_state.respondido and st.button("Siguiente ➡️"):
        st.session_state.indice += 1
        st.session_state.respondido = False
        st.rerun()
else:
    st.balloons()
    st.success(f"🏆 ¡Finalizado! {st.session_state.puntos}/33")
    if st.button("Reiniciar"):
        st.session_state.update({'puntos':0, 'indice':0, 'respondido':False})
        random.shuffle(st.session_state.lista)
        st.rerun()
