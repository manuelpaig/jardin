import streamlit as st
import random
import os
from PIL import Image, ImageOps

st.set_page_config(page_title="Botánica Quiz", layout="centered")

# BASE DE DATOS ACTUALIZADA Y CORREGIDA
p_list = [
    {"id":"1","n":"Níspero","s":"Eriobotrya japonica","t":"Angiosperma","f":"Pomo"},
    {"id":"2","n":"Olivo","s":"Olea europaea","t":"Angiosperma","f":"Aceituna"},
    {"id":"3","n":"Drago","s":"Dracaena draco","t":"Angiosperma","f":"Baya"},
    {"id":"4","n":"Yuca / Cereus","s":"Yuca / Cereus hexagonus","t":"Angiosperma","f":"Cápsula"},
    {"id":"5","n":"Naranjo","s":"Citrus sinensis","t":"Angiosperma","f":"Hesperidio"},
    {"id":"6","c":"Cítrico","s":"Citrus sp.","t":"Angiosperma","f":"Hesperidio"},
    {"id":"7","n":"Falso maguey","s":"Furcraea foetida","t":"Angiosperma","f":"Cápsula"},
    {"id":"8","n":"Aspidistra","s":"Aspidistra elatior","t":"Angiosperma","f":"Baya"},
    {"id":"9","n":"Geranio","s":"Pelargonium sp.","t":"Angiosperma","f":"Esquizocarpo"},
    {"id":"10","n":"Agave","s":"Agave americana","t":"Angiosperma","f":"Cápsula"},
    {"id":"11","n":"Flor de Pascua","s":"Euphorbia pulcherrima","t":"Angiosperma","f":"Ciatio"},
    {"id":"12","n":"Arándano azul","s":"Vaccinium corymbosum","t":"Angiosperma","f":"Baya"},
    {"id":"13","n":"Pino","s":"Pinus pinaster","t":"Gimnosperma","f":"Cono"},
    {"id":"14","n":"Araucaria","s":"Araucaria heterophylla","t":"Gimnosperma","f":"Cono"},
    {"id":"15","n":"Araucaria","s":"Araucaria sp.","t":"Gimnosperma","f":"Cono"},
    {"id":"16","n":"Bonetero del japón","s":"Euonymus japonicus","t":"Angiosperma","f":"Cápsula"},
    {"id":"17","n":"Maguey morado","s":"Tradescantia spathacea","t":"Angiosperma","f":"Cápsula"},
    {"id":"18","n":"Laurel","s":"Laurus nobilis","t":"Angiosperma","f":"Baya"},
    {"id":"19","n":"Washingtonia filifera","s":"Washingtonia filifera","t":"Angiosperma","f":"Drupa"},
    {"id":"20","n":"Naranjo","s":"Citrus sinensis","t":"Angiosperma","f":"Hesperidio"},
    {"id":"21","n":"Cica","s":"Cycas revoluta","t":"Gimnosperma","f":"Semilla desnuda"},
    {"id":"22","n":"Cinta","s":"Chlorophytum comosum","t":"Angiosperma","f":"Cápsula"},
    {"id":"23","n":"Costilla de Adán","s":"Monstera deliciosa","t":"Angiosperma","f":"Baya"},
    {"id":"24","n":"Maguey morado","s":"Tradescantia spathacea","t":"Angiosperma","f":"Cápsula"},
    {"id":"25","n":"Ficus caucho","s":"Ficus elastica","t":"Angiosperma","f":"Sicono"},
    {"id":"26","n":"Buganvilla","s":"Bougainvillea sp.","t":"Angiosperma","f":"Aquenio"},
    {"id":"27","n":"Potus","s":"Epipremnum aureum","t":"Angiosperma","f":"Baya"},
    {"id":"28","n":"Conchitas mandala","s":"Echeveria sp.","t":"Angiosperma","f":"Cápsula"},
    {"id":"29","n":"Romero","s":"Salvia rosmarinus","t":"Angiosperma","f":"Tetraquenio"},
    {"id":"30","n":"Diente de león","s":"Taraxacum officinale","t":"Angiosperma","f":"Cipsela"},
    {"id":"31","n":"Naranjo","s":"Citrus sinensis","t":"Angiosperma","f":"Hesperidio"},
    {"id":"32","n":"Grama","s":"Cynodon dactylon","t":"Angiosperma","f":"Cariópside"},
    {"id":"33","n":"Trébol","s":"Trifolium sp.","t":"Angiosperma","f":"Legumbre"}
]

# Inicialización
if 'idx' not in st.session_state:
    st.session_state.update({'pts':0,'idx':0,'l':p_list.copy(),'opts':[],'tipo_p':""})
    random.shuffle(st.session_state.l)

def generar_opciones():
    item = st.session_state.l[st.session_state.idx]
    # Elegimos aleatoriamente qué preguntar
    st.session_state.tipo_p = random.choice(["Nombre","Científico","Tipo"])
    
    if st.session_state.tipo_p == "Nombre":
        correcta = item['n']
        otros = [p['n'] for p in p_list if p['n'] != correcta]
    elif st.session_state.tipo_p == "Científico":
        correcta = item['s']
        otros = [p['s'] for p in p_list if p['s'] != correcta]
    else:
        correcta = item['t']
        otros = ["Gimnosperma" if correcta == "Angiosperma" else "Angiosperma"]
    
    opciones = random.sample(list(set(otros)), 3) + [correcta]
    random.shuffle(opciones)
    st.session_state.opts = opciones

if not st.session_state.opts:
    generar_opciones()

# Pantalla de Juego
if st.session_state.idx < len(st.session_state.l):
    item = st.session_state.l[st.session_state.idx]
    st.title("🌿 Quiz de Botánica")
    st.subheader(f"Puntos: {st.session_state.pts} | Planta {st.session_state.idx + 1}/33")
    
    img_path = f"{item['id']}.jpg.jpg"
    if os.path.exists(img_path):
        st.image(ImageOps.exif_transpose(Image.open(img_path)), use_container_width=True)

    st.write(f"### Pregunta: ¿Cuál es el **{st.session_state.tipo_p}** de esta planta?")
    
    # Botones A, B, C, D
    cols = st.columns(2)
    for i, opcion in enumerate(st.session_state.opts):
        with cols[i % 2]:
            if st.button(f"{chr(65+i)}) {opcion}", use_container_width=True):
                # Validar
                val = ""
                if st.session_state.tipo_p == "Nombre": val = item['n']
                elif st.session_state.tipo_p == "Científico": val = item['s']
                else: val = item['t']
                
                if opcion == val:
                    st.success("¡CORRECTO!")
                    st.session_state.pts += 1
                else:
                    st.error(f"INCORRECTO. Era: {val}")
                
                st.info(f"Ficha: {item['n']} ({item['s']}) | {item['t']} | Fruto: {item['f']}")
                st.session_state.idx += 1
                st.session_state.opts = [] # Para generar nuevas en el siguiente loop
                st.button("Siguiente Planta ➡️")
else:
    st.balloons()
    st.success(f"🏆 ¡Finalizado! Total: {st.session_state.pts}/33")
    if st.button("Reiniciar"):
        st.session_state.update({'pts':0,'idx':0,'opts':[]})
        st.rerun()
