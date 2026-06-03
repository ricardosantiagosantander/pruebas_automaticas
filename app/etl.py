import pandas as pd
def transformar_ventas(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Convertir columnas a números
    df["selling_price"] = pd.to_numeric(df["selling_price"], errors="coerce")
    df["purchase_price"] = pd.to_numeric(df["purchase_price"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

    # Eliminar filas con nulos importantes
    df = df.dropna(subset=["selling_price", "purchase_price", "quantity"])

    # Crear columnas calculadas
    df["unit_profit"] = df["selling_price"] - df["purchase_price"]
    df["total_sales"] = df["selling_price"] * df["quantity"]
    df["total_profit"] = df["unit_profit"] * df["quantity"]

    return df
