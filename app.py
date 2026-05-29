import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# =========================================================
# CONFIGURACION GENERAL
# =========================================================

plt.style.use("ggplot")
plt.ion()

# =========================================================
# FUNCION PARA MOSTRAR GRAFICOS
# STREAMLIT + TERMINAL
# =========================================================

def mostrar_grafico(fig):

    fig.tight_layout()

    # STREAMLIT
    st.pyplot(fig)

    # TERMINAL
    plt.show(block=False)
    plt.pause(0.1)

# =========================================================
# CONFIGURACION DE PAGINA
# =========================================================

st.set_page_config(
    page_title="Procesamiento Estadistico",
    page_icon="📊",
    layout="wide"
)

# =========================================================
# TITULO PRINCIPAL
# =========================================================

st.title("📊 PROCESAMIENTO ESTADISTICO CON PYTHON")

st.markdown("---")

# =========================================================
# FASE 1
# CARGA DE DATOS CSV
# =========================================================

st.header("📌 FASE 1: CARGA DE DATOS")

st.write("Lectura del archivo estudiantes.csv")

# =========================================================
# LEER ARCHIVO CSV
# =========================================================

df = pd.read_csv("datos_estudiantes.csv")
# =========================================================
# CANTIDAD DE DATOS
# =========================================================

cantidad_datos = len(df)

st.success(f"✅ Cantidad total de registros: {cantidad_datos}")

# =========================================================
# MOSTRAR BASE DE DATOS
# =========================================================

st.subheader("📋 BASE DE DATOS")

st.dataframe(df, use_container_width=True)

# =========================================================
# TERMINAL
# =========================================================

print("\n====================================================")
print("                 BASE DE DATOS")
print("====================================================")

print(df)

print("\nCantidad total de registros =", cantidad_datos)

# ----------------------
# FASE 2 VARIABLES CUALITATIVAS
# ----------------------

st.markdown("---")

st.header("📌 FASE 2: VARIABLES CUALITATIVAS")

st.write("Variable cualitativa: carrera")

# =========================================================
# TABLA DE FRECUENCIA CUALITATIVA
# =========================================================

frecuencia_carrera = df["carrera"].value_counts()

tabla_cualitativa = pd.DataFrame({
    "Carrera": frecuencia_carrera.index,
    "fi": frecuencia_carrera.values
})

tabla_cualitativa["hi"] = (
    tabla_cualitativa["fi"] /
    tabla_cualitativa["fi"].sum()
)

tabla_cualitativa["hip"] = (
    tabla_cualitativa["hi"] * 100
)

tabla_cualitativa["Fi"] = (
    tabla_cualitativa["fi"].cumsum()
)

tabla_cualitativa["Hi"] = (
    tabla_cualitativa["hi"].cumsum()
)

tabla_cualitativa = tabla_cualitativa.round(4)

# =========================================================
# MOSTRAR TABLA
# =========================================================

st.subheader("📋 Tabla de Frecuencia Cualitativa")

st.dataframe(tabla_cualitativa, use_container_width=True)

# =========================================================
# TERMINAL
# =========================================================

print("\n====================================================")
print("       TABLA DE FRECUENCIA CUALITATIVA")
print("====================================================")

print(tabla_cualitativa)

# =========================================================
# GRAFICO DE BARRAS
# =========================================================

st.subheader("📊 GRAFICO DE BARRAS")

fig1, ax1 = plt.subplots(figsize=(8, 4), dpi=110)

barras = ax1.bar(
    tabla_cualitativa["Carrera"],
    tabla_cualitativa["fi"],
    color="cornflowerblue",
    edgecolor="black"
)

ax1.set_title(
    "DISTRIBUCION POR CARRERA",
    fontsize=14,
    fontweight="bold"
)

ax1.set_xlabel("Carreras")
ax1.set_ylabel("Frecuencia")

ax1.grid(True, linestyle="--", alpha=0.4)

plt.xticks(rotation=15)

for barra in barras:

    altura = barra.get_height()

    ax1.text(
        barra.get_x() + barra.get_width()/2,
        altura + 0.1,
        str(int(altura)),
        ha='center',
        fontsize=9
    )

mostrar_grafico(fig1)

# =========================================================
# GRAFICO DE TORTA
# =========================================================

st.subheader("📊 GRAFICO DE TORTA")

fig2, ax2 = plt.subplots(figsize=(6, 6), dpi=110)

ax2.pie(
    tabla_cualitativa["fi"],
    labels=tabla_cualitativa["Carrera"],
    autopct="%1.1f%%",
    startangle=90
)

ax2.set_title(
    "DISTRIBUCION POR CARRERA",
    fontsize=14,
    fontweight="bold"
)

mostrar_grafico(fig2)

# =========================================================
# FASE 3
# DATOS NO AGRUPADOS
# =========================================================

st.markdown("---")

st.header("📌 FASE 3: DATOS NO AGRUPADOS")

