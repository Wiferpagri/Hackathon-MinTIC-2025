import pandas as pd

from utils.conectar_databricks import ejecutar_query_databricks


def obtener_datos_pandas(query: str):
    """Obtiene datos desde Databricks y los carga en un DataFrame de Pandas.

    Args:
        query: Consulta SQL para ejecutar.

    Returns:
        DataFrame de Pandas con los datos obtenidos.
    """

    filas, descripcion_cursor = ejecutar_query_databricks(query)

    if not filas:
        return pd.DataFrame()

    columnas = [desc[0] for desc in descripcion_cursor]

    df = pd.DataFrame(data=filas, columns=columnas)

    return df
