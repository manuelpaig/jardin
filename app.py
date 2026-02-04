import streamlit as st
import random
import os
from PIL import Image, ImageOps

st.set_page_config(page_title="Mi Jardín Botánico", page_icon="🌿")

# BASE DE DATOS COMPLETA Y REVISADA
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
    {"id": "21", "comun": "Cica", "cient": "Cycas
