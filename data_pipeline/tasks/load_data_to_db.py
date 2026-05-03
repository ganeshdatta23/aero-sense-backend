import psycopg2
import psycopg2.extras
from backend.app.core.config import settings

def load_data(table_name, payload, **kwargs):
    """
    Loads raw JSON data into the specified PostgreSQL table.
    """
    conn = psycopg2.connect(settings.sqlalchemy_database_uri)
    cur = conn.cursor()
    
    if table_name == "raw_flights":
        cur.execute(
            "INSERT INTO raw_flights (payload) VALUES (%s)",
            (psycopg2.extras.Json(payload),)
        )
    elif table_name == "raw_weather":
        cur.execute(
            "INSERT INTO raw_weather (latitude, longitude, payload) VALUES (%s, %s, %s)",
            (kwargs.get("lat"), kwargs.get("lon"), psycopg2.extras.Json(payload))
        )
    
    conn.commit()
    cur.close()
    conn.close()
