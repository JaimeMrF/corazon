import streamlit as st
import joblib
import numpy as np
from PIL import Image
import requests
from io import BytesIO

# --- Cargar modelos ---
scaler = joblib.load("scaler.jb")
model = joblib.load("svc_model.jb")

# --- Configuración de página ---
st.set_page_config(
    page_title="Modelo IA para predicción de problemas cardiacos",
    layout="wide",
    page_icon="❤️"
)

# --- Mostrar banner ---
banner_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUAjsoawWLXxiMg1ThfhfluWfh-n0eXFIGKA&s"
banner_response = requests.get(banner_url)
banner_img = Image.open(BytesIO(banner_response.content))
st.image(banner_img, use_column_width=True)

# --- Título principal ---
st.title("🧠 Modelo IA para predicción de problemas cardiacos")

# --- Explicación del modelo ---
st.markdown("""
Este modelo utiliza un clasificador SVC entrenado para predecir la probabilidad de que un paciente sufra problemas cardíacos.
Se toman como entrada la edad y el nivel de colesterol, los cuales son escalados antes de la predicción para obtener resultados más precisos.
""")

# --- Sidebar con inputs ---
st.sidebar.header("🔧 Parámetros de entrada")

edad = st.sidebar.slider("Edad (años)", min_value=25, max_value=80, value=55, step=1)
colesterol = st.sidebar.slider("Colesterol (mg/dL)", min_value=120, max_value=600, value=242, step=2)

# --- Preparar datos para modelo ---
input_data = np.array([[edad, colesterol]])
input_scaled = scaler.transform(input_data)

# --- Predicción ---
prediction = model.predict(input_scaled)[0]

# --- Mostrar resultado con imagen y mensaje ---
if prediction == 0:
    # Imagen de no enfermo
    healthy_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBM-KPKbnV-4ZluLxeo08GamAQItMuNMq3cw&s"
    healthy_response = requests.get(healthy_url)
    healthy_img = Image.open(BytesIO(healthy_response.content))
    
    st.image(healthy_img, width=300)
    st.markdown(
        """
        <div style="background-color: #90EE90; color: black; padding: 20px; border-radius: 10px; font-size: 20px; text-align: center;">
        😊 <strong>No sufrirá problemas cardíacos.</strong>
        </div>
        """, unsafe_allow_html=True
    )
else:
    # Imagen de enfermo
    sick_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuXrLD59qBsERfpbDe6acGUhsgfHoK1btS2Q&s"
    sick_response = requests.get(sick_url)
    sick_img = Image.open(BytesIO(sick_response.content))
    
    st.image(sick_img, width=300)
    st.markdown(
        """
        <div style="background-color: #FF6961; color: black; padding: 20px; border-radius: 10px; font-size: 20px; text-align: center;">
        😞 <strong>Sufrirá problemas cardíacos.</strong>
        </div>
        """, unsafe_allow_html=True
    )

# --- Pie de página ---
st.markdown("---")
st.markdown("Elaborado por: Jaime Alejandro Vega Barbosa © Unab 2025")
