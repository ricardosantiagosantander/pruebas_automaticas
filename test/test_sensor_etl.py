import pandas as pd
from app.sensor_etl import limpiar_datos_sensor


def test_limpiar_datos_sensor_columnas():
    df = pd.DataFrame({
        "sensor_id": ["S1", "S2"],
        "timestamp": ["2026-06-03 10:00:00", "2026-06-03 10:01:00"],
        "temperature": [25.5, 30.0],
        "humidity": [60, 70]
    })

    resultado = limpiar_datos_sensor(df)

    assert "sensor_id" in resultado.columns
    assert "timestamp" in resultado.columns
    assert "temperature" in resultado.columns
    assert "humidity" in resultado.columns
    assert "temperature_f" in resultado.columns

def test_limpiar_datos_sensor_rangos_validos():
    df = pd.DataFrame({
        "sensor_id": ["S1", "S2", "S3"],
        "timestamp": [
            "2026-06-03 10:00:00",
            "2026-06-03 10:01:00",
            "2026-06-03 10:02:00"
        ],
        "temperature": [25.5, 150, -50],
        "humidity": [60, 70, 80]
    })

    resultado = limpiar_datos_sensor(df)

    assert resultado["temperature"].between(-20, 100).all()


def test_limpiar_datos_sensor_humedad_valida():
    df = pd.DataFrame({
        "sensor_id": ["S1", "S2", "S3"],
        "timestamp": [
            "2026-06-03 10:00:00",
            "2026-06-03 10:01:00",
            "2026-06-03 10:02:00"
        ],
        "temperature": [25, 26, 27],
        "humidity": [50, 120, -10]
    })

    resultado = limpiar_datos_sensor(df)

    assert resultado["humidity"].between(0, 100).all()

def test_limpiar_datos_sensor_elimina_nulos():
    df = pd.DataFrame({
        "sensor_id": ["S1", None, "S3"],
        "timestamp": [
            "2026-06-03 10:00:00",
            "2026-06-03 10:01:00",
            None
        ],
        "temperature": [25, 26, None],
        "humidity": [50, 60, 70]
    })

    resultado = limpiar_datos_sensor(df)

    assert resultado["sensor_id"].isna().sum() == 0
    assert resultado["timestamp"].isna().sum() == 0
    assert resultado["temperature"].isna().sum() == 0
    assert resultado["humidity"].isna().sum() == 0