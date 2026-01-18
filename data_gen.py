import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime, timedelta

def generate_data(num_records=15000):
    np.random.seed(42)
    
    # Definimos 5 zonas calientes (Lat, Lon) en Bogota
    hotspots = [
        (4.6019, -74.0721), # Centro
        (4.6486, -74.0620), # Chapinero
        (4.6304, -74.1456), # Kennedy
        (4.7410, -74.0841), # Suba
        (4.7110, -74.0710)  # Calle 100
    ]
    
    latitudes = []
    longitudes = []
    
    for _ in range(num_records):
        center = hotspots[np.random.randint(0, len(hotspots))]
        latitudes.append(np.random.normal(center[0], 0.008))
        longitudes.append(np.random.normal(center[1], 0.008))

    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    date_range = (end_date - start_date).days
    
    localidades = ['Chapinero', 'Usaquén', 'Suba', 'Kennedy', 'Bosa', 'Engativá', 'Santa Fe', 'Teusaquillo', 'Ciudad Bolívar']
    modalidades = ['Atraco', 'Cosquilleo', 'Rompimiento vidrio', 'Escopolamina']
    armas = ['Arma de fuego', 'Arma blanca', 'Contundentes', 'Sin empleo de armas']
    
    data = {
        'fecha_hecho': [start_date + timedelta(days=np.random.randint(date_range)) for _ in range(num_records)],
        'localidad': np.random.choice(localidades, num_records),
        'modalidad': np.random.choice(modalidades, num_records),
        'arma_empleada': np.random.choice(armas, num_records),
        'latitud': latitudes,
        'longitud': longitudes,
        'genero': np.random.choice(['Masculino', 'Femenino', 'No reporta'], num_records)
    }
    
    df = pd.DataFrame(data)
    
    horas_prob = [0.01]*6 + [0.03]*4 + [0.05]*4 + [0.08]*4 + [0.10]*4 + [0.05]*2
    horas_prob = [p/sum(horas_prob) for p in horas_prob]
    df['hora_hecho'] = np.random.choice(range(24), num_records, p=horas_prob)
    
    return df

def save_to_sql(df):
    conn = sqlite3.connect('security_db.db')
    df.to_sql('crime_data', conn, if_exists='replace', index=False)
    conn.close()

if __name__ == "__main__":
    df_crime = generate_data()
    save_to_sql(df_crime)
    print("Database created successfully with Clusters.")