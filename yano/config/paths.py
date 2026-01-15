# config/paths.py
"""
Path configuration for the DRG Xenium analysis project.

Edit BASE_DIR to the location of local data directory.
"""

from pathlib import Path

REPO_DIR = Path(__file__).resolve().parents[1]

# CHANGE THIS to your local data directory
BASE_DIR = Path("/home/workspace/projects/drg")

# Metadata containing manual annotations, housed within repo
METADATA_DIR = REPO_DIR / "metadata"