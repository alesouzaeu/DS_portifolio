# -*- coding: utf-8 -*-
"""
@author: Alessandro Souza Eugenio
"""


import numpy as np
import matplotlib as plt
import pickle
import streamlit as st
import pandas as pd
from PIL import Image

pickle_in = open("modelo2.pkl", "rb")
classifier = pickle.load(pickle_in)

region_to_onehot = {'Australia and New Zealand': np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                    'Central and Eastern Europe': np.array([0, 1, 0, 0, 0, 0, 0, 0, 0, 0]),
                    'Eastern Asia': np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0]),
                    'Latin America and Caribbean': np.array([0, 0, 0, 1, 0, 0, 0, 0, 0, 0]),
                    'Middle East and Northern Africa': np.array([0, 0, 0, 0, 1, 0, 0, 0, 0, 0]),
                    'North America': np.array([0, 0, 0, 0, 0, 1, 0, 0, 0, 0]),
                    'Southeastern Asia': np.array([0, 0, 0, 0, 0, 0, 1, 0, 0, 0]),
                    'Southern Asia': np.array([0, 0, 0, 0, 0, 0, 0, 1, 0, 0]),
                    'Sub-Saharan Africa': np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 0]),
                    'Western Europe': np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
                    }




def prepare_input(Region):


    return [np.r_[GDP, Family, Health, Freedom, Corruption, Generosity, region_to_onehot[Region]]]

# @app.route('/predict',methods=["Get"])


def main():



    st.title("Projeto - Happiness Report 2015-2019")
    html_temp = """
    <div style="background-color:gray;padding:10px">
    <h2 style="color:white;text-align:center;">Preditor de Felicidade</h2>
    </div>
    """
    Region = st.sidebar.selectbox("Selecione a Região", options=list(region_to_onehot.keys()))
    st.write(f"Você selecionou {Region}")


    st.markdown(html_temp, unsafe_allow_html=True)
    GDP = values = st.sidebar.slider('GDP', 0.0, 1.0, (0.5))
    st.sidebar.write('Valores:', values)
    Family = values = st.sidebar.slider('Family', 0.0, 1.0, (0.5))
    st.sidebar.write('Valores:', values)
    Health = values = st.sidebar.slider('Health', 0.0, 1.0, (0.5))
    st.sidebar.write('Valores:', values)
    Freedom = values = st.sidebar.slider('Freedom', 0.0, 1.0, (0.5))
    st.sidebar.write('Valores:', values)
    Corruption = values = st.sidebar.slider('Corruption', 0.0, 1.0, (0.5))
    st.sidebar.write('Valores:', values)
    Generosity = values = st.sidebar.slider('Generosity', 0.0, 1.0, (0.5))
    st.sidebar.write('Valores:', values)


    if st.sidebar.button("Prever"):

        (result) = classifier.predict([np.r_[GDP, Family, Health, Freedom, Corruption, Generosity, region_to_onehot[Region]]])
        a = (result)
        b = 0
        if a == b:
            st.success("Esta região é feliz")
        else:
            st.warning("Esta região é Infeliz")



        #st.warning("Esta região é: {}".format(result))


if __name__ == '__main__':
    main()
