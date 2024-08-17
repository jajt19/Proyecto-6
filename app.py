import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv("vehicles_us.csv") # leer los datos
# Casilla de verificación para mostrar gráficos
hist_button = st.button('Construir histograma')  # crear un botón
if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.header('Histograma de Odometer')
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
# crear un bonton para el diagrama de dispersion
scatter_button = st.button("Construir diagrama de dispersión")
if scatter_button:
    st.header('Diagrama de Dispersión: Odometer vs Price')
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    # Crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price", color="condition",
                             title="Odometer vs Price según la Condición del Vehículo")  # Ejemplo de variables
    # Mostrar el gráfico de dispersión
    st.plotly_chart(fig_scatter, use_container_width=True)
