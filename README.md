# SentimentAnalysis - AI Topics
## Datos del estudiante 📝
* **Nombre:** Marcos Andrés Simon Ágreda
* **Código:** 56728
* **Carrera:** Ingeniería de Sistemas Computacionales
* **Curso:** Tópicos Selectos en Inteligencia Artificial

## Descripción del proyecto 📋

El proyecto consiste en la implementación de una API, cuyos endpoints, de forma general, brindan acceso a cuatro modelos de procesamiento de lenguaje natural, los cuales, cada uno tiene una tarea específica, que es la siguiente:

- **Spanish Core News Medium:** Modelo que permite realizar la tarea de POS Tagging, la cual consiste en asignar a cada palabra de una oración, una etiqueta gramatical, como por ejemplo, sustantivo, verbo, adjetivo, etc; la tarea de NER, la cual consiste en identificar entidades en una oración, como por ejemplo, nombres de personas, lugares, organizaciones, etc; y la tarea de Embedding, la cual consiste en asignar a cada palabra de una oración, un vector de números reales, que representa la palabra en un espacio vectorial.
- **Spanish Sentiment Analysis:** Modelo que permite realizar la tarea de Sentiment Analysis, la cual consiste en identificar el sentimiento de una oración, en este caso: Muy negativo, negativo, poco negativo, neutral, poco positivo, positivo, muy positivo.
- **GPT-4:** Modelo de lenguaje colosal, que permite realizar la tarea de generación de texto general, en este caso, utilizado para generar una ruta alternativa para obtener las salidas obtenidas por los modelos anteriores, menos el modelo de Embedding.
- **Text Embedding ADA 002:** Modelo que permite realizar la tarea de Embedding, utilizando las capacidades de generación de texto de GPT.

La API está desarrollada en Python, haciendo uso de la librería FastAPI, y cada uno de los modelos, están basados en las siguientes librerías:

- **Spanish Core News Medium:** Librería SpaCy.
- **Spanish Sentiment Analysis:** Librería PyTorch y transformers (modelo creado por Karina Aquino).
- **GPT-4 y Text Embedding ADA 002:** Librería OpenAI y LangChain.

Como un extra, se ha desarrollado una aplicación web, que hace uso de la API, para brindar una interfaz gráfica al usuario, y así poder hacer uso de la API de forma más amigable, la cual se encuentra en la carpeta `frontend`. Dicho frontend solamente hace uso del endpoint `/sentiment`.

## Descripción de la API 🚀

La API cuenta con los siguientes endpoints:

* `/status`: Endpoint que devuelve el estado de la API, en caso de que esté activa, devuelve un mensaje de éxito, además de datos extra, como el nombre de la API, la versión y los nombres de los modelos.
* `/sentiment`: Endpoint que recibe una cadena de texto, y devuelve el sentimiento de la misma,utilizando el modelo de Spanish Sentiment Analysis, con un número entre -1 y 1, donde -1 es muy negativo, y 1 es muy positivo. Además, devuelve la etiqueta que corresponde al sentimiento, que puede ser: Muy negativo, negativo, poco negativo, neutral, poco positivo, positivo, muy positivo.
* `/analysis`: Endpoint que recibe una cadena de texto, y devuelve la salida del anterior endpoint, junto con el análisis realizado por el modelo de Spanish Core News Medium, el cual contiene el POS Tagging, el NER y el Embedding.
* `/analysis_v2`: Endpoint que recibe una cadena de texto, y devuelve las salidas de los endpoints `/sentiment` y `/analysis`, pero en vez de utilizar los modelos correspondientes, utiliza el modelo de GPT-4, para generar una ruta alternativa, para obtener el sentimiento, el POS Tagging y el NER; y el modelo de Text Embedding ADA 002, para obtener el Embedding.
* `/reports`: Endpoint que devuelve un reporte en formato .csv de la ejecución de los endpoints `/sentiment`, `/analysis` y `/analysis_v2` proporcionando información relevante como: El texto original y su cantidad de carácteres, la predicción numérica del sentimiento del texto, la etiqueta de sentimiento asignada,la fecha y hora de ejecución, el tiempo de ejeución en segundos, el modelo utilizado, la versión de la API, y si aplica, el POS Tagging, el NER y el Embedding.

## Proceso de instalación y ejecución 🛠️

Antes de poder ejecutar la API, se debe crear un archivo `.env` en la ruta raiz del proyecto, y agregar las siguientes variables de entorno:

```
OPENAI_KEY=<API_KEY>
```

Para poder ejecutar la API, se debe tener instalado Docker. Posteriormente, se debe abrir una terminal en la raiz del proyecto, y ejecutar el siguiente comando:

```
docker-compose up
```

Este comando, creará un contenedor de Docker, sin antes crear la imagen Docker, basada en el archivo `Dockerfile`, el cual descargará todas las dependencias necesarias para ejecutar la API, y posteriormente, ejecutará la API en el puerto 8000.

### Instalación y ejecución sin Docker 🐳

ATECIÓN: Este proceso de instalación y ejecución, no es recomendado, ya que se debe instalar cada una de las dependencias de forma manual, y además, se deben descargar los modelos de forma manual, lo cual puede tomar mucho tiempo.

El modelo de Spanish Sentiment Analysis, se debe clonar de la siguiente dirección:
```
git clone https://huggingface.co/karina-aquino/spanish-sentiment-model
```

OJO, se debe tener habilitado el LFS de Git, para poder clonar el modelo.

Y la carpeta clonada, es decir `spanish-sentiment-model`, se debe mover a la carpeta `models`, que se encuentra en la carpeta src del proyecto.

El modelo de Spanish Core News Medium, se debe descargar de la siguiente dirección:
```
https://github.com/explosion/spacy-models/releases/download/es_core_news_md-3.7.0/es_core_news_md-3.7.0.tar.gz
```
Una vez descargado, descomprimir el archivo, lo cual dejará una carpeta llamada `es_core_news_md-3.7.0`. En esa carpeta, entrar a la carpeta `es_core_news_md`, y finalmente, copiar la carpeta `es_core_news_md-3.7.0` a la carpeta `models`, que se encuentra en la carpeta src del proyecto.

Después, se debe tener Python 3.10 o superior instalado, y posteriormente instalar las dependencias del proyecto:

```
fastapi
uvicorn
pydantic
pydantic-settings
python-multipart
python-dotenv
numpy
spacy
openai
langchain
tiktoken
transformers
```

Además, de forma separada, se debe ejecutar el siguiente comando:

```
pip3 install torch==2.1.1+cpu torchvision==0.16.1+cpu torchaudio==2.1.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
```
Finalmente, para ejecutar la API, se debe abrir una terminal en la raiz del proyecto, y ejecutar el siguiente comando:

```
uvicorn src.app:app --reload
```

## Extra: Aplicación web 📦

Para poder ejecutar la aplicación web, se debe tener instalado Node.js 14 o superior. Posteriormente, se debe abrir la carpeta `frontend` en una terminal, y ejecutar el siguiente comando:

```
npm install
```

Posteriormente, crear un archivo `.env` en la carpeta `frontend`, y agregar la siguiente variable de entorno:

```
REACT_APP_BACKEND_URL=http://localhost:8000
``` 
O, también se puede usar el link de la API en Google Cloud Platform (adjuntado en el correo)

Finalmente, ejecutar el siguiente comando:

```
npm start
```
