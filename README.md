# 🧠 Modelo IA para Predicción de Problemas Cardíacos

Este proyecto es una aplicación web desarrollada con **Streamlit** que utiliza un modelo de **machine learning (SVC)** para predecir si una persona tiene riesgo de sufrir problemas cardíacos. La predicción se realiza en base a dos variables clínicas: **edad** y **colesterol**.

---

## 🖼️ Vista previa

![Banner](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUAjsoawWLXxiMg1ThfhfluWfh-n0eXFIGKA&s)

---

## 🚀 ¿Cómo funciona?

1. El usuario ingresa su edad y nivel de colesterol a través de la barra lateral.
2. Los datos se normalizan utilizando un `StandardScaler`.
3. Un modelo previamente entrenado (`svc_model.jb`) predice si hay riesgo de enfermedad cardíaca.
4. Se muestra un mensaje visual con una imagen según el resultado:

- ✅ No hay riesgo:

  ![Saludable](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBM-KPKbnV-4ZluLxeo08GamAQItMuNMq3cw&s)

- ❌ Hay riesgo:

  ![Enfermo](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuXrLD59qBsERfpbDe6acGUhsgfHoK1btS2Q&s)

---

## 📦 Requisitos

Instala las dependencias con:

```bash
pip install -r requirements.txt
