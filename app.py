import streamlit as st
import random, os
from PIL import Image, ImageOps

st.set_page_config(page_title="Herbario Botánico", page_icon="🌿")

# BASE DE DATOS ACTUALIZADA (1-33) - 12 AHORA ES ARÁNDANO AZUL
p_list = [
    {"id":"1","c":"Níspero","t":"Angiosperma","f":"Pomo"},
    {"id":"2","c":"Olivo","t":"Angiosperma","f":"Drupa (Aceituna)"},
    {"id":"3","c":"Drago","t":"Angiosperma","f":"Baya. Savia roja"},
    {"id":"4","c":"Yuca","t":"Angiosperma","f":"Cápsula. Hoja lisa"},
    {"id":"5","c":"Naranjo","t":"Angiosperma","f":"Hesperidio"},
    {"id":"6","c":"Cítrico","t":"Angiosperma","f":"Hesperidio (aceites)"},
    {"id":"7","c":"Yuca de jardín","t":"Angiosperma","f":"Cápsula. Hoja con espina"},
    {"id":"8","c":"Aspidistra","t":"Angiosperma","f":"Baya (flor a ras de suelo)"},
    {"id":"9","c":"Geranio","t":"Angiosperma","f":"Esquizocarpo"},
    {"id":"10","c":"Agave","t":"Angiosperma","f":"Cápsula. Suculenta"},
    {"id":"11","c":"Flor de Pascua","t":"Angiosperma","f":"Ciatio (brácteas rojas)"},
    {"id":"12","c":"Arándano azul","t":"Angiosperma","f":"Baya"},
    {"id":"13","c":"Pino","t":"Gimnosperma","f":"Cono (Piña)"},
    {"id":"14","c":"Araucaria","t":"Gimnosperma","f":"Cono. Pino de Norfolk"},
    {"id":"15","c":"Araucaria","t":"Gimnosperma","f":"Cono. Tercer ejemplar"},
    {"id":"16","c":"Palmera abanico","t":"Angiosperma","f":"Drupa (hoja palmada)"},
    {"id":"17","c":"Maguey morado","t":"Angiosperma","f":"Cápsula. Hoja bicolor"},
    {"id":"18","c":"Laurel","t":"Angiosperma","f":"Baya (Drupa pequeña)"},
    {"id":"19","c":"Aloe Vera","t":"Angiosperma","f":"Cápsula. Medicinal"},
    {"id":"20","c":"Naranjo","t":"Angiosperma","f":"Hesperidio (Ejemplar 2)"},
    {"id":"21","c":"Cica","t":"Gimnosperma","f":"Semillas desnudas (falso fruto)"},
    {"id":"22","c":"Cinta","t":"Angiosperma","f":"Cápsula. Estolonífera"},
    {"id":"23","c":"Costilla de Adán","t":"Angiosperma","f":"Baya compuesta (tóxica)"},
    {"id":"24","c":"Maguey morado","t":"Angiosperma","f":"Cápsula (Ejemplar 2)"},
    {"id":"25","c":"Ficus caucho","t":"Angiosperma","f":"Sicono (Higo pequeño)"},
    {"id":"26","c":"Buganvilla","t":"Angiosperma","f":"Aquenio (brácteas)"},
    {"id":"27","c":"Potus","t":"Angiosperma","f":"Baya (en interior no florece)"},
    {"id":"28","c":"Conchitas mandala","t":"Angiosperma","f":"Cápsula. Suculenta roseta"},
    {"id":"29","c":"Romero","t":"Angiosperma","f":"Tetraquenio. Aromática"},
    {"id":"30","c":"Diente de león","t":"Angiosperma","f":"Cipsela (Vilano)"},
    {"id":"31","c":"Naranjo","t":"Angiosperma","f":"Hesperidio (Ejemplar 3)"},
    {"id":"32","c":"Grama","t":"Angiosperma","f":"Cariópside (Gramínea)"},
    {"id":"33","c":"Trébol","t":"Angiosperma","f":"Legumbre (Trifoliada)"}
]

if 'pts' not in st.session_state:
    st.session_state.update({'pts': 0, 'idx': 0, 'r': False, 'l': p_list.copy(), 'ultima_rta': ''})
    random.shuffle(st.session_state.l)

if st.session_state.idx < len(st.session_state.l):
    item = st.session_state.l[st.session_state.idx]
    st.title("🌿 Examen de Botánica")
    st.write(f"Planta {st.session_state.idx + 1}/33 | Puntos: {st.session_state.pts}")

    img_path = f"{item['id']}.jpg.jpg"
    if os.path.exists(img_path):
        st.image(ImageOps.exif_transpose(Image.open(img_path)), use_container_width=True)
    else: st.error(f"Falta: {img_path}")

    with st.form("quiz", clear_on_submit=True):
        txt = st.text_input("¿Qué planta es?").strip().lower()
        if st.form_submit_button("Validar"):
            st.session_state.ultima_rta = txt
            st.session_state.r = True

    if st.session_state.r:
        def cl(t): return t.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("
