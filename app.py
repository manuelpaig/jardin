import streamlit as st
import random

st.set_page_config(page_title="App Botánica", page_icon="🌿")

# BASE DE DATOS EXACTA DE 33 PLANTAS
plantas = [
    {"id": "1", "comun": "Níspero", "cient": "Eriobotrya japonica", "tipo": "Angiosperma", "info": "Fruto en pomo y hoja perenne rugosa"},
    {"id": "2", "comun": "Olivo", "cient": "Olea europaea", "tipo": "Angiosperma", "info": "Fruto en drupa (aceituna) y hoja coriácea"},
    {"id": "3", "comun": "Drago", "cient": "Dracaena draco", "tipo": "Angiosperma", "info": "Planta monocotiledónea de savia roja"},
    {"id": "4", "comun": "Yuca", "cient": "Yucca elephantipes", "tipo": "Angiosperma", "info": "Hoja en forma de espada, muy resistente"},
    {"id": "5", "comun": "Naranjo", "cient": "Citrus sinensis", "tipo": "Angiosperma", "info": "Fruto en hesperidio (naranja)"},
    {"id": "6", "comun": "Cítrico", "cient": "Citrus", "tipo": "Angiosperma", "info": "Género que incluye limones y naranjas"},
    {"id": "7", "comun": "Yuca de jardín", "cient": "Yucca gloriosa", "tipo": "Angiosperma", "info": "Hoja rígida y terminada en espina"},
    {"id": "8", "comun": "Aspidistra", "cient": "Aspidistra elatior", "tipo": "Angiosperma", "info": "Planta de sombra, hoja muy ancha"},
    {"id": "9", "comun": "Geranio", "cient": "Pelargonium hortorum", "tipo": "Angiosperma", "info": "Hoja circular y flores vistosas"},
    {"id": "10", "comun": "Agave", "cient": "Agave attenuata", "tipo": "Angiosperma", "info": "Suculenta sin espinas, forma de roseta"},
    {"id": "11", "comun": "Pino de Norfolk", "cient": "Araucaria heterophylla", "tipo": "Gimnosperma", "info": "Conífera de ramas simétricas"},
    {"id": "12", "comun": "Araucaria", "cient": "Araucaria columnaris", "tipo": "Gimnosperma", "info": "Porte columnar y escamas densas"},
    {"id": "13", "comun": "Evónimo", "cient": "Euonymus japonicus", "tipo": "Angiosperma", "info": "Arbusto de hoja brillante serrada"},
    {"id": "14", "comun": "Maguey morado", "cient": "Tradescantia spathacea", "tipo": "Angiosperma", "info": "Hoja verde arriba y púrpura debajo"},
    {"id": "15", "comun": "Laurel", "cient": "Laurus nobilis", "tipo": "Angiosperma", "info": "Hoja aromática usada en cocina"},
    {"id": "16", "comun": "Palmera abanico", "cient": "Washingtonia robusta", "tipo": "Angiosperma", "info": "Hoja palmada con filamentos blancos"},
    {"id": "17", "comun": "Limonero", "cient": "Citrus limon", "tipo": "Angiosperma", "info": "Fruto ácido (limón)"},
    {"id": "18", "comun": "Flor de Pascua", "cient": "Euphorbia pulcherrima", "tipo": "Angiosperma", "info": "Brácteas rojas (hojas modificadas)"},
    {"id": "19", "comun": "Aloe Vera", "cient": "Aloe vera", "tipo": "Angiosperma", "info": "Suculenta medicinal con gel interior"},
    {"id": "20", "comun": "Morera", "cient": "Morus alba", "tipo": "Angiosperma", "info": "Hoja caduca, alimento del gusano de seda"},
    {"id": "21", "comun": "Cica", "cient": "Cycas revoluta", "tipo": "Gimnosperma", "info": "Fósil viviente, semillas desnudas"},
    {"id": "22", "comun": "Cinta", "cient": "Chlorophytum comosum", "tipo": "Angiosperma", "info": "Hoja estolonífera (malamadre)"},
    {"id": "23", "comun": "Costilla Adán", "cient": "Monstera deliciosa", "tipo": "Angiosperma", "info": "Hojas con fenestraciones (agujeros)"},
    {"id": "24", "comun": "Hibisco", "cient": "Hibiscus rosa-sinensis", "tipo": "Angiosperma", "info": "Flor con estambre prominente"},
    {"id": "25", "comun": "Ficus caucho", "cient": "Ficus elastica", "tipo": "Angiosperma", "info": "Hoja grande y coriácea"},
    {"id": "26", "comun": "Buganvilla", "cient": "Bougainvillea glabra", "tipo": "Angiosperma", "info": "Trepadora con brácteas de colores"},
    {"id": "27", "comun": "Potus", "cient": "Epipremnum aureum", "tipo": "Angiosperma", "info": "Liana trepadora variegada"},
    {"id": "28", "comun": "Sansevieria", "cient": "Dracaena trifasciata", "tipo": "Angiosperma", "info": "Hoja crasa vertical (lengua suegra)"},
    {"id": "29", "comun": "Romero", "cient": "Salvia rosmarinus", "tipo": "Angiosperma", "info": "Arbusto aromático mediterráneo"},
    {"id": "30", "comun": "Diente león", "cient": "Taraxacum officinale", "tipo": "Angiosperma", "info": "Flor amarilla y vilanos para el viento"},
    {"id": "31", "comun": "Árbol cielo", "cient": "Ailanthus altissima", "tipo": "Angiosperma", "info": "Hoja compuesta muy larga"},
    {"id": "32", "comun": "Aligustre", "cient": "Ligustrum japonicum", "tipo": "Angiosperma", "info": "Hojas opuestas muy brillantes"},
    {"id": "33", "comun": "Madreselva", "cient": "Lonicera japonica", "tipo": "Angiosperma", "info": "Flor tubular muy perfumada"}
]

# Inicialización
if 'puntos' not in st.session_state:
    st.session_state.puntos = 0
    st.session_state.pregunta = random.choice(plantas)
    st.session_state.modo = random.choice(["cientifico", "tipo"])

p = st.session_state.pregunta
modo = st.session_state.modo

st.title("🌿 Challenge Botánico")
st.write(f"Puntos: **{st.session_state.puntos}**")

# Mostrar imagen ajustada
st.image(f"{p['id']}.jpg", use_container_width=True)

if modo == "cientifico":
    label = f"¿Nombre científico de: {p['comun']}?"
    correcta = p['cient']
else:
    label = f"¿Es Angiosperma o Gimnosperma?"
    correcta = p['tipo']

st.info(f"Pista: {p['info']}")

with st.form("quiz_form"):
    rta = st.text_input(label).strip()
    enviado = st.form_submit_button("Comprobar")
    
    if enviado:
        if rta.lower() == correcta.lower():
            st.success("✨ ¡Acierto!")
            st.session_state.puntos += 1
            st.balloons()
        else:
            st.error(f"❌ Fallo. Era: {correcta}")

if st.button("Siguiente Planta ➡️"):
    st.session_state.pregunta = random.choice(plantas)
    st.session_state.modo = random.choice(["cientifico", "tipo"])
    st.rerun()