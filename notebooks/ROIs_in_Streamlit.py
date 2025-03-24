import streamlit as st
from pathlib import Path
from nilearn import plotting, image
from nilearn.datasets import load_mni152_template
from nilearn.plotting import find_xyz_cut_coords
import numpy as np
import matplotlib.pyplot as plt

# Title clearly displayed
st.title('🧠 Interactive CC200 ROI Visualization')

# Load CC200 atlas only once (cached for performance clearly)
@st.cache_resource
def load_atlas():
    # Explicitly get path based on current file location
    current_dir = Path(__file__).parent
    data_dir = current_dir.parent / 'data'
    atlas_file = data_dir / 'CC200.nii.gz'

    # Load atlas clearly
    atlas_img = image.load_img(str(atlas_file))
    return atlas_img, atlas_img.get_fdata()


atlas_img, atlas_data = load_atlas()

# User input clearly and interactively
roi_number = st.number_input(
    label='Enter ROI number (1-200):',
    min_value=1,
    max_value=200,
    value=1,
    step=1
)

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
    title=f"Interactive Visualization of ROI #{roi_number}",
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
