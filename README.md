# Análisis de Tendencias Musicales: TikTok y Spotify

Este repositorio contiene 4 notebooks, uno que explora la relación entre las tendencias musicales de TikTok y su impacto en Spotify y el resto que se limitan a proporcionar los datos para el análisis. El proyecto busca identificar las características que definen una canción viral en TikTok y comprobar si estas tendencias se reflejan en el éxito de las canciones en Spotify, pero sobre todo, analizar las características musicales de las canciones que componen los rankings del estudio.

## Estructura del Proyecto

### Notebook de análisis
1. **EDA_TikTok_Spotify.ipynb**: Este notebook realiza un Análisis Exploratorio de Datos (EDA) para estudiar la influencia de las canciones populares de TikTok en los rankings de Spotify.

### Notebook de extracción

1. **Scrapper_TikTok.ipynb**: Este notebook sirve para poder extraer la información de la página: [TikTok Creative Center - Popular Music](https://ads.tiktok.com/business/creativecenter/inspiration/popular/music/pc/en).

2. **spotify_info.ipynb**: Consulta a través de la API de Spotify para extraer los track_id y las primeras características de las canciones.

3. **Scrapper_Musicstax.ipynb**: Este notebook contiene un scraper diseñado para recopilar información musical desde [Musicstax](https://musicstax.com/), la cual proporciona características detalladas de cada canción, como tempo, tonalidad y danceability.

## Hipótesis del Análisis

En el notebook de EDA se plantean las siguientes hipótesis:

1. **Popularidad en Spotify**: Las canciones que son tendencia en TikTok se correlacionan con un índice de popularidad alto en Spotify.

2. **Características musicales y ranking en TikTok**: Las canciones con tempos rápidos, un índice alto de *danceability* y en tonalidad mayor tendrán un mejor posicionamiento dentro del ranking de TikTok.

3. **Similitud entre rankings globales y regionales**: ¿El *Top 5 Global* de TikTok se asemeja a los *Top 5* regionales?.

4. **Influencia de la estacionalidad**: Dado que la extracción de datos se realizó el 27 de diciembre, se espera encontrar canciones temáticas de Navidad en posiciones intermedias del ranking.

5. **Influencia del formato**: Se analiza cuál es el formato predominante.

## Requisitos

Para ejecutar los notebooks es necesario tener instaladas las siguientes bibliotecas de Python:

- pandas
- numpy
- matplotlib
- seaborn
- requests
- beautifulsoup4
- selenium
- fake_useragent
- undetected_chromedriver
- spotipy
- requests.exception

## Cómo ejecutar el proyecto

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/tiktok-spotify-analysis.git
   cd tiktok-spotify-analysis
   ```

2. Abre los notebooks en Jupyter Notebook o Jupyter Lab:
   ```bash
   jupyter notebook
   ```

3. Ejecuta cada notebook siguiendo el orden recomendado:
   - Primero, **Scrapper_TikTok.ipynb** para obtener los datos de TikTok.
   - Segundo, **spotify_info.ipynb** para obtener los ids de las caciones y generar las playlists.
   - Tercero, **Scrapper_Musicstax.ipynb** para obtener los metadatos de las canciones.
   - Después, **EDA_TikTok_Spotify.ipynb** para realizar el análisis.


¡Gracias por tu atención!

Nacho Miguelsanz
