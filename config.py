"""
Configuration file for FloodSafe ML Pipeline
Store your API credentials here (add to .gitignore!)
"""
import os

# NASA Earthdata credentials
NASA_USERNAME = os.getenv("NASA_USERNAME")
NASA_PASSWORD = os.getenv("NASA_PASSWORD")


# Google Earth Engine
GEE_SERVICE_ACCOUNT_JSON = os.getenv("GEE_SERVICE_ACCOUNT_JSON")


# OpenRouteService (already have)
ORS_API_KEY =  os.getenv("ORS_API_KEY")


# Data storage paths
DATA_DIR = "data"
RAW_DATA_DIR = f"{DATA_DIR}/raw"
PROCESSED_DATA_DIR = f"{DATA_DIR}/processed"
MODEL_DIR = "models"


# Model parameters
RANDOM_STATE = 42
TEST_SIZE = 0.2


# Routing parameters
LAMBDA_SAFEST = 10.0  # High weight on flood risk
LAMBDA_BALANCED = 3.0  # Medium weight
LAMBDA_FASTEST = 0.5  # Low weight (prioritize speed)

