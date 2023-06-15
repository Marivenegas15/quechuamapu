# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 00:23:23 2023

@author: jveraz
"""

##########################
## Números en streamlit ##
##########################

## instalación
## https://docs.streamlit.io/library/get-started/installation

## text_input = st.text_input(
##        "Escriba un verbo 👇",
##        label_visibility=st.session_state.visibility,
##        disabled=st.session_state.disabled,
##        placeholder=st.session_state.placeholder,
##    )

## st.write(xxx)

## librería!
import streamlit as st

st.title('Quechua y Mapudungu')

def sufijo(s):
    ## si termina en vocal
    if s[-1] in 'aeiou':
        s = s + '-yuq'
    ## termina en consonante
    else:
        s = s + '-ni-yuq'
    return s

## Función que recibe un entero entre 1 y 99, y entrega su versión en palabras

## input: entero n entre 1 y 99

D = {0:'', 1:'huk', 2:'iskay', 3:'kimsa', 4:'tawa', 5:'pichqa', 6:'suqta', 7:'qanchis', 8:'pusaq', 9:'isqun', 10:'chunka'}

def quechua(n):
    ## el número es menor o igual a 10
    if n <= 10:
        ## usamos el diccionario
        s = D[n]
    ## el número es mayor a 10
    else:
        ## el número comienza con chunka
        s = 'chunka'
        
        ## extraemos la decena y la unidad
        decena = n//10
        unidad = n%10
        
        ## agregamos la unidad
        s = s + ' ' + D[unidad]
        
        ## si la decena es mayor a 1
        if decena > 1:
            s = D[decena] + ' ' + s
            
        ## agregamos el sufijo
        if unidad!=0:
            s = sufijo(s)
    return s

R = {0: '', 1:'kiñe' , 2:'epu', 3:'küla', 4:'meli', 5:'kechu', 6:'kayu', 7:'reqle', 8:'pura', 9:'aylla', 10:'mari' }

def mapuche(n):
    if n <= 10:
        s= R[n]
    else:
        s = 'mari'
        decena = n//10
        unidad = n%10
        s = s + ' ' + R[unidad]
        if decena > 1:
            s = R[decena] + ' ' + s
            
    return s

options = st.multiselect(
    'Elige una o dos lenguas!',
    ['Quechua', 'Mapuche'])

n_input = st.slider("Escriba un número entre 1 y 99", 1, 99, 1)
if 'Quechua' in options:
    st.write('Elegiste:', quechua(n_input))
if 'Mapuche' in options:
    st.write('Elegiste:', mapuche(n_input))

import streamlit as st
from PIL import Image

i = Image.open('mimi.jpeg')

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image(i)

with col3:
    st.write(' ')

## Terminación en vocal o consonante

## input: string s




