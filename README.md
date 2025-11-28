# Sistema de Monitoreo y Detección de Anomalías en Transacciones Inmobiliarias (2015–2025)

## 📌 Descripción del Reto
Colombia concentra más de **34 millones de registros de transacciones inmobiliarias únicas** entre 2015 y 2025, distribuidas en **1.105 municipios**. Esta información es esencial para la planeación territorial, el análisis de mercado, la supervisión operativa y la evaluación de riesgos.

No obstante, el **alto volumen**, la **heterogeneidad** y las **posibles inconsistencias** en los datos generan limitaciones para:
- Detectar errores o anomalías.
- Identificar patrones de fraude.
- Controlar riesgos operativos y financieros.
- Validar la calidad de los registros.
- Integrar datos con otras fuentes públicas.

Este proyecto aborda estos desafíos mediante técnicas de análisis avanzado, automatización y machine learning.

---

## 🎯 Objetivo General
Diseñar e implementar un **sistema automatizado de monitoreo, análisis y detección de anomalías** en la dinámica inmobiliaria del país, permitiendo identificar riesgos operativos, financieros, de fraude y problemas de calidad de datos en tiempo real o mediante procesos periódicos.

---

## 🎯 Objetivos Específicos
- **OE1.** Integrar y estandarizar los registros de transacciones inmobiliarias.  
- **OE2.** Construir modelos de detección de anomalías basados en estadísticas, reglas y machine learning.  
- **OE3.** Identificar patrones de fraude, valores atípicos, duplicidades y errores de anotación.  
- **OE4.** Desarrollar un tablero de monitoreo con indicadores clave de riesgo y calidad.  
- **OE5.** Integrar fuentes públicas complementarias.  
- **OE6.** Documentar la metodología, procesos y arquitectura de datos.  

---

## 🌍 Impacto Esperado
- Mayor control operativo sobre registros inmobiliarios.  
- Identificación temprana de fraude y anomalías.  
- Reducción de errores administrativos.  
- Incremento en la confianza sobre la calidad de los datos.  
- Fortalecimiento de la planeación territorial.  
- Ahorro de tiempo y recursos mediante automatización.  
- Mejora en la capacidad analítica nacional y municipal para comprender la dinámica del mercado inmobiliario.  

---

## 📊 Fuente de Datos
El conjunto de datos principal proviene del portal oficial de datos abiertos de Colombia:

🔗 **Registro de transacciones inmobiliarias en Colombia (2015–2025)**  
https://www.datos.gov.co/Vivienda-Ciudad-y-Territorio/Registro-de-transacciones-inmobiliarias-en-Colombi/7y2j-43cv/about_data

---

## 📁 Estructura del Proyecto
```
Hackathon-MinTIC-2025/
├── README.md
├── LICENSE
├── .gitignore
│
├── docs/ # Documentación del proyecto
│   ├── Documentación.pdf
│
├── notebooks/ # Exploración y prototipado
│   ├── Anomalias en predios.ipynb
│   ├── Data Cleaning.ipynb
│   ├── 4.0_modelos_anomalias.ipynb
│   ├── Preparacion de datos para modelo de deteccion de anomalias.ipynb
│
│
├── src/ # Código fuente modularizado
│   ├── etl/ # Scripts de extracción, transformación y carga
│   │   ├── data_loader
│
├── data_model/ # Definiciones de esquemas y reglas
│   ├── esquema_bronze.json
│   ├── esquema_silver.json
│   ├── esquema_gold.json
│   ├── features_ml.json
│   └── reglas_calidad.json
│
├── dashboards/ # Archivos de Power BI
│   ├── transacciones_anomalas.pbix
│   └── transacciones_inmobiliarias.pbix
│
└── anexos/ # Archivos complementarios y catálogos
    ├── Directorio_ORIP_20251128.csv
    ├── DIVIPOLA-_Codigos_municipios_20251121.csv
    ├── transacciones_inmobiliarias.csv
    └── tabla_reglas_aplicadas.csv
```

---

## 🛠 Tecnologías utilizadas
- Python (pandas, numpy, scikit-learn, PySpark)
- Databricks (Datalake)
- DuckDB y Polars.
- Power BI 
- Git para control de versiones

---
