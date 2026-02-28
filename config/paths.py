#### KA updating 20260228




# config/paths.py
"""
Path configuration for the DRG Xenium analysis project.

Edit BASE_DIR to the location of local data directory.
"""

from pathlib import Path

# CHANGE THIS to your local data directory for intermediate outputs
DATA_DIR = Path("/home/workspace/data/temp/DRG")

# CHANGE THIS to your local data directory where raw xenium data is stored
BASE_DIR = Path("/home/workspace/DRG/spatial_mouse_drg_outputs/Kim")
# BASE_DIR = Path("/home/workspace/projects/drg") # MC previous




# REPO_DIR = Path(__file__).resolve().parents[1]