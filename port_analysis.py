import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import folium
from typing import Union, List, Dict
import pytz
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def calculate_turnaround_time(df: pd.DataFrame) -> float:
    """
    Calculate the average turnaround time from a DataFrame containing arrival and departure times.
    
    Args:
        df (pd.DataFrame): DataFrame with 'Arrival_Time' and 'Departure_Time' columns
        
    Returns:
        float: Average turnaround time in hours
    """
    try:
        # Ensure datetime columns are in datetime format
        df['Arrival_Time'] = pd.to_datetime(df['Arrival_Time'])
        df['Departure_Time'] = pd.to_datetime(df['Departure_Time'])
        
        # Calculate turnaround time in hours
        turnaround_times = (df['Departure_Time'] - df['Arrival_Time']).dt.total_seconds() / 3600
        
        # Log statistics
        logger.info(f"Calculated turnaround times - Mean: {turnaround_times.mean():.2f} hours")
        logger.info(f"Min turnaround time: {turnaround_times.min():.2f} hours")
        logger.info(f"Max turnaround time: {turnaround_times.max():.2f} hours")
        
        return turnaround_times.mean()
    except Exception as e:
        logger.error(f"Error calculating turnaround time: {str(e)}")
        raise

def analyze_container_dwell_times(df: pd.DataFrame) -> Dict[str, float]:
    """
    Analyze container dwell times and return key statistics.
    
    Args:
        df (pd.DataFrame): DataFrame with dwell time data
        
    Returns:
        Dict[str, float]: Dictionary containing median and standard deviation
    """
    try:
        dwell_times = df['dwell_time'].astype(float)
        
        stats = {
            'median': dwell_times.median(),
            'std_dev': dwell_times.std(),
            'mean': dwell_times.mean(),
            'min': dwell_times.min(),
            'max': dwell_times.max()
        }
        
        logger.info(f"Container dwell time analysis completed - Median: {stats['median']:.2f} hours")
        return stats
    except Exception as e:
        logger.error(f"Error analyzing container dwell times: {str(e)}")
        raise

def create_turnaround_histogram(df: pd.DataFrame, output_path: str = 'turnaround_histogram.png'):
    """
    Create a histogram of vessel turnaround times.
    
    Args:
        df (pd.DataFrame): DataFrame with arrival and departure times
        output_path (str): Path to save the histogram
    """
    try:
        turnaround_times = (df['Departure_Time'] - df['Arrival_Time']).dt.total_seconds() / 3600
        
        plt.figure(figsize=(10, 6))
        plt.hist(turnaround_times, bins=30, edgecolor='black')
        plt.title('Distribution of Vessel Turnaround Times')
        plt.xlabel('Turnaround Time (hours)')
        plt.ylabel('Frequency')
        
        # Add mean and median lines
        plt.axvline(turnaround_times.mean(), color='r', linestyle='dashed', linewidth=1, label=f'Mean: {turnaround_times.mean():.2f}')
        plt.axvline(turnaround_times.median(), color='g', linestyle='dashed', linewidth=1, label=f'Median: {turnaround_times.median():.2f}')
        plt.legend()
        
        plt.savefig(output_path)
        plt.close()
        
        logger.info(f"Histogram saved to {output_path}")
    except Exception as e:
        logger.error(f"Error creating histogram: {str(e)}")
        raise

def create_route_map(routes_df: pd.DataFrame, output_path: str = 'route_map.html'):
    """
    Create an interactive map showing shipping routes using Folium.
    
    Args:
        routes_df (pd.DataFrame): DataFrame with route data including coordinates
        output_path (str): Path to save the HTML map
    """
    try:
        # Create a base map centered on the average coordinates
        center_lat = routes_df['latitude'].mean()
        center_lon = routes_df['longitude'].mean()
        m = folium.Map(location=[center_lat, center_lon], zoom_start=4)
        
        # Add route lines with different colors based on frequency
        route_counts = routes_df.groupby(['start_lat', 'start_lon', 'end_lat', 'end_lon']).size()
        
        for (start_lat, start_lon, end_lat, end_lon), count in route_counts.items():
            color = 'blue' if count < 5 else 'red' if count < 10 else 'green'
            folium.PolyLine(
                locations=[[start_lat, start_lon], [end_lat, end_lon]],
                weight=2,
                color=color,
                opacity=0.8,
                popup=f'Frequency: {count}'
            ).add_to(m)
        
        m.save(output_path)
        logger.info(f"Route map saved to {output_path}")
    except Exception as e:
        logger.error(f"Error creating route map: {str(e)}")
        raise

def calculate_berth_occupancy(df: pd.DataFrame) -> float:
    """
    Calculate berth occupancy rate.
    
    Args:
        df (pd.DataFrame): DataFrame with berth usage data
        
    Returns:
        float: Berth occupancy rate as a percentage
    """
    try:
        total_time = (df['Departure_Time'].max() - df['Arrival_Time'].min()).total_seconds()
        occupied_time = (df['Departure_Time'] - df['Arrival_Time']).sum().total_seconds()
        
        occupancy_rate = (occupied_time / total_time) * 100
        logger.info(f"Calculated berth occupancy rate: {occupancy_rate:.2f}%")
        
        return occupancy_rate
    except Exception as e:
        logger.error(f"Error calculating berth occupancy: {str(e)}")
        raise

def calculate_eoq(demand_rate: float, ordering_cost: float, holding_cost: float) -> float:
    """
    Calculate Economic Order Quantity (EOQ).
    
    Args:
        demand_rate (float): Annual demand rate
        ordering_cost (float): Cost per order
        holding_cost (float): Annual holding cost per unit
        
    Returns:
        float: Economic Order Quantity
    """
    try:
        eoq = np.sqrt((2 * demand_rate * ordering_cost) / holding_cost)
        logger.info(f"Calculated EOQ: {eoq:.2f} units")
        return eoq
    except Exception as e:
        logger.error(f"Error calculating EOQ: {str(e)}")
        raise 