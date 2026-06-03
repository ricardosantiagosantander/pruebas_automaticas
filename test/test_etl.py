import pandas as pd
from app.etl import transformar_ventas


def test_transformar_ventas():
    df = pd.DataFrame({
        "product": ["A", "B", "C"],
        "selling_price": [10, 20, 15],
        "purchase_price": [6, 12, 10],
        "quantity": [2, 3, 4]
    })

    resultado = transformar_ventas(df)

    assert "unit_profit" in resultado.columns
    assert "total_sales" in resultado.columns
    assert "total_profit" in resultado.columns

    assert list(resultado["unit_profit"]) == [4, 8, 5]
    assert list(resultado["total_sales"]) == [20, 60, 60]
    assert list(resultado["total_profit"]) == [8, 24, 20]