st.write("Variable cuantitativa discreta: nota")

# DATOS NO AGRUPADOS: NOTA
# =========================================================
# TABLA DE FRECUENCIA DISCRETA
# =========================================================

frecuencia_nota = (
    df["nota"]
    .value_counts()
    .sort_index()
)

tabla_discreta = pd.DataFrame({
    "Nota": frecuencia_nota.index,
    "fi": frecuencia_nota.values
})

tabla_discreta["hi"] = (
    tabla_discreta["fi"] /
    tabla_discreta["fi"].sum()
)

tabla_discreta["hip"] = (
    tabla_discreta["hi"] * 100
)

tabla_discreta["Fi"] = (
    tabla_discreta["fi"].cumsum()
)

tabla_discreta["Hi"] = (
    tabla_discreta["hi"].cumsum()
)

tabla_discreta = tabla_discreta.round(4)

# =========================================================
# MOSTRAR TABLA
# =========================================================

st.subheader("📋 Tabla de Frecuencia Discreta")

st.dataframe(tabla_discreta, use_container_width=True)

# =========================================================
# TERMINAL
# =========================================================
print("\n====================================================")
print("              DATOS NO AGRUPADOS")
print("====================================================")

print("\n====================================================")
print("         TABLA DE FRECUENCIA DISCRETA")
print("====================================================")

print(tabla_discreta)

# =========================================================
# MEDIDAS ESTADISTICAS
# =========================================================

st.subheader("📋 MEDIDAS ESTADISTICAS")

media = df["nota"].mean()
mediana = df["nota"].median()
moda = df["nota"].mode()[0]
varianza = df["nota"].var()
desviacion = df["nota"].std()

valor_maximo_nota = df["nota"].max()
valor_minimo_nota = df["nota"].min()

rango_nota = valor_maximo_nota - valor_minimo_nota

tabla_medidas = pd.DataFrame({
    "Medida": [
        "Media",
        "Mediana",
        "Moda",
        "Varianza",
        "Desviacion Estandar",
        "Valor Maximo",
        "Valor Minimo",
        "Rango"
    ],
    "Valor": [
        round(media, 4),
        round(mediana, 4),
        round(moda, 4),
        round(varianza, 4),
        round(desviacion, 4),
        valor_maximo_nota,
        valor_minimo_nota,
        rango_nota
    ]
})

st.dataframe(tabla_medidas, use_container_width=True)

# =========================================================
# TERMINAL
# =========================================================

print("\n====================================================")
print("           MEDIDAS ESTADISTICAS")
print("====================================================")

print(tabla_medidas)

# =========================================================
# GRAFICO DE BASTON
# =========================================================

st.subheader("📊 GRAFICO DE BASTON")

fig3, ax3 = plt.subplots(figsize=(8, 4), dpi=110)

markerline, stemlines, baseline = ax3.stem(
    tabla_discreta["Nota"],
    tabla_discreta["fi"]
)

plt.setp(stemlines, linewidth=2)
plt.setp(markerline, markersize=7)

ax3.set_title(
    "DISTRIBUCION DE NOTAS",
    fontsize=14,
    fontweight="bold"
)

ax3.set_xlabel("Notas")
ax3.set_ylabel("Frecuencia")

ax3.grid(True, linestyle="--", alpha=0.4)

mostrar_grafico(fig3)

# =========================================================
# FASE 4
# DATOS AGRUPADOS
# =========================================================

st.markdown("---")

st.header("📌 FASE 4: DATOS AGRUPADOS")

st.write("Variable cuantitativa continua: edad")

# =========================================================
# PARAMETROS
# =========================================================

n = len(df["edad"])

valor_maximo = df["edad"].max()
valor_minimo = df["edad"].min()

rango = valor_maximo - valor_minimo

k = int(1 + 3.322 * np.log10(n))

amplitud = int(np.ceil(rango / k))

# =========================================================
# MOSTRAR PARAMETROS
# =========================================================

st.subheader("📋 Parametros de Sturges")

st.write("Numero de datos =", n)
st.write("Valor maximo =", valor_maximo)
st.write("Valor minimo =", valor_minimo)
st.write("Rango =", rango)
st.write("Numero de clases =", k)
st.write("Amplitud =", amplitud)

# =========================================================
# TERMINAL
# =========================================================

print("\n====================================================")
print("             PARAMETROS DE STURGES")
print("====================================================")

print("Numero de datos =", n)
print("Valor maximo =", valor_maximo)
print("Valor minimo =", valor_minimo)
print("Rango =", rango)
print("Numero de clases =", k)
print("Amplitud =", amplitud)

# =========================================================
# CREAR INTERVALOS
# =========================================================

intervalos = pd.interval_range(
    start=valor_minimo,
    end=valor_maximo + amplitud,
    freq=amplitud
)

df["Intervalos"] = pd.cut(
    df["edad"],
    bins=intervalos
)

