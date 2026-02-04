import streamlit as st
import random, os
from PIL import Image, ImageOps

st.set_page_config(page_title="Herbario 33", page_icon="🌿")

# LISTA 1-33 (Fragmentada para evitar cortes)
p_list = [
    {"id":"1","c":"Níspero","t":"Angiosperma","f":"Pomo"},
    {"id":"2","c":"Olivo","t":"Angiosperma","f":"Drupa"},
    {"id":"3","c":"Drago","t":"Angiosperma","f":"Baya"},
    {"id":"4","c":"Yuca","t":"Angiosperma","f":"Cápsula"},
    {"id":"5","c":"Naranjo","t":"Angiosperma","f":"Hesperidio"},
    {"id":"6","c":"Cítrico","t":"Angiosperma","f":"Hesperidio"},
    {"id":"7","c":"Yuca de jardín","t":"Angiosperma","f":"Cápsula"},
    {"id":"8","c":"Aspidistra","t":"Angiosperma","f":"Baya"},
    {"id":"9","c":"Geranio","t":"Angiosperma","f":"Esquizocarpo"},
    {"id":"10","c":"Agave","t":"Angiosperma","f":"Cápsula"},
    {"id":"11","c":"Flor de Pascua","t":"Angiosperma","f":"Ciatio"},
    {"id":"12","c":"Arándano azul","t":"Angiosperma","f":"Baya"},
    {"id":"13","c":"Pino","t":"Gimnosperma","f":"Cono"},
    {"id":"14","c":"Araucaria","t":"Gimnosperma","f":"Cono"},
    {"id":"15","c":"Araucaria","t":"Gimnosperma","f":"Cono"},
    {"id":"16","c":"Bonetero del japón","t":"Angiosperma","f":"Cápsula"},
    {"id":"17","c":"Maguey morado","t":"Angiosperma","f":"Cápsula"},
    {"id":"18","c":"Laurel","t":"Angiosperma","f":"Baya"},
    {"id":"19","c":"Aloe Vera","t":"Angiosperma","f":"Cápsula"},
    {"id":"20","c":"Naranjo","t":"Angiosperma","f":"Hesperidio"},
    {"id":"21","c":"Cica","t":"Gimnosperma","f":"Semilla desnuda"},
    {"id":"22","c":"Cinta","t":"Angiosperma","f":"Cápsula"},
    {"id":"23","c":"Costilla de Adán","t":"Angiosperma","f":"Baya"},
    {"id":"24","c":"Maguey morado","t":"Angiosperma","f":"Cápsula"},
    {"id":"25","c":"Ficus caucho","t":"Angiosperma","f":"Sicono"},
    {"id":"26","c":"Buganvilla","t":"Angiosperma","f":"Aquenio"},
    {"id":"27","c":"Potus","t":"Angiosperma","f":"Baya"},
    {"id":"28","c":"Conchitas mandala","t":"Angiosperma","f":"Cápsula"},
    {"id":"29","c":"Romero","t":"Angiosperma","f":"Tetraquenio"},
    {"id":"30","c":"Diente de león","t":"Angiosperma","f":"Cipsela"},
    {"id":"31","c":"Naranjo","t":"Angiosperma","f":"Hesperidio"},
    {"id":"32","c":"Grama","t":"Angiosperma","f":"Cariópside"},
    {"id":"33","c":"Trébol","t":"Angiosperma","f":"Legumbre"}
]

def limpiar(t):
    if not t: return ""
    t = t.lower()
    t = t.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    return t

if 'pts' not in st.session_state:
    st.session_state.update({'pts':0,'idx':0,'r':False,'l':p_list.copy(),'ur':'','li':-1})
    random.shuffle(st.session_state.l)

if st.session_state.idx < len(st.session_state.l):
    item = st.session_state.l[st.session_state.idx]
    st.title("Herbario 33")
    st.write("Planta: " + str(st.session_state.idx + 1) + " / 33")
    st.write("Puntos: " + str(st.session_state.pts))

    img_path = item['id'] + ".jpg.jpg"
    if os.path.exists(img_path):
        img = Image.open(img_path)
        st.image(ImageOps.exif_transpose(img), use_container_width=True)
    else:
        st.error("Falta imagen: " + img_path)

    with st.form("f", clear_on_submit=True):
        txt = st.text_input("Nombre común:").strip().lower()
        if st.form_submit_button("Validar"):
            st.session_state.ur = txt
            st.session_state.r = True

    if st.session_state.r:
        if limpiar(st.session_state.ur) == limpiar(item['c']):
            st.success("Correcto: " + item['c'])
            if st.session_state.li != st.session_state.idx:
                st.session_state.pts += 1
                st.session_state.li = st.session_state.idx
        else:
            st.error("Incorrecto. Es: " + item['c'])
        
        st.write("---")
        st.write("Tipo: " + item['t'])
        st.write("Fruto: " + item['
