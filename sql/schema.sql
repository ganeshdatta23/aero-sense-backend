-- Schema for AeroSense Database

-- Table: raw_flights
CREATE TABLE IF NOT EXISTS raw_flights (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    source VARCHAR(255) DEFAULT 'opensky',
    payload JSONB
);

-- Table: raw_weather
CREATE TABLE IF NOT EXISTS raw_weather (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    latitude VARCHAR(50),
    longitude VARCHAR(50),
    payload JSONB
);

-- Index for faster queries on timestamps
CREATE INDEX IF NOT EXISTS idx_flights_timestamp ON raw_flights(timestamp);
CREATE INDEX IF NOT EXISTS idx_weather_timestamp ON raw_weather(timestamp);
