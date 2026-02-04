import streamlit as st
import random
import os
from PIL import Image, ImageOps

st.set_page_config(page_title="Mi Jardín Botánico", page_icon="🌿")

# BASE DE DATOS REVISADA LÍNEA POR LÍNEA
plantas = [
    {"id": "1", "comun": "Níspero", "extra": "Fruto: Pomo. Hoja: Perenne rugosa"},
    {"id": "2", "comun": "Olivo", "extra": "Fruto: Drupa (Aceituna). Hoja: Elíptica"},
    {"id": "3", "comun": "Drago", "extra": "Savia roja. Hoja: Ensiforme"},
    {"id": "4", "comun": "Yuca", "extra": "Hoja lisa sin espina terminal"},
    {"id": "5", "comun": "Naranjo", "extra": "Fruto: Hesperidio. Hoja: Pecíolo alado"},
    {"id": "6", "comun": "Cítrico", "extra": "Género de frutales con aceites esenciales"},
    {"id": "7", "comun": "Yuca de jardín", "extra": "Hoja rígida con espina terminal"},
    {"id": "8", "comun": "Aspidistra", "extra": "Hoja muy ancha de sombra"},
    {"id": "9", "comun": "Geranio", "extra": "Hoja circular lobulada"},
    {"id": "10", "comun": "Agave", "extra": "Suculenta. Roseta sin espinas"},
    {"id": "11", "comun": "Pino de Norfolk", "extra": "Gimnosperma. Ramas simétricas"},
    {"id": "12", "comun": "Araucaria", "extra": "Gimnosperma. Porte columnar estrecho"},
    {"id": "13", "comun": "Evónimo", "extra": "Arbusto. Hoja brillante serrada"},
    {"id": "14", "comun": "Maguey morado", "extra": "Hoja bicolor (verde/púrpura)"},
    {"id": "15", "comun": "Laurel", "extra": "Hoja aromática culinaria"},
    {"id": "16", "comun": "Palmera abanico", "extra": "Hoja palmada con hilos"},
    {"id": "17", "comun": "Limonero", "extra": "Fruto ácido (Limón)"},
    {"id": "18", "comun": "Flor de Pascua", "extra": "Brácteas rojas llamativas"},
    {"id": "19", "comun": "Aloe Vera", "extra": "Medicinal. Hoja suculenta con dientes"},
    {"id": "20", "comun": "Naranjo", "extra": "Segundo ejemplar de naranjo"},
    {"id": "21", "comun": "Cica", "extra": "Gimnosperma. Semillas desnudas"},
    {"id": "22", "comun": "Cinta", "extra": "Hojas estoloníferas (malamadre)"},
    {"id": "23", "comun": "Costilla de Adán", "extra": "Hojas con agujeros"},
    {"id": "24", "comun": "Hibisco", "extra": "Flor con columna estaminal larga"},
    {"id": "25", "comun": "Ficus caucho", "extra": "Hoja grande coriácea con látex"},
    {"id": "26", "comun": "Buganvilla", "extra": "Trepadora. Brácteas coloridas"},
    {"id": "27", "comun": "Potus", "extra": "Liana de interior variegada"},
    {"id": "28", "comun": "Sansevieria", "extra": "Hoja espada vertical"},
    {"id": "29", "comun": "Romero", "extra": "Arbusto aromático lineal"},
    {"id": "30", "comun": "Diente de león", "extra": "Inflorescencia amarilla"},
    {"id": "31", "comun": "Árbol del cielo", "extra": "Hoja compuesta muy larga"},
    {"id": "32", "comun": "Aligustre", "extra": "Hoja opuesta brillante"},
    {"id": "33", "comun": "Trébol", "extra": "Hoja: Trifoliada. Fruto: Legumbre"}
]

# Inicialización segura
if 'puntos' not in st.session_state:
    st.session_state.puntos = 0
    st.session_state.indice = 0
    st.session_state.lista = plantas.copy()
    random.shuffle(st.session_state.lista)
    st.session_state.respondido = False

if st.session_state.indice < len(st.session_state.lista):
    p = st.session_state.lista[st.session_state.indice]
    st.title("🌿 Herbario Interactivo")
    st.write(f"Planta {st.session_state.indice + 1} de 33 | Puntos: {st.session_state.puntos}")

    # Imagen
    nombre_img = f"{p['id']}.jpg.jpg"
    if os.path.exists(nombre_img):
        try:
            img = Image.open(nombre_img)
            img = ImageOps.exif_transpose(img)
            st.image(img, use_container_width=True)
        except:
            st.error("Error al cargar imagen")
    else:
        st.error(f"No encuentro {nombre_img}")

    # Formulario
    with st.form("quiz"):
        rta = st.text_input("¿Cómo se llama?").strip().lower()
        if st.form_submit_button("Comprobar"):
            st.session_state.respondido = True
            def norm(t): return t.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
            if norm(rta) == norm(p['comun'].lower()):
                st.success(f"✅ ¡Correcto! Es {p['comun']}")
                st.session_state.puntos += 1
            else:
                st.error(f"❌ Es {p['comun']}")
            st.info(f"🧬 {p['extra']}")

    if st.session_state.respondido and st.button("Siguiente ➡️"):
        st.session_state.indice += 1
        st.session_state.respondido = False
        st.rerun()
else:
    st.balloons()
    st.success(f"🏆 ¡Finalizado! Puntos: {st.session_state.puntos}/33")
    if st.button("Reiniciar"):
        st.session_state.puntos = 0
        st.session_state.indice = 0
        random.shuffle(st.session_state.lista)
        st.rerun()
