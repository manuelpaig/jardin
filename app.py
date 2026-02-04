import streamlit as st
import random
import os
from PIL import Image, ImageOps

# Configuración inicial
st.set_page_config(page_title="Quiz Botánico", layout="centered")

# 1. BASE DE DATOS (Asegúrate de que los IDs coincidan con tus fotos)
p_list = [
    {"id":"1","n":"Níspero","s":"Eriobotrya japonica","t":"Angiosperma","f":"Pomo"},
    {"id":"2","n":"Olivo","s":"Olea europaea","t":"Angiosperma","f":"Aceituna"},
    {"id":"3","n":"Drago","s":"Dracaena draco","t":"Angiosperma","f":"Baya"},
    {"id":"4","n":"Yuca / Cereus","s":"Yuca / Cereus hexagonus","t":"Angiosperma","f":"Cápsula"},
    {"id":"5","n":"Naranjo","s":"Citrus sinensis","t":"Angiosperma","f":"Hesperidio"},
    {"id":"6","n":"Cítrico","s":"Citrus sp.","t":"Angiosperma","f":"Hesperidio"},
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
    {"id":"21","n":"Magnolia común","s":"Magnolia grandiflora","t":"Angiosperma","f":"Polifolículo"},
    {"id":"22","n":"Cinta","s":"Chlorophytum comosum","t":"Angiosperma","f":"Cápsula"},
    {"id":"23","n":"Adelfa","s":"Nerium oleander","t":"Angiosperma","f":"Folículo"},
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

# 2. INICIALIZACIÓN DEL ESTADO
if 'lista' not in st.session_state:
    l_copy = p_list.copy()
    random.shuffle(l_copy)
    st.session_state.lista = l_copy
    st.session_state.puntos = 0
    st.session_state.indice = 0
    st.session_state.opciones = []
    st.session_state.respondido = False

# 3. LÓGICA DE PREGUNTAS
def preparar_pregunta():
    planta = st.session_state.lista[st.session_state.indice]
    tipo = random.choice(["Nombre Común", "Nombre Científico", "Tipo"])
    st.session_state.pregunta_tipo = tipo
    
    if tipo == "Nombre Común":
        correcta = planta['n']
        falsas = [p['n'] for p in p_list if p['n'] != correcta]
    elif tipo == "Nombre Científico":
        correcta = planta['s']
        falsas = [p['s'] for p in p_list if p['s'] != correcta]
    else:
        correcta = planta['t']
        falsas = ["Gimnosperma" if correcta == "Angiosperma" else "Angiosperma"]
    
    # Mezclar
    random.shuffle(falsas)
    finales = list(set(falsas[:3])) + [correcta]
    random.shuffle(finales)
    st.session_state.opciones = finales
    st.session_state.respondido = False

if not st.session_state.opciones:
    preparar_pregunta()

# 4. INTERFAZ
if st.session_state.indice < len(st.session_state.lista):
    item = st.session_state.lista[st.session_state.indice]
    
    st.title("🌿 Examen de Botánica")
    st.write(f"Planta **{st.session_state.indice + 1}** de 33 | Puntos: **{st.session_state.puntos}**")
    
    # Imagen
    img_name = f"{item['id']}.jpg.jpg"
    if os.path.exists(img_name):
        st.image(ImageOps.exif_transpose(Image.open(img_name)), use_container_width=True)
    else:
        st.warning(f"No se encuentra la imagen: {img_name}")

    st.write(f"### Pregunta: ¿Cuál es el **{st.session_state.pregunta_tipo}**?")

    # Botones
    for opt in st.session_state.opciones:
        if st.button(opt, use_container_width=True, disabled=st.session_state.respondido):
            st.session_state.respondido = True
            st.session_state.ultimo_click = opt
            
            # Validar
            correcta = item['n'] if st.session_state.pregunta_tipo == "Nombre Común" else (item['s'] if st.session_state.pregunta_tipo == "Nombre Científico" else item['t'])
            
            if opt == correcta:
                st.session_state.puntos += 1
                st.balloons()
            st.rerun()

    # Feedback tras responder
    if st.session_state.respondido:
        correcta = item['n'] if st.session_state.pregunta_tipo == "Nombre Común" else (item['s'] if st.session_state.pregunta_tipo == "Nombre Científico" else item['t'])
        
        if st.session_state.ultimo_click == correcta:
            st.success(f"✅ ¡Correcto! Es {correcta}")
        else:
            st.error(f"❌ Incorrecto. La respuesta era: {correcta}")
            
        st.info(f"**
