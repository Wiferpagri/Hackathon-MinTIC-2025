from utils.conectar_databricks import ejecutar_query_databricks

rows = ejecutar_query_databricks(
    "SELECT * FROM workspace.default.`transacciones-inmobiliarias` LIMIT 10000;"
)

print(rows)