import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# ----------------------
# Configuración de la página
# ----------------------
st.set_page_config(page_title="Estadística Descriptiva", layout="wide")
st.title("📊 Procesamiento Estadístico - Datos de Estudiantes")

# ----------------------
# Carga de Datos
# ----------------------
@st.cache_data
def cargar_datos():
    df = pd.read_csv("datos_estudiantes.csv")
    return df

df = cargar_datos()

st.subheader("📋 Vista Previa de los Datos")
st.dataframe(df, use_container_width=True)

# ----------------------
# FASE 2: Variable Cualitativa - Carrera
# ----------------------
st.header("🔹 FASE 2: Variable Cualitativa (Carrera)")
freq_carrera = df['carrera'].value_counts().reset_index()
freq_carrera.columns = ['Carrera', 'Frecuencia Absoluta']
freq_carrera['Frecuencia Relativa'] = freq_carrera['Frecuencia Absoluta'] / len(df)
freq_carrera['Porcentaje (%)'] = freq_carrera['Frecuencia Relativa'] * 100
st.dataframe(freq_carrera, use_container_width=True)

# Gráfico de Barras
fig1, ax1 = plt.subplots(figsize=(8, 4))
ax1.bar(freq_carrera['Carrera'], freq_carrera['Frecuencia Absoluta'], color='#1f77b4')
ax1.set_title('Distribución por Carrera')
ax1.grid(axis='y', alpha=0.3)
st.pyplot(fig1)

# Gráfico de Torta
fig2, ax2 = plt.subplots(figsize=(5,5))
ax2.pie(freq_carrera['Frecuencia Absoluta'], labels=freq_carrera['Carrera'], autopct='%1.1f%%', startangle=90)
ax2.set_title('Porcentaje por Carrera')
ax2.axis('equal')
st.pyplot(fig2)

# ----------------------
# FASE 3: Variable Cuantitativa Discreta - Materias Aprobadas
# ----------------------
st.header("🔹 FASE 3: Variable Cuantitativa Discreta (Materias Aprobadas)")
freq_materias = df['materias_aprobadas'].value_counts().sort_index().reset_index()
freq_materias.columns = ['Materias Aprobadas', 'Frecuencia Absoluta']
freq_materias['Frecuencia Acumulada'] = freq_materias['Frecuencia Absoluta'].cumsum()
st.dataframe(freq_materias, use_container_width=True)

# Gráfico de Bastón
fig3, ax3 = plt.subplots(figsize=(8, 4))
ax3.stem(freq_materias['Materias Aprobadas'], freq_materias['Frecuencia Absoluta'], basefmt=" ")
ax3.set_title('Frecuencia de Materias Aprobadas')
ax3.set_xlabel('Número de Materias')
ax3.set_ylabel('Frecuencia')
ax3.grid(axis='y', alpha=0.3)
st.pyplot(fig3)

# ----------------------
# FASE 4: Datos Agrupados - EDAD (Regla de Sturges)
# ----------------------
st.header("🔹 FASE 4: Datos Agrupados - EDAD (Regla de Sturges)")

n = len(df)
valor_min = df['edad'].min()
valor_max = df['edad'].max()
rango = valor_max - valor_min
k = 1 + 3.322 * np.log10(n)
k_redondeado = int(np.round(k))
amplitud = rango / k_redondeado

col1, col2, col3, col4 = st.columns(4)
with col1: st.metric("Valor Mínimo", valor_min)
with col2: st.metric("Valor Máximo", valor_max)
with col3: st.metric("Rango", rango)
with col4: st.metric("N° Clases (Sturges)", k_redondeado)

# Crear intervalos
limites = np.linspace(valor_min, valor_max, k_redondeado + 1)
df['rango_edad'] = pd.cut(df['edad'], bins=limites, include_lowest=True)

tabla_edad = df['rango_edad'].value_counts().sort_index().reset_index()
tabla_edad.columns = ['Intervalo', 'Frecuencia Absoluta']
tabla_edad['Marca de Clase'] = tabla_edad['Intervalo'].apply(lambda x: (x.left + x.right)/2)
tabla_edad['Frecuencia Acumulada'] = tabla_edad['Frecuencia Absoluta'].cumsum()
tabla_edad['Frecuencia Relativa'] = tabla_edad['Frecuencia Absoluta'] / n

st.dataframe(tabla_edad, use_container_width=True)

# Gráficos: Histograma, Polígono y Ojiva
fig4, (ax4, ax5) = plt.subplots(1, 2, figsize=(12, 4))

# Histograma + Polígono
ax4.hist(df['edad'], bins=limites, edgecolor='black', alpha=0.6)
ax4.plot(tabla_edad['Marca de Clase'], tabla_edad['Frecuencia Absoluta'], marker='o', color='red', linewidth=2, label='Polígono')
ax4.set_title('Histograma y Polígono de Frecuencias')
ax4.legend()
ax4.grid(axis='y', alpha=0.3)

# Ojiva
ax5.plot(tabla_edad['Marca de Clase'], tabla_edad['Frecuencia Acumulada'], marker='s', color='green', linewidth=2)
ax5.set_title('Gráfico Ojiva (Frecuencia Acumulada)')
ax5.grid(True, alpha=0.3)

st.pyplot(fig4)
