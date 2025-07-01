from .logger_config import setup_logger

logger = setup_logger(__name__)

def transform(df):
    logger.info("Iniciando transformação dos dados")
    df = df[df["valor"] > 10000]
    df.loc[:, "risco"] = df["valor"].apply(lambda v: "alto" if v > 50000 else "médio")
    logger.info(f"{len(df)} registros após filtro de valor > 10000")
    return df
