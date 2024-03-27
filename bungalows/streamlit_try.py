import streamlit as st
import pythreejs as p3js

# Charger le modèle Wavefront
obj_path = "bungalows/cube.obj"
loader = p3js.OBJLoader()
obj = loader.load(obj_path)

# Créer une scène 3D
scene = p3js.Scene(children=[obj])

# Créer une caméra
camera = p3js.PerspectiveCamera(position=[0, 5, 10])

# Créer un rendu
renderer = p3js.Renderer(camera=camera, scene=scene, controls=[p3js.OrbitControls(controlling=camera)])

# Afficher le rendu dans Streamlit
st.write(renderer)

