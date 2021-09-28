import streamlit as st
from skimage import io
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="  De Imagenes",#titulo
    page_icon="📸",#Icono
    layout="wide",
    initial_sidebar_state="expanded",
)

st.header('Manipulacion de Imagenes')
st.write("---")

image = st.sidebar.file_uploader('Imagen',type=['.jpg','.png','.csv'])

rgb = io.imread('lena.jpg')
rgb = io.imread(image)
st.sidebar.header('Especifique los parametros de RED , GREEN y BLUE')
st.sidebar.write("---")

red = st.sidebar.slider('RED',-100,100,0)
green = st.sidebar.slider('GREEN',-100,100,0)
blue = st.sidebar.slider('BLUE',-100,100,0)

for i in range(rgb.shape[0]):
    for j in range(rgb.shape[1]):
        rgb[i,j,0] += red 

for i in range(rgb.shape[0]):
    for j in range(rgb.shape[1]):
        rgb[i,j,1] += green 

for i in range(rgb.shape[0]):
    for j in range(rgb.shape[1]):
        rgb[i,j,2] += blue 

io.imsave('lena2.jpg',rgb)

st.image('lena2.jpg')
