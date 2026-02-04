import streamlit as st
import random
import os
from PIL import Image, ImageOps  # Librerías para manejar el giro

st.set_page_config(page_title="Mi Jardín Botánico", page_icon="🌿")

# (La lista de plantas se mantiene igual que la anterior...)
plantas = [
    {"id": "1", "comun": "Níspero", "cient": "Eriobotrya japonica", "tipo": "Angiosperma", "extra": "Fruto: Pomo. Hoja: Perenne rugosa"},
    {"id": "2", "comun": "Olivo", "cient": "Olea europaea", "tipo": "Angiosperma", "extra": "Fruto: Drupa (Aceituna). Hoja: Elíptica"},
    # ... pega aquí el resto de tus 33 plantas ...
    {"id": "33", "comun": "Madreselva", "cient": "Lonicera japonica", "tipo": "Angiosperma", "extra": "Trepadora perfumada tubular"}
]

# Inicializar estados
if 'puntos' not in st.session_state:
    st.session_state.puntos = 0
    st.session_state.indice = 0
    random.shuffle(plantas)
    st.session_state.lista = plantas
    st.session_state.respondido = False

if st.session_state.indice < len(st.session_state.lista):
    p = st.session_state.lista[st.session_state.indice]
    
    st.title("🌿 Quiz Botánico")
    st.write(f"Planta {st.session_state.indice + 1}/33 | Puntos: {st.session_state.puntos}")

    # --- BLOQUE PARA CORREGIR EL GIRO ---
    nombre_img = f"{p['id']}.jpg.jpg"
    if os.path.exists(nombre_img):
        img = Image.open(nombre_img)
        img = ImageOps.exif_transpose(img) # Esta línea detecta el giro y lo corrige
        st.image(img, use_container_width=True)
    else:
        st.error(f"Falta foto: {nombre_img}")
    # ------------------------------------

    with st.form("mi_formulario"):
        rta = st.text_input("¿Cómo se llama esta planta?").strip().lower()
        enviado = st.form_submit_button("Comprobar")
        
        if enviado:
            st.session_state.respondido = True
            def limpiar(t): return t.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
            
            if limpiar(rta) == limpiar(p['comun'].lower()):
                st.success(f"✅ ¡Correcto! Es: {p['comun']}")
                st.session_state.puntos += 1
            else:
                st.error(f"❌ Es: {p['comun']}")
            
            st.info(f"🧬 **Datos PRO:** {p.get('extra', '')} | Tipo: {p.get('tipo', 'Angiosperma')}")

    if st.session_state.respondido:
        if st.button("Siguiente Planta ➡️"):
            st.session_state.indice += 1
            st.session_state.respondido = False
            st.rerun()
else:
    st.balloons()
    st.success(f"🏆 ¡Fin! Puntuación: {st.session_state.puntos}/33")
    if st.button("Volver a jugar"):
        st.session_state.indice = 0
        st.session_state.puntos = 0
        random.shuffle(st.session_state.lista)
        st.rerun()
