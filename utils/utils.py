# Función para estructurar visualizaciones
def custom_sort(area):
    if "Europe" in area:
        return 1
    elif "America" in area:
        return 2
    elif "Asia" in area:
        return 3
    else:
        return 4
# Función para asignar tempo y dance_ind
def traduccion_bpm(bpm):
    if bpm < 40:
        return "Muy lento"
    elif 40 <= bpm <= 60:
        return "Largo"
    elif 60 < bpm <= 66:
        return "Larghetto"
    elif 66 < bpm <= 76:
        return "Adagio"
    elif 76 < bpm <= 108:
        return "Andante"
    elif 108 < bpm <= 120:
        return "Moderato"
    elif 120 < bpm <= 156:
        return "Allegro"
    elif 156 < bpm <= 176:
        return "Vivace"
    elif 176 < bpm <= 200:
        return "Presto"
    else:
        return "Prestissimo"
    #(0-20,20-40,40-60,60-80,80-100)
def ind_dance(danceability):
    if danceability < 20:
        return "0-20"
    elif 20 <= danceability <= 40:
        return "20-40"
    elif 40 < danceability <= 60:
        return "40-60"
    elif 60 < danceability <= 80:
        return "60-80"
    elif 80 < danceability <= 100:
        return "80-100"


def ind_pos(positiveness):
    if positiveness < 20:
        return "0-20"
    elif 20 <= positiveness <= 40:
        return "20-40"
    elif 40 < positiveness <= 60:
        return "40-60"
    elif 60 < positiveness <= 80:
        return "60-80"
    elif 80 < positiveness <= 100:
        return "80-100"

def group_rank(ranking):
    if 1 > ranking <= 5:
        return "1-5"
    elif 5 > ranking <= 10:
        return "6-10"
    elif 10 > ranking <= 15:
        return "10-15"
    elif 15 > ranking <= 20:
        return "16-20"
    elif 20 > ranking <= 25:
        return "20-25"
    elif 25 > ranking <= 30:
        return "26-30"
    elif 30 > ranking <= 35:
        return "30-35"
    elif 35 > ranking <= 40:
        return "36-40"
    elif 40 > ranking <= 45:
        return "40-45"
    elif 45 > ranking <= 50:
        return "46-50"    
    
def parse_release_date(release_date):
    try:
        # Comprabamos si es un año o fecha entera
        if release_date.isdigit() and len(release_date) == 4:
            return int(release_date)  
        else:
            # Si no lo trabajamos para parsear la fecha
            parsed_date = pd.to_datetime(release_date, errors='coerce')
            if pd.notna(parsed_date):
                return parsed_date  # Devuelve la fecha completa
    except Exception as e:
        print(f"Error al parsear {release_date}: {e}")
    return None  # Devuelve None si no se puede procesar

#Parseo de ms a minutos:segundos    
def format_duration(ms):
    # Convertir milisegundos a segundos (como enteros)
    seconds = int(ms // 1000)
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02d}:{seconds:02d}"

# Normalizar las características para radar plot
def normalize_features(features):
    min_max_values = {
        'loudness_db': (top50_songs_world['loudness_db'].min(), top50_songs_world['loudness_db'].max()),    # Escala típica de loudness en dB
        'energy': (0, 100),
        'danceability': (0, 100),
        'positiveness': (0, 100),
        'speechiness': (0, 100),
        'liveness': (0, 100),
        'acousticness': (0, 100),
        'instrumentalness': (0, 100),      
        'tempo_bpm': (0, 240),          # BPM típicos
        'Duration': (0, (top50_songs_world['Duration'].quantile(.99))), # Seleccionamos como máximo el percentil 99 para evitar desviaciones por outlier       
        'Explicit': (0, 1),        
        'Popularity': (0, 100),
        'mode': (0,1)     
    }
    return {key: (value - min_value) / (max_value - min_value)
            for key, value in features.items()
            for min_value, max_value in [min_max_values[key]]}
