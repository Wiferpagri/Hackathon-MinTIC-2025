import polars as pl

from utils.conectar_databricks import ejecutar_query_databricks


def obtener_datos_polars(query: str):
    """Obtiene datos desde Databricks y los carga en un DataFrame de Polars.

    Args:
        query: Consulta SQL para ejecutar.

    Returns:
        DataFrame de Polars con los datos obtenidos.

    """

    filas, descripcion_cursor = ejecutar_query_databricks(query)

    if not filas:
        return pl.DataFrame()

    columnas = [desc[0] for desc in descripcion_cursor]

    df = pl.DataFrame(data=filas, schema=columnas)

    return df
