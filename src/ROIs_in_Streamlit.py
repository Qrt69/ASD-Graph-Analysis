import streamlit as st
from pathlib import Path
from nilearn import plotting, image
from nilearn.datasets import load_mni152_template
from nilearn.plotting import find_xyz_cut_coords
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# paths
current_dir = Path(__file__).parent
data_dir = current_dir.parent / 'data'
img_path =  current_dir.parent / 'docs' / 'img' / 'Brain afbeelding.png'


# Title clearly displayed
st.title('🧠 Interactieve CC200 ROI Visualisatie')

# Load CC200 atlas only once (cached for performance clearly)
@st.cache_resource
def load_data():
    # Explicitly get path based on current file location
    current_dir = Path(__file__).parent
    data_dir = current_dir.parent / 'data'

    atlas_file = data_dir / 'CC200.nii.gz'
    roi_labels_file = data_dir / 'CC200_ROI_labels.csv'

    # Load atlas clearly
    atlas_img = image.load_img(str(atlas_file))
    atlas_data = atlas_img.get_fdata()

    roi_labels = pd.read_csv((roi_labels_file))

    return atlas_img, atlas_data, roi_labels


atlas_img, atlas_data, roi_labels = load_data()

# User input clearly and interactively
roi_number = st.number_input(
    label='Enter ROI number (1-200):',
    min_value=1,
    max_value=200,
    value=1,
    step=1
)

# Get clear ROI description
roi_info = roi_labels[roi_labels['ROI number'] == roi_number]

if not roi_info.empty:
    harvard_label = roi_info['Harvard-Oxford'].values[0]
    center_of_mass = roi_info['center of mass'].values[0]

    st.subheader(f"📍 ROI #{roi_number} Informatie:")
    st.markdown(f"""
    - **Harvard-Oxford Label:** {harvard_label}  
    - **Center of Mass (X,Y,Z):** {center_of_mass}  
    - **Volume (voxels):** {roi_info['volume'].values[0]}  
    """)
else:
    st.warning("ROI informatie is niet gevonden.")

# Mask explicitly selected ROI
roi_mask = (atlas_data == roi_number)
masked_roi_data = np.where(roi_mask, atlas_data, 0)

# Create new masked image explicitly
masked_img = image.new_img_like(atlas_img, masked_roi_data)

# Optimal coordinates clearly found
cut_coords = find_xyz_cut_coords(masked_img)

# Clearly plot and display ROI using Streamlit
fig = plt.figure(figsize=(10, 8))
plotting.plot_roi(
    masked_img,
    bg_img=load_mni152_template(),
    title=f"Interactieve Visualisatie van ROI #{roi_number}",
    draw_cross=True,
    annotate=True,
    cmap='Set1',
    colorbar=True,
    display_mode='ortho',
    cut_coords=cut_coords,
    dim=-0.5,
    figure=fig
)

st.pyplot(fig)

st.image(str(img_path) ,caption = 'xyz-oriëntatie', width = 250)

st.markdown("ℹ️ **ROI Volume Toelichting**")
with st.expander("Zie toelichting 'Volume in voxels'"):
    st.write(
        "het volume van een ROI is de som van de aantal voxels in de ROI."
        "Een voxel is een kleine 3D kubus, typisch 3mm x 3mm x 3mm, "
        "gebruikt in hersenafbeeldingen om volume te meten."
        )