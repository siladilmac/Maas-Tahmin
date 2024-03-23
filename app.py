# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Bhzr7mAmdISOrD41hJzk_LUomfH8E9ut
"""

import streamlit as st
import pandas as ps
import pickle

st.title("Maaş Tahmin Sistemi:heavy_dollar_sign:")

model=pickle.load(open("model.pkl","rb"))
tecrube=st.number_input("Tecrube",1,10)
yazili=st.number_input("Sınav",1,10)
mulakat=st.number_input("Mulakat",1,10)
if st.button("Tahmin Et"):
  tahmin=model.predict([[tecrube,yazili,mulakat]])
  tahmin=round(tahmin[0],2)
  st.write(f"Tahmini maas $: {tahmin}")

