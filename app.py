import streamlit as st
import random
import os
from PIL import Image, ImageOps

st.set_page_config(page_title="Herbario", page_icon="🌿")

# LISTA DEFINITIVA (1-33) CON TODAS TUS CORRECCIONES
plantas = [
    {"id": "1", "comun": "Níspero", "extra": "Fruto: Pomo. Hoja rugosa"},
    {"id": "2", "comun": "Olivo", "extra": "Fruto: Aceituna. Hoja elíptica"},
    {"id": "3", "comun": "Drago", "extra": "Savia roja. Hoja ensiforme"},
    {"id": "4", "comun": "Yuca", "extra": "Hoja lisa sin espina terminal"},
    {"id": "5", "comun": "Naranjo", "extra": "Fruto: Hesperidio (Naranja)"},
    {"id": "6", "comun": "Cítrico", "extra": "Aromático con aceites esenciales"},
    {"id": "7", "comun": "Yuca de jardín", "extra": "Hoja con espina terminal"},
    {"id": "8", "comun": "Aspidistra", "extra": "Planta de sombra, hojas anchas"},
    {"id": "9", "comun": "Geranio", "extra": "Hoja circular lobulada"},
    {"id": "10", "comun": "Agave", "extra": "Suculenta sin espinas laterales"},
    {"id": "11", "comun": "Flor de Pascua", "extra": "Brácteas rojas llamativas"},
    {"id": "12", "comun": "Araucaria", "extra": "Porte columnar estrecho"},
    {"id": "13", "comun": "Pino", "extra": "Gimnosperma. Hojas de aguja"},
    {"id": "14", "comun": "Araucaria", "extra": "Segundo ejemplar (Pino de Norfolk)"},
    {"id": "15", "comun": "Araucaria", "extra": "Tercer ejemplar de Araucaria"},
    {"id": "16", "comun": "Palmera abanico", "extra": "Hoja palmada con hilos"},
    {"id": "17", "comun": "Maguey morado", "extra": "Haz verde y envés púrpura"},
    {"id": "18", "comun": "Laurel", "extra": "Hoja coriácea y aromática"},
    {"id": "19", "comun": "Aloe Vera", "extra": "Medicinal. Hoja con dientes"},
    {"id": "20", "comun": "Naranjo", "extra": "Segundo ejemplar de naranjo"},
    {"id": "21", "comun": "Cica", "extra": "Gimnosperma. Semillas desnudas"},
    {"id": "22", "comun": "Cinta", "extra": "Hojas estoloníferas"},
    {"id": "23", "comun": "Costilla de Adán", "extra": "Hojas con fenestraciones"},
    {"id": "24", "comun": "Maguey morado", "extra": "Segundo ejemplar de Maguey"},
    {"id": "25", "comun": "Ficus caucho", "extra": "Hoja con látex blanco"},
    {"id": "26", "comun": "Buganvilla", "extra": "Trepadora con brácteas"},
    {"id": "27", "comun": "Potus", "extra": "Liana de interior variegada"},
    {"id": "28", "comun": "Sansevieria", "extra": "Hoja vertical rígida"},
    {"id": "29", "comun": "Romero", "extra": "Arbusto aromático lineal"},
    {"id": "30", "comun": "Diente de león", "extra": "Inflorescencia amarilla"},
    {"id": "31", "comun": "Árbol del cielo", "extra": "Hoja pinnada muy larga"},
    {"id": "32", "comun": "Grama", "extra": "Césped rastrero (Agropyron)"},
    {"id": "33", "comun": "Trébol", "extra": "Hoja trifoliada. Leguminosa"}
]

# Inicialización
if 'puntos' not in st
