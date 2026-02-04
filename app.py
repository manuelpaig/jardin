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
    {"id": "32", "comun": "Aligustre", "cient": "Ligustrum japonicum", "tipo
