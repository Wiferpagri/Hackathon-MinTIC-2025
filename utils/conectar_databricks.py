"""Utilidad para realizar consultas hacia Databricks."""


from config import get_databricks_conn
from functools import lru_cache

@lru_cache(maxsize=1)
def ejecutar_query_databricks(query: str)->list:
    """Ejecuta una consulta SQL en Databricks.

    Args:
        query: Query SQL para ejecutar.

    Returns:
        Resultado de la consulta.

    """
    conn = get_databricks_conn()

    with conn.cursor() as cursor:
        data = cursor.execute(query)
        data = data.fetchall()
        description = cursor.description

        return data, description
