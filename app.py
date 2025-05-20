import streamlit as st
import pandas as pd
import plotly_express as px

# leer los datos
car_data = pd.read_csv('vehicles_us.csv')

st.header('Sprint 7 - Proyecto')
st.write('El objetivo de este proyecto es proporcionarte más posibilidades de practicar las tareas habituales de la ingeniería de software.')


st.header('Histograma')

# crear un botón
build_histogram = st.checkbox('Construir histograma')
     
if build_histogram: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

st.header('Grafico de dispersion')

# crear un botón
build_dispersion = st.checkbox('Construir grafico de dispersion') 

if build_dispersion: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un diagrama de dispersion para el conjunto de datos de anuncios de venta de coches')
         
    # crear un grafico de dispersion
    fig = px.scatter(car_data, x="odometer", y="price")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

