import unittest
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from port_analysis import (
    calculate_turnaround_time,
    analyze_container_dwell_times,
    create_turnaround_histogram,
    create_route_map,
    calculate_berth_occupancy,
    calculate_eoq
)

class TestPortAnalysis(unittest.TestCase):
    def setUp(self):
        # Create sample data for testing
        self.sample_dates = pd.date_range(start='2024-01-01', periods=5, freq='D')
        self.vessel_data = pd.DataFrame({
            'Arrival_Time': self.sample_dates,
            'Departure_Time': self.sample_dates + timedelta(hours=24),
            'vessel_id': [f'VESSEL_{i}' for i in range(5)],
            'vessel_type': ['Container', 'Bulk', 'Container', 'Tanker', 'Container']
        })
        
        self.container_data = pd.DataFrame({
            'dwell_time': [12, 24, 36, 48, 60],
            'container_id': [f'CONT_{i}' for i in range(5)]
        })
        
        self.route_data = pd.DataFrame({
            'start_lat': [40.7128, 34.0522, 51.5074],
            'start_lon': [-74.0060, -118.2437, -0.1278],
            'end_lat': [34.0522, 51.5074, 40.7128],
            'end_lon': [-118.2437, -0.1278, -74.0060]
        })

    def test_calculate_turnaround_time(self):
        result = calculate_turnaround_time(self.vessel_data)
        self.assertEqual(result, 24.0)  # All vessels have 24-hour turnaround time

    def test_analyze_container_dwell_times(self):
        result = analyze_container_dwell_times(self.container_data)
        self.assertEqual(result['median'], 36.0)
        self.assertEqual(result['mean'], 36.0)
        self.assertEqual(result['min'], 12.0)
        self.assertEqual(result['max'], 60.0)

    def test_calculate_berth_occupancy(self):
        result = calculate_berth_occupancy(self.vessel_data)
        self.assertAlmostEqual(result, 100.0, places=2)  # Should be 100% as vessels occupy all time

    def test_calculate_eoq(self):
        result = calculate_eoq(demand_rate=1000, ordering_cost=100, holding_cost=2)
        expected = np.sqrt((2 * 1000 * 100) / 2)
        self.assertAlmostEqual(result, expected, places=2)

if __name__ == '__main__':
    unittest.main() 