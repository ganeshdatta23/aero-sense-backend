-- Analytical Marts (Representing transformed data)

-- View: flight_weather_correlation
-- Joins flight data with weather data based on closest timestamp and location (Simplified)
CREATE OR REPLACE VIEW flight_weather_correlation AS
SELECT 
    f.id as flight_id,
    f.timestamp as flight_timestamp,
    w.timestamp as weather_timestamp,
    w.latitude,
    w.longitude,
    f.payload->>'callsign' as callsign,
    w.payload->'current'->>'wind_speed_10m' as wind_speed
FROM raw_flights f
CROSS JOIN LATERAL (
    SELECT * 
    FROM raw_weather rw
    ORDER BY ABS(EXTRACT(EPOCH FROM (rw.timestamp - f.timestamp)))
    LIMIT 1
) w;

-- View: hourly_disruption_metrics
-- Aggregates data by hour (Example structure)
CREATE OR REPLACE VIEW hourly_disruption_metrics AS
SELECT 
    date_trunc('hour', timestamp) as hour,
    COUNT(*) as flight_count,
    -- Example logic: flag as "disrupted" if something in payload suggests it
    COUNT(CASE WHEN (payload->>'velocity')::numeric < 100 THEN 1 END) as slow_flights_count
FROM raw_flights
GROUP BY 1;
