"""
Configuration settings for the port performance analysis tool.
"""

# Database settings
DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'port_analysis',
    'user': 'postgres',
    'password': ''  # Set this in environment variables
}

# Analysis settings
ANALYSIS_CONFIG = {
    'turnaround_time_threshold': 48,  # hours
    'dwell_time_threshold': 72,  # hours
    'berth_occupancy_threshold': 80,  # percentage
    'min_vessels_for_analysis': 10
}

# Visualization settings
VIZ_CONFIG = {
    'histogram_bins': 30,
    'map_zoom_level': 4,
    'route_colors': {
        'low_frequency': 'blue',
        'medium_frequency': 'red',
        'high_frequency': 'green'
    },
    'frequency_thresholds': {
        'medium': 5,
        'high': 10
    }
}

# Logging settings
LOG_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(levelname)s - %(message)s',
    'file': 'port_analysis.log'
}

# EOQ calculation settings
EOQ_CONFIG = {
    'default_holding_cost': 2.0,  # per unit per year
    'default_ordering_cost': 100.0,  # per order
    'safety_stock_factor': 1.5
} 