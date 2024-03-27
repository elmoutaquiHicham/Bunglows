import streamlit as st
import pywavefront

def load_obj(file_path):
    return pywavefront.Wavefront(file_path)

# Charger le modèle Blender
obj = load_obj("bungalows/cube.mtl")

# Afficher l'élément 3D dans Streamlit
st.write(obj)
