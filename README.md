# Bogotá Security Radar
### Real-Time Crime Analytics Dashboard

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)


## Contexto del Proyecto

La seguridad ciudadana en Bogotá requiere monitoreo ágil. Este proyecto simula un sistema de inteligencia en tiempo real para visualizar incidentes delictivos.

**Objetivo:** Crear una herramienta ligera y rápida que permita a las autoridades identificar focos de criminalidad ("Hotspots") sin la complejidad de los sistemas GIS tradicionales.


##  Tech Stack & Arquitectura

* **Ingeniería de Datos:** Generación de 15,000 registros sintéticos con distribución de probabilidad realista (clusters geográficos y picos horarios nocturnos).
* **Backend:** Base de datos **SQLite** para persistencia y consultas SQL directas.
* **Frontend:** **Streamlit** para el despliegue web.
* **Visualización:** Uso de `st.map` (OpenStreetMap) para renderizado geoespacial de alta velocidad y bajo consumo de recursos.


## Vista del Dashboard

El sistema permite filtrar miles de puntos en milisegundos, mostrando la ubicación exacta de incidentes y las tendencias horarias.

![Bogota Security Dashboard](dashboard_preview.png)

*(Nota: Los datos mostrados son generados sintéticamente para fines de demostración técnica).*


##  Cómo ejecutar localmente

```bash
# 1. Clonar el repositorio
git clone [https://github.com/DiegoJimenez14/Bogota-Security-Radar.git](https://github.com/DiegoJimenez14/Bogota-Security-Radar.git)

# 2. Instalar dependencias
pip install pandas streamlit matplotlib

# 3. Generar datos y lanzar la App
python data_gen.py
streamlit run app.py