# =========================================================
# TABLA AGRUPADA
# =========================================================

tabla_agrupada = (
    df.groupby("Intervalos")
    .size()
    .reset_index(name="fi")
)

tabla_agrupada["Intervalos_Texto"] = (
    tabla_agrupada["Intervalos"]
    .apply(lambda x: f"{int(x.left)} - {int(x.right)}")
)

tabla_agrupada["Marca_Clase"] = (
    tabla_agrupada["Intervalos"]
    .apply(lambda x: (x.left + x.right) / 2)
)

tabla_agrupada["hi"] = (
    tabla_agrupada["fi"] /
    tabla_agrupada["fi"].sum()
)

tabla_agrupada["hip"] = (
    tabla_agrupada["hi"] * 100
)

tabla_agrupada["Fi"] = (
    tabla_agrupada["fi"].cumsum()
)

tabla_agrupada["Hi"] = (
    tabla_agrupada["hi"].cumsum()
)

tabla_agrupada = tabla_agrupada.round(4)

tabla_final = tabla_agrupada[[
    "Intervalos_Texto",
    "Marca_Clase",
    "fi",
    "hi",
    "hip",
    "Fi",
    "Hi"
]]

# =========================================================
# MOSTRAR TABLA
# =========================================================

st.subheader("📋 Tabla de Datos Agrupados")

st.dataframe(tabla_final, use_container_width=True)

# =========================================================
# TERMINAL
# =========================================================

print("\n====================================================")
print("           TABLA DE DATOS AGRUPADOS")
print("====================================================")

print(tabla_final)

# =========================================================
# HISTOGRAMA
# =========================================================

st.subheader("📊 HISTOGRAMA")

fig4, ax4 = plt.subplots(figsize=(8, 4), dpi=110)

ax4.hist(
    df["edad"],
    bins=k,
    color="skyblue",
    edgecolor="black"
)

ax4.set_title(
    "HISTOGRAMA DE EDADES",
    fontsize=14,
    fontweight="bold"
)

ax4.set_xlabel("Edad")
ax4.set_ylabel("Frecuencia")

ax4.grid(True, linestyle="--", alpha=0.4)

mostrar_grafico(fig4)

# =========================================================
# POLIGONO DE FRECUENCIA
# =========================================================

st.subheader("📊 POLIGONO DE FRECUENCIA")

fig5, ax5 = plt.subplots(figsize=(8, 4), dpi=110)

ax5.plot(
    tabla_agrupada["Marca_Clase"],
    tabla_agrupada["fi"],
    marker="o",
    linewidth=3,
    color="blue"
)

ax5.set_title(
    "POLIGONO DE FRECUENCIA",
    fontsize=14,
    fontweight="bold"
)

ax5.set_xlabel("Marca de Clase")
ax5.set_ylabel("Frecuencia")

ax5.grid(True, linestyle="--", alpha=0.4)

mostrar_grafico(fig5)

# =========================================================
# HISTOGRAMA + POLIGONO
# =========================================================

st.subheader("📊 HISTOGRAMA Y POLIGONO JUNTOS")

fig6, ax6 = plt.subplots(figsize=(8, 4), dpi=110)

ax6.hist(
    df["edad"],
    bins=k,
    color="lightblue",
    edgecolor="black"
)

ax6.plot(
    tabla_agrupada["Marca_Clase"],
    tabla_agrupada["fi"],
    marker="o",
    linewidth=3,
    color="red"
)

ax6.set_title(
    "HISTOGRAMA Y POLIGONO",
    fontsize=14,
    fontweight="bold"
)

ax6.set_xlabel("Edad")
ax6.set_ylabel("Frecuencia")

ax6.grid(True, linestyle="--", alpha=0.4)

mostrar_grafico(fig6)

# =========================================================
# OJIVA
# =========================================================

st.subheader("📊 OJIVA")

fig7, ax7 = plt.subplots(figsize=(8, 4), dpi=110)

ax7.plot(
    tabla_agrupada["Marca_Clase"],
    tabla_agrupada["Fi"],
    marker="o",
    linewidth=3,
    color="green"
)

ax7.set_title(
    "OJIVA",
    fontsize=14,
    fontweight="bold"
)

ax7.set_xlabel("Marca de Clase")
ax7.set_ylabel("Frecuencia Acumulada")

ax7.grid(True, linestyle="--", alpha=0.4)

mostrar_grafico(fig7)

# =========================================================
# FINAL DEL PROGRAMA
# =========================================================

st.markdown("---")

st.success("✅ PROGRAMA EJECUTADO CORRECTAMENTE")

print("\n====================================================")
print("      PROGRAMA EJECUTADO CORRECTAMENTE")
print("====================================================")

# =========================================================
# MANTENER ABIERTAS LAS VENTANAS EN TERMINAL
# =========================================================

plt.ioff()
plt.show()
