import streamlit as st
import pywavefront
import pythreejs as p3js

def load_obj(file_path):
    return pywavefront.Wavefront(file_path)

# Charger le modèle Wavefront
obj_path = "bungalows/cube.obj"
obj = load_obj(obj_path)

# Créer un objet Mesh de pythreejs
geometry = p3js.BufferGeometry.from_geometry(p3js.JSONLoader.parse(obj))
material = p3js.MeshPhongMaterial(color="gray")
mesh = p3js.Mesh(geometry=geometry, material=material)

# Créer une scène 3D
scene = p3js.Scene(children=[mesh])

# Créer une caméra
camera = p3js.PerspectiveCamera(position=[0, 5, 10])

# Créer un rendu
renderer = p3js.Renderer(camera=camera, scene=scene, controls=[p3js.OrbitControls(controlling=camera)])

# Afficher le rendu dans Streamlit
st.write(renderer)
