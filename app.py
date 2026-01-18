import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(page_title="Bogotá Security Radar", layout="wide")

def load_data():
    conn = sqlite3.connect('security_db.db')
    query = "SELECT * FROM crime_data"
    df = pd.read_sql(query, conn)
    conn.close()
    df['fecha_hecho'] = pd.to_datetime(df['fecha_hecho'])
    return df

try:
    df = load_data()
except:
    st.error(" Error: Ejecuta 'python data_gen.py' primero.")
    st.stop()

st.title(" Bogotá Security Radar")
st.markdown("### Monitor de Incidentes en Tiempo Real")

col1, col2, col3 = st.columns(3)
col1.metric("Total Incidentes", f"{len(df):,}")
col2.metric("Localidad Crítica", df['localidad'].mode()[0])
col3.metric("Hora Pico", f"{df['hora_hecho'].mode()[0]}:00 h")

st.divider()

c_filter1, c_filter2 = st.columns(2)
localidad = c_filter1.multiselect("Filtrar Localidad", df['localidad'].unique(), default=df['localidad'].unique())
modalidad = c_filter2.multiselect("Filtrar Modalidad", df['modalidad'].unique(), default=df['modalidad'].unique())

filtered_df = df[(df['localidad'].isin(localidad)) & (df['modalidad'].isin(modalidad))]


col_map, col_chart = st.columns([2, 1]) 

with col_map:
    st.subheader(" Ubicación de Incidentes")
    st.map(filtered_df, latitude='latitud', longitude='longitud', size=20, color='#FF0000')

with col_chart:
    st.subheader(" Tendencia Horaria")
    st.bar_chart(filtered_df['hora_hecho'].value_counts().sort_index())
    
    st.subheader(" Top Zonas")
    st.dataframe(
        filtered_df['localidad'].value_counts().head(5), 
        use_container_width=True
    )