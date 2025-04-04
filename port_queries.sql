-- Query to retrieve vessel IDs and turnaround times
SELECT 
    vessel_id,
    EXTRACT(EPOCH FROM (departure_time - arrival_time))/3600 as turnaround_time_hours
FROM vessel_data
WHERE departure_time IS NOT NULL 
AND arrival_time IS NOT NULL;

-- Query to calculate average turnaround time by vessel type
SELECT 
    vessel_type,
    AVG(EXTRACT(EPOCH FROM (departure_time - arrival_time))/3600) as avg_turnaround_time_hours
FROM vessel_data
GROUP BY vessel_type;

-- Query to find vessels with turnaround times exceeding threshold
SELECT 
    vessel_id,
    vessel_name,
    EXTRACT(EPOCH FROM (departure_time - arrival_time))/3600 as turnaround_time_hours
FROM vessel_data
WHERE EXTRACT(EPOCH FROM (departure_time - arrival_time))/3600 > 48
ORDER BY turnaround_time_hours DESC;

-- Query to calculate berth utilization
SELECT 
    berth_id,
    COUNT(*) as total_vessels,
    AVG(EXTRACT(EPOCH FROM (departure_time - arrival_time))/3600) as avg_turnaround_time,
    SUM(EXTRACT(EPOCH FROM (departure_time - arrival_time))/3600) as total_occupancy_hours
FROM vessel_data
GROUP BY berth_id
ORDER BY total_occupancy_hours DESC; 