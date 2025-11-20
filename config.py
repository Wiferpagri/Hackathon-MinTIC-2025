"""Configuración de la aplicación y variables globales."""

import os
from dotenv import load_dotenv
from databricks import sql

load_dotenv()


def get_databricks_conn():
    """Crea un objeto de conexión a Databricks.

    Returns:
        Objeto de conexión a Databricks.

    Raises:
        ValueError: Si no se encuentran las variables de entorno.
        sql.Error: Si la conexión a Databricks falla.

    """
    server = os.getenv('DATABRICKS_SERVER_HOSTNAME')
    http_path = os.getenv('DATABRICKS_HTTP_PATH')
    token = os.getenv('DATABRICKS_ACCESS_TOKEN')

    conn = sql.connect(
        server_hostname=server,
        http_path=http_path,
        access_token=token,
    )

    return conn
