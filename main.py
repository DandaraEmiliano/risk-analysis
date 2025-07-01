from etl.extract import extract
from etl.transform import transform
from etl.load import load

if __name__ == "__main__":
    filepath = "data/transacoes.csv"
    df = extract(filepath)
    df = transform(df)
    load(df, "risco_db", "transacoes_filtradas")
