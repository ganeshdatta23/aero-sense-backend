-- Sample Queries for AeroSense

-- 1. Get the 10 most recent flight records
SELECT * FROM raw_flights 
ORDER BY timestamp DESC 
LIMIT 10;

-- 2. Count flights by source
SELECT source, COUNT(*) 
FROM raw_flights 
GROUP BY source;

-- 3. Get weather data for a specific location
SELECT * FROM raw_weather 
WHERE latitude = '40.7128' AND longitude = '-74.0060' 
ORDER BY timestamp DESC;

-- 4. Extract specific flight data from JSONB payload (example for OpenSky)
-- Note: Adjust based on the actual JSON structure
SELECT 
    timestamp,
    payload->>'icao24' as icao24,
    payload->>'callsign' as callsign,
    payload->>'origin_country' as origin_country
FROM raw_flights
LIMIT 5;

-- 5. Delete records older than 30 days
-- DELETE FROM raw_flights WHERE timestamp < NOW() - INTERVAL '30 days';
-- DELETE FROM raw_weather WHERE timestamp < NOW() - INTERVAL '30 days';
