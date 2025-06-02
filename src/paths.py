from pathlib import Path
import sys

def get_project_root() -> Path:
    """Return the root path of the project."""
    try:
        # If this is a script file
        return Path(__file__).resolve().parents[1]
    except NameError:
        # If in a notebook or interactive shell
        return Path().resolve().parents[1]

# ------------------
# Standard directories
# ------------------

def get_data_dir() -> Path:
    return get_project_root() / "data"

def get_raw_data_dir() -> Path:
    return get_data_dir() / "raw"

def get_processed_data_dir() -> Path:
    return get_data_dir() / "processed"

def get_connectivity_dir() -> Path:
    return get_raw_data_dir() / "connectivity_matrices"

def get_docs_dir() -> Path:
    return get_project_root() / "docs"

def get_notebooks_dir() -> Path:
    return get_project_root() / "notebooks"

# ------------------
# Specific files
# ------------------

def get_phenotype_path() -> Path:
    return get_processed_data_dir() / "Phenotypic_filtered.csv"

def get_roi_labels_path() -> Path:
    return get_raw_data_dir() / "CC200_ROI_labels.csv"

def get_atlas_path() -> Path:
    return get_raw_data_dir() / "CC200.nii.gz"

# ------------------
# Example utility
# ------------------

def list_1d_files() -> list[Path]:
    """Return all .1D files in connectivity dir"""
    return list(get_connectivity_dir().glob("*.1D"))
