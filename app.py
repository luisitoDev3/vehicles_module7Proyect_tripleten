import streamlit as st 
import pandas as pd
import plotly.graph_objects as go

# Importación de datos
loc_csv = r'data\vehicles_us.csv'
car_data = pd.read_csv(loc_csv)

# Header
st.header('Vehículos')

# Crear un botón en la aplicación Streamlit que construya un histograma
hist_button = st.button('Construir histograma')

# Funcionamiento del botón de histograma
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    #Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    
    #Opcional: Se puede añadir un título al gráfico si se desea
    fig.update_layout(title_text='Distribución del Odómetro')
    
    #Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # ´use_container_with=True´ ajusta el ancho del gráfico al contenedor 
    st.plotly_chart(fig, use_container_width=True)
    
# Crear un botón que construya un gráfico de dispersión
dispersion_button = st.button('Construir gráfico de dispersión')

# Funcionamiento del botón de dispersión
if dispersion_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un gráfico de dispersión utilizando plotly.graph_objects
    # Se crea la digura indicando la fuente de los datos tanto para x como para y
    fig = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])
    
    # Opcional: Se añade un título al gráfico
    fig.update_layout(title_text='Relación entre Odómetro y Precio')
    
    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)