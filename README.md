# Análisis de Anuncios de Venta de Coches

## Descripción
Esta es una aplicación interactiva desarrollada con **Streamlit** para explorar y analizar un conjunto de datos de anuncios de venta de vehículos en Estados Unidos. Permite generar visualizaciones interactivas (histogramas y gráficos de dispersión) que facilitan la identificación de patrones en variables como el kilometraje (`odometer`) y el precio (`price`).

## Características
- Visualizaciones interactivas con Plotly Express
- Histograma del odómetro (kilometraje)
- Gráfico de dispersión: odómetro vs precio, coloreado por tipo de vehículo
- Filtrado básico para ignorar valores faltantes en las columnas relevantes

## Tecnologías
- Python
- Streamlit
- Pandas
- Plotly Express

## Instalación

Requisitos: Python 3.7+

Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Cómo ejecutar

Inicia la aplicación web con Streamlit:

```bash
streamlit run app.py
```

La aplicación se abrirá en tu navegador en `http://localhost:8501`.

## Estructura del proyecto
- `app.py` - Aplicación principal de Streamlit que crea un histograma y un gráfico de dispersión
- `EDA.ipynb` - Notebook para Análisis Exploratorio de Datos
- `vehicles_us.csv` - Dataset con anuncios de vehículos
- `requirements.txt` - Dependencias del proyecto

## Datos
El archivo `vehicles_us.csv` contiene registros de anuncios con columnas como `price`, `model_year`, `model`, `condition`, `cylinders`, `fuel`, `odometer`, `transmission`, `type`, `paint_color`, `date_posted` y `days_listed`.

## Notas y mejoras futuras
- Añadir filtros de rango (precio, año, odómetro)
- Incorporar limpieza y tratamiento de valores atípicos
- Añadir más visualizaciones y métricas resumidas

## Autor
Proyecto desarrollado por Nicolás Espinosa.

# Análisis de Anuncios de Venta de Coches

## Descripción
Esta es una aplicación interactiva desarrollada con **Streamlit** que permite explorar y analizar datos de anuncios de venta de vehículos. La aplicación proporciona visualizaciones dinámicas que facilitan la comprensión de patrones en los datos del mercado automotriz.

## Características
- 📊 **Visualizaciones Interactivas**: Gráficos con Plotly para explorar distribuciones
- 🔄 **Análisis de Odómetro**: Histogramas interactivos del kilometraje de vehículos
- 📈 **Interfaz Intuitiva**: Aplicación web fácil de usar gracias a Streamlit

## Tecnologías Utilizadas
- **Python** - Lenguaje de programación
- **Streamlit** - Framework para crear aplicaciones web
- **Pandas** - Manipulación y análisis de datos
- **Plotly** - Visualización interactiva

## Instalación

### Requisitos
- Python 3.7+

### Configuración
1. Clona o descarga el proyecto
2. Instala las dependencias:
```bash
pip install -r requirements.txt