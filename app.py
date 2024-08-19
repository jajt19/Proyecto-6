import streamlit as st
import pandas as pd
import plotly.express as px

# Título general de la aplicación
st.title("Análisis de Datos de Vehículos Usados")

# Descripción general de la aplicación
st.write("Esta aplicación permite explorar el conjunto de datos de anuncios de venta de coches. "
         "Puedes visualizar un histograma del odómetro y un diagrama de dispersión entre el odómetro y el precio.")

# Leer los datos
car_data = pd.read_csv("vehicles_us.csv")

# Subtítulo y botón para el histograma
st.subheader("Visualización de Histograma")
st.write("Haz clic en el botón a continuación para generar un histograma que muestra la distribución del kilometraje (odómetro) de los vehículos.")
hist_button = st.button('Construir histograma')
if hist_button:
    st.header('Histograma de Odometer')
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Subtítulo y botón para el diagrama de dispersión
st.subheader("Visualización de Diagrama de Dispersión")
st.write("Haz clic en el botón a continuación para generar un diagrama de dispersión que muestra la relación entre el kilometraje (odómetro) y el precio de los vehículos, diferenciados por la condición del vehículo.")
scatter_button = st.button("Construir diagrama de dispersión")
if scatter_button:
    st.header('Diagrama de Dispersión: Odometer vs Price')
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price", color="condition",
                             title="Odometer vs Price según la Condición del Vehículo")

    # Mostrar el gráfico de dispersión
    st.plotly_chart(fig_scatter, use_container_width=True)


    # Mostrar el gráfico de dispersión
    st.plotly_chart(fig_scatter, use_container_width=True)
