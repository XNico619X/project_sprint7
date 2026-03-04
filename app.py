import pandas as pd
import streamlit as st
import plotly.express as px

vehicles = pd.read_csv('vehicles_us.csv')  # leer los datos

st.header('anuncios de venta de coches')  # Titulo de la aplicación

hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(vehicles, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Nuevo: botón para construir un gráfico de dispersión
scatter_button = st.button('Construir dispersión')  # crear botón para dispersión

if scatter_button:
    st.write('Creación de un gráfico de dispersión (odómetro vs precio)')

    # eliminar filas con NaN en las columnas usadas
    df_scatter = vehicles.dropna(subset=['odometer', 'price'])

    # crear un gráfico de dispersión interactivo
    fig2 = px.scatter(
        df_scatter,
        x='odometer',
        y='price',
        color='type',
        hover_data=['model', 'model_year'],
        title='Dispersión: odómetro vs precio'
    )

    # mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)
