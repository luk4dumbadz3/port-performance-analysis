# Port Performance Analysis Tool

This project provides a comprehensive suite of tools for analyzing port performance metrics, including vessel turnaround times, berth occupancy, and container dwell times.

## Features

- Calculate average vessel turnaround times
- Analyze container dwell times
- Generate visualizations of turnaround time distributions
- Create interactive shipping route maps
- Calculate berth occupancy rates
- Determine Economic Order Quantity (EOQ)
- SQL queries for vessel data analysis

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Python Functions

```python
from port_analysis import (
    calculate_turnaround_time,
    analyze_container_dwell_times,
    create_turnaround_histogram,
    create_route_map,
    calculate_berth_occupancy,
    calculate_eoq
)

# Example usage:
# df = pd.read_csv('vessel_data.csv')
# avg_turnaround = calculate_turnaround_time(df)
```

### SQL Queries

The `port_queries.sql` file contains various SQL queries for analyzing vessel data. These can be executed in your preferred SQL database management system.

## Key Concepts

### Berth Occupancy
Berth occupancy refers to the percentage of time that a berth is occupied by vessels. It's calculated as:
```
Occupancy Rate = (Total time berth is occupied / Total available time) × 100
```

### Gross Tonnage vs Deadweight Tonnage
- **Gross Tonnage**: A measure of the vessel's total internal volume
- **Deadweight Tonnage**: The maximum weight a vessel can carry (cargo, fuel, water, etc.)

### Economic Order Quantity (EOQ)
EOQ is calculated using the formula:
```
EOQ = √(2 × Annual Demand × Ordering Cost / Holding Cost)
```

## Data Requirements

The analysis functions expect the following data formats:

1. Vessel Data:
   - Arrival_Time (datetime)
   - Departure_Time (datetime)
   - vessel_id (string)
   - vessel_type (string)

2. Container Data:
   - dwell_time (float)
   - container_id (string)

3. Route Data:
   - start_lat (float)
   - start_lon (float)
   - end_lat (float)
   - end_lon (float)

## Contributing

Feel free to submit issues and enhancement requests! 