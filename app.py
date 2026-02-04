import streamlit as st
import random
import os
from PIL import Image
from PIL import ImageOps

st.set_page_config(page_title="Herbario")

# Lista en formato vertical para que no se corte
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
    if not t:
        return ""
    t = t.lower()
    a,e,i,o,u = "á","é","í","ó","ú"
    t = t.replace(a,"a").replace(e,"e")
    t = t.replace(i,"i").replace(o,"o")
    t = t.replace(u,"u")
    return t

if 'pts' not in st.session_state:
    st.session_state.update({
        'pts':0,
        'idx':0,
        'r':False,
        'l':p_list.copy(),
        'ur':'',
        'li':-1
    })
    random.shuffle(st.session_state.l)

if st.session_state.idx < len(st.session_state.l):
    item = st.session_state.l[st.session_state.idx]
    st.title("Herbario")
    
    # Imagen
    img_n = item['id'] + ".jpg.jpg"
    if os.path.exists(img_n):
        im = Image.open(img_n)
        st.image(ImageOps.exif_transpose(im))
    
    # Formulario
    with st.form("f", clear_on_submit=True):
        txt = st.text_input("Nombre:")
        btn = st.form_submit_button("Validar")
        if btn:
            st.session_state.ur = txt
            st.session_state.r = True

    if st.session_state.r:
        r_u = limpiar(st.session_state.ur)
        r_c = limpiar(item['c'])
        if r_u == r_c:
            st.success("Correcto")
            if st.session_state.li != st.session_state.idx:
                st.session_state.pts += 1
                st.session_state.li = st.session_state.idx
        else:
            st.error("Es: " + item['c'])
        
        # Info tecnica
        st.write("Tipo: " + item['t'])
        st.write("Fruto: " + item['f'])

        if st.button("Siguiente"):
            st.session_state.r = False
            st.session_state.ur = ""
            st.session_state.idx += 1
            st.rerun()
else:
    st.write("Fin. Puntos: " + str(st.session_state.pts))
    if st.button("Reiniciar"):
        st.session_state.update({'pts':0,'idx':0,'r':False})
        st.rerun()
