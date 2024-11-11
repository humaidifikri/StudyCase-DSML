import pandas as pd
import streamlit as st
from house_price_prediction.regression_app import regression
from intro import intro

st.set_page_config(page_title="Demo Studi Kasus")

page_names_to_funcs = {
    "Pengenalan Demo":intro,
    "Regresi": regression
    # "Mapping Demo": mapping_demo,
    # "DataFrame Demo": data_frame_demo
}

demo_name = st.sidebar.selectbox("Pilih studi kasus", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()