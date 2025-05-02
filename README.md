# UCI-I61: Análisis de la Readmisión a la UCI en Pacientes con Hemorràgia Intracerebral 


## Objetivo
Desarrollar un modelo que estime la probabilidad de readmisión a la UCI en pacientes con hemorragia intracerebral, identificando factores de riesgo para mejorar las estrategias de seguimiento.

## Hipótesis 

La combinación de variables clínicas (estado neurológico, presión arterial, comorbilidades, escalas de coma) permite predecir efectivamente la readmisión de estos pacientes.

## Metodología 

- Selección de Datos: Extraer de MIMIC-IV la cohorte de pacientes con hemorragia intracerebral y los datos de seguimiento tras el alta. 
- Variables: Considerar parámetros clínicos al ingreso, escalas como el GCS, y comorbilidades. 
- Preprocesamiento: Normalización, codificación de variables categóricas y manejo de datos desequilibrados (por ejemplo, técnicas de oversampling).
- Modelado: Aplicar técnicas de regresión, random forest y métodos ensemble, validando con métricas como F1-score, precisión, recall y AUC. 

## Producto/Entregable:

- Desarrollo del Sistema: Desarrollar una herramienta de soporte a la decisión que integre un frontend y backend en una plataforma tipo Hugging Face o Groq. La aplicación debe permitir seleccionar los datos clínicos y visualizar un score de riesgo de readmisión mediante gráficas interactivas y métricas de validación.
- Repositorios: Los estudiantes deben crear sus cuentas en GitHub, subir el desarrollo y compartir la dirección del repositorio. o Documentación: Incluir una descripción de la funcionalidad, la arquitectura del sistema y ejemplos prácticos de uso. 


# README from Juan Barrios: 

Este proyecto utiliza datos del conjunto MIMIC-IV para predecir la readmisión a la UCI en pacientes diagnosticados con hemorragia intracerebral. Se implementa un flujo de análisis en Python, empleando BigQuery como fuente de datos y técnicas de machine learning para modelado.

## 📁 Estructura del repositorio

- `analisis_readmision_uci_hemorragia_intracerebral.ipynb`: Notebook principal con todo el flujo de trabajo.
- `README.md`: Descripción general del proyecto.

## ⚙️ Requisitos

- Cuenta en Google Cloud con acceso al dataset MIMIC-IV en BigQuery.
- Python >= 3.7
- Paquetes: `pandas`, `scikit-learn`, `matplotlib`, `google-cloud-bigquery`

## 🚀 Instrucciones

1. Autenticarte en Google Cloud dentro del entorno donde se ejecute el notebook.
2. Actualizar `project_id` en la celda de configuración.
3. Ejecutar las celdas secuencialmente para obtener, procesar y analizar los datos.

## 📊 Resultado

Se entrena un modelo de Random Forest para estimar la probabilidad de readmisión y se evalúa con métricas como F1-score y AUC. Se visualiza la curva ROC del modelo.

## 🧰 Posibles mejoras

- Implementar interfaz visual con Streamlit o Gradio.
- Incorporar oversampling/undersampling para balanceo.
- Integración en Hugging Face Spaces.

## 🔐 Aviso

Este proyecto utiliza datos de pacientes anonimizados del dataset MIMIC-IV con fines académicos.