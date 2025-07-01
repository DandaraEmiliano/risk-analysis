import pandas as pd
from .logger_config import setup_logger

logger = setup_logger(__name__)

def extract(filepath):
    logger.info(f"Extraindo dados do arquivo: {filepath}")
    df = pd.read_csv(filepath)
    logger.info(f"{len(df)} registros extraídos")
    return df
