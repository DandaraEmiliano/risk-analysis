def transform(df):
    df = df[df["valor"] > 10000]
    df.loc[:, "risco"] = df["valor"].apply(lambda v: "alto" if v > 50000 else "médio")
    return df
