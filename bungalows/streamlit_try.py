import streamlit as st
import pythreejs as p3js

# Charger le modèle Wavefront
obj_path = "bungalows/cube.obj"
geometry = p3js.load(obj_path)

# Créer une scène 3D
scene = p3js.Scene(children=[geometry, p3js.AmbientLight(color=0x777777)])

# Créer une caméra
camera = p3js.PerspectiveCamera(position=[0, 5, 10], aspect=st.write(geometry.bounding_box[2] / geometry.bounding_box[1]))

# Créer un rendu
renderer = p3js.Renderer(camera=camera, scene=scene, controls=[p3js.OrbitControls(controlling=camera)])

# Afficher le rendu dans Streamlit
st.write(renderer)
