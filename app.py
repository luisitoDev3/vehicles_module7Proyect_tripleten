import streamlit as st 
import pandas as pd
import plotly

# Importación de datos
loc_csv = r'..\data\vehicles_us.csv'
car_data = pd.read_csv(loc_csv)

# Header
st.header('Vehículos')

# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    #Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    
    #Opcional: Se puede añadir un título al gráfico si se desea
    fig.update_lagout(title_text='Distribución del Odómetro')
    
    #Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # ´use_container_with=True´ ajusta el ancho del gráfico al contenedor 
    st.plotly_chart(fig, use_container_width=True)