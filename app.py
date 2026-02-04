import streamlit as st
import random
import os
from PIL import Image, ImageOps

st.set_page_config(page_title="Quiz Botánico Pro", layout="centered")

# BASE DE DATOS ACTUALIZADA (ID 21: Magnolia | ID 23: Adelfa)
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

if 'idx' not in st.session_state:
    st.session_state.update({'pts':0,'idx':0,'l':p_list.copy(),'opts':[],'tipo_p':"",'respondido':False})
    random.shuffle(st.session_state.l)

def nueva_pregunta():
    item = st.session_state.l[st.session_state.idx]
    st.session_state.tipo_p = random.choice(["Nombre Común","Nombre Científico","Tipo (Angio/Gimno)"])
    
    if st.session_state.tipo_p == "Nombre Común":
        correcta = item['n']
        pool = list(set([p['n'] for p in p_list if p['n'] != correcta]))
    elif st.session_state.tipo_p == "Nombre Científico":
        correcta = item['s']
