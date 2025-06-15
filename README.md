# 🧠 Análisis de Readmisión a la UCI en Pacientes con Hemorragia Intracerebral (MIMIC-IV)

Este proyecto analiza pacientes con **hemorragia intracerebral (ICH)** en la base de datos **MIMIC-IV**, con el objetivo de **predecir la readmisión a la UCI** mediante ingeniería de características, análisis clínico y modelado predictivo.

---

## 📚 Contenido del Proyecto

### 1. 🔧 Configuración Inicial
- Conexión a Google BigQuery.
- Autenticación con claves de servicio.
- Preparación del entorno.

### 2. 📦 Extracción de Datos
Consulta SQL avanzada que incluye:
- Selección de pacientes con diagnóstico ICH (ICD-9: 431, ICD-10: I610–I619).
- Variables clínicas: signos vitales, laboratorio, escalas (GCS, APS-III).
- Diagnósticos y tratamientos: hipertensión, neurocirugía, anticoagulantes, etc.
- Cálculo de:
  - Número de estancias en UCI por hospitalización.
  - Readmisión posterior en hospitalizaciones diferentes.

> Se exporta como: `mimiciv_ich_readmission_raw.csv`

### 3. 🧽 Preprocesamiento

#### 🧹 Limpieza del Dataset
- Manejo de valores nulos.
- Verificación de IDs duplicados o inconsistentes.
- Creación de variable objetivo binaria: `readmitted`.

#### 🧠 Feature Engineering
- Selección estadística de diagnósticos ICD relevantes mediante asociación con readmisión.
- Eliminación de columnas irrelevantes, con muchos nulos o que podrían inducir fuga de datos.

#### 🔬 Imputación de Valores Faltantes
- Evaluación de mecanismo MCAR/MAR/MNAR.
- Imputación basada en el patrón identificado.

### 4. 📊 Modelado Predictivo

#### Modelos Utilizados
- `Extra Trees Classifier`
- Técnicas de balanceo como `RandomOverSampler`

#### Evaluación del Desempeño
- Se define un entorno tipo *playground* para probar múltiples combinaciones de variables y modelos.
- Se hace énfasis en interpretar las variables predictoras más influyentes.

---

## ✅ Utilidad del Estudio
Este análisis permite:
- Anticipar qué pacientes podrían requerir una nueva estancia en UCI.
- Optimizar recursos críticos hospitalarios.
- Desarrollar modelos ML para soporte clínico en decisiones post-ICH.

---

## 💾 Requisitos Técnicos
- Acceso a Google BigQuery con el dataset MIMIC-IV.
- Archivo de credenciales `.json`.
- Librerías: `pandas`, `numpy`, `sklearn`, `google-cloud-bigquery`, etc.

---

## 📁 Estructura del Proyecto
- `analisis_readmision_uci_hemorragia_intracerebral.ipynb`: Notebook completo del flujo de análisis.
- `data/`: Carpeta destino para guardar dataset limpio y transformado.
- `README.md`: (este archivo)
