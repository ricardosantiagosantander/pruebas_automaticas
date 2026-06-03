import pandas as pd


def limpiar_datos_sensor(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["sensor_id"] = df["sensor_id"].astype(str)
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df["temperature"] = pd.to_numeric(df["temperature"], errors="coerce")
    df["humidity"] = pd.to_numeric(df["humidity"], errors="coerce")

    # Eliminar filas inválidas
    df = df.dropna(subset=["sensor_id", "timestamp", "temperature", "humidity"])

    # Filtrar rangos físicos razonables
    df = df[
        (df["temperature"] >= -20) &
        (df["temperature"] <= 100) &
        (df["humidity"] >= 0) &
        (df["humidity"] <= 100)
    ]

    # Crear columna calculada
    df["temperature_f"] = (df["temperature"] * 9 / 5) + 32

    return df
