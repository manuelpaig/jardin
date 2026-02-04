import streamlit as st
import random
import os
from PIL import Image, ImageOps

st.set_page_config(page_title="Mi Jardín Botánico", page_icon="🌿")

# BASE DE DATOS COMPLETA Y CORREGIDA (33 PLANTAS)
plantas = [
    {"id": "1", "comun": "Níspero", "cient": "Eriobotrya japonica", "tipo": "Angiosperma", "extra": "Fruto: Pomo. Hoja: Perenne rugosa"},
    {"id": "2", "comun": "Olivo", "cient": "Olea europaea", "tipo": "Angiosperma", "extra": "Fruto: Drupa (Aceituna). Hoja: Elíptica"},
    {"id": "3", "comun": "Drago", "cient": "Dracaena draco", "tipo": "Angiosperma", "extra": "Savia roja. Hoja: Ensiforme"},
    {"id": "4", "comun": "Yuca", "cient": "Yucca elephantipes", "tipo": "Angiosperma", "extra": "Hoja lisa sin espina terminal"},
    {"id": "5", "comun": "Naranjo", "cient": "Citrus sinensis", "tipo": "Angiosperma", "extra": "Fruto: Hesperidio. Hoja: Pecíolo alado"},
    {"id": "6", "comun": "Cítrico", "cient": "Citrus", "tipo": "Angiosperma", "extra": "Género de frutales con aceites esenciales"},
    {"id": "7", "comun": "Yuca de jardín", "cient": "Yucca gloriosa", "tipo": "Angiosperma", "extra": "Hoja rígida con espina terminal"},
    {"id": "8", "comun": "Aspidistra", "cient": "Aspidistra elatior", "tipo": "Angiosperma", "extra": "Hoja muy ancha de sombra"},
    {"id": "9", "comun": "Geranio", "cient": "Pelargonium hortorum", "tipo": "Angiosperma", "extra": "Hoja circular lobulada"},
    {"id": "10", "comun": "Agave", "cient": "Agave attenuata", "tipo": "Angiosperma", "extra": "Suculenta. Roseta sin espinas"},
    {"id": "11", "comun": "Pino de Norfolk", "cient": "Araucaria heterophylla", "tipo": "Gimnosperma", "extra": "Conífera. Ramas simétricas"},
    {"id": "12", "comun": "Araucaria", "cient": "Araucaria columnaris", "tipo": "Gimnosperma", "extra": "Porte columnar muy estrecho"},
    {"id": "13", "comun": "Evónimo", "cient": "Euonymus japonicus", "tipo": "Angiosperma", "extra": "Arbusto. Hoja brillante serrada"},
    {"id": "14", "comun": "Maguey morado", "cient": "Tradescantia spathacea", "tipo": "Angiosperma", "extra": "Hoja bicolor (verde/púrpura)"},
    {"id": "15", "comun": "Laurel", "cient": "Laurus nobilis", "tipo": "Angiosperma", "extra": "Hoja aromática culinaria"},
    {"id": "16", "comun": "Palmera abanico", "cient": "Washingtonia robusta", "tipo": "Angiosperma", "extra": "Hoja palmada con hilos"},
    {"id": "17", "comun": "Limonero", "cient": "Citrus limon", "tipo": "Angiosperma", "extra": "Fruto ácido (Limón)"},
    {"id": "18", "comun": "Flor de Pascua", "cient": "Euphorbia pulcherrima", "tipo": "Angiosperma", "extra": "Brácteas rojas llamativas"},
    {"id": "19", "comun": "Aloe Vera", "cient": "Aloe vera", "tipo": "Angiosperma", "extra": "Medicinal. Hoja suculenta con dientes"},
    {"id": "20", "comun": "Naranjo", "cient": "Citrus sinensis", "tipo": "Angiosperma", "extra": "Segundo ejemplar de naranjo"},
    {"id": "21", "comun": "Cica", "cient": "Cycas revoluta", "tipo": "Gimnosperma", "extra": "Fósil viviente. Semillas desnudas"},
    {"id": "22", "comun": "Cinta", "cient": "Chlorophytum comosum", "tipo": "Angiosperma", "extra": "Hojas estoloníferas (malamadre)"},
    {"id": "23", "comun": "Costilla de Adán", "cient": "Monstera deliciosa", "tipo": "Angiosperma", "extra": "Hojas con agujeros (fenestraciones)"},
    {"id": "24", "comun": "Hibisco", "cient": "Hibiscus rosa-sinensis", "tipo": "Angiosperma", "extra": "Flor con columna estaminal larga"},
    {"id": "25", "comun": "Ficus caucho", "cient": "Ficus elastica", "tipo": "Angiosperma", "extra": "Hoja grande coriácea con látex"},
    {"id": "26", "comun": "Buganvilla", "cient": "Bougainvillea glabra", "tipo": "Angiosperma", "extra": "Trepadora. Brácteas coloridas"},
    {"id": "27", "comun": "Potus", "cient": "Epipremnum aureum", "tipo": "Angiosperma", "extra": "Liana de interior variegada"},
    {"id": "28", "comun": "Sansevieria", "cient": "Dracaena trifasciata", "tipo": "Angiosperma", "extra": "Hoja espada vertical"},
    {"id": "29", "comun": "Romero", "cient": "Salvia rosmarinus", "tipo": "Angiosperma", "extra": "Arbusto aromático lineal"},
    {"id": "30", "comun": "Diente de león", "cient": "Taraxacum officinale", "tipo": "Angiosperma", "extra": "Inflorescencia amarilla (aquenio)"},
    {"id": "31", "comun": "Árbol del cielo", "cient": "Ailanthus altissima", "tipo": "Angiosperma", "extra": "Hoja compuesta muy larga pinnada"},
    {"id": "32", "comun": "Aligustre", "cient": "Ligustrum japonicum", "tipo": "Angiosperma", "extra": "Hoja opuesta brillante"},
    {"id": "33", "comun": "Trébol", "cient": "Trifolium repens", "tipo": "Angiosperma", "extra": "Hoja: Trifoliada. Fruto: Legumbre pequeña"}
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
    
    st.title("🌿 Herbario Interactivo")
    st.write(f"**Progreso:** {st.session_state.indice + 1}/33 | **Puntos:** {st.session_state.puntos}")

    # --- BLOQUE DE IMAGEN CON CORRECCIÓN DE GIRO ---
    nombre_img = f"{p['id']}.jpg.jpg"
    if os.path.exists(nombre_img):
        try:
            img = Image.open(nombre_img)
            img = ImageOps.exif_transpose(img) # Corrige el giro automático
            st.image(img, use_container_width=True)
        except Exception as e:
            st.error(f"Error al cargar la imagen: {e}")
    else:
        st.error(f"No encuentro el archivo: {nombre_img}")

    # FORMULARIO DE RESPUESTA
    with st.form("quiz_form"):
        rta = st.text_input("¿Cómo se llama esta planta?").strip().lower()
        enviado = st.form_submit_button("Comprobar")
        
        if enviado:
            st.session_state.respondido = True
            def limpiar(t): return t.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
            
            if limpiar(rta) == limpiar(p['comun'].lower()):
                st.success(f"✅ ¡Correcto! Es un {p['comun']}")
                st.session_state.puntos += 1
            else:
                st.error(f"❌ Es un {p['comun']}")
            
            st.info(f"🧬 **Datos PRO:** {p['extra']} | **Clasificación:** {p.get('tipo', 'Angiosperma')}")

    # BOTÓN SIGUIENTE (Fuera del formulario)
    if st.session_state.respondido:
        if st.button("Siguiente Planta ➡️"):
            st.session_state.indice += 1
            st.session_state.respondido = False
            st.rerun()

else:
    st.balloons()
    st.title("🏆 ¡Fin del Examen!")
    st.write(f"Tu puntuación final es de **{st.session_state.puntos} de 33**.")
    if st.button("Reiniciar Juego"):
        st.session_state.puntos = 0
        st.session_state.indice = 0
        random.shuffle(
