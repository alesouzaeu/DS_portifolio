# -*- coding: utf-8 -*-
"""
@author: Alessandro Souza Eugenio
"""


import numpy as np
import pickle
import streamlit as st

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
    st.title("Preditor de felicidade")
    html_temp = """
    <div style="background-color:gray;padding:10px">
    <h2 style="color:white;text-align:center;">Projeto - Happiness Report 2015-2019 </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    GDP = values = st.slider('GDP', 0.0, 1.74, (0.9))
    st.write('Values:', values)
    Family = values = st.slider('Family', 0.0, 1.49, (1.06))
    st.write('Values:', values)
    Health = values = st.slider('Health', 0.0, 1.02, (0.60))
    st.write('Values:', values)
    Freedom = values = st.slider('Freedom', 0.0, 0.65, (0.41))
    st.write('Values:', values)
    Corruption = values = st.slider('Corruption', 0.0, 0.47, (0.12))
    st.write('Values:', values)
    Generosity = values = st.slider('Generosity', 0.0, 0.72, (0.22))
    st.write('Values:', values)
    Region = st.selectbox("Select option", options=list(region_to_onehot.keys()))
    st.write(f"Você selecionou {Region}")

    if st.button("Prever"):
        result = classifier.predict([np.r_[GDP, Family, Health, Freedom, Corruption, Generosity, region_to_onehot[Region]]])
        (st.success("Esta região é: {}".format(result)))

if __name__ == '__main__':
    main()
