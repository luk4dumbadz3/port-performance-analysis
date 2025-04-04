import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import folium
from typing import Union, List, Dict
import pytz

def calculate_turnaround_time(df: pd.DataFrame) -> float:
    """
    Calculate the average turnaround time from a DataFrame containing arrival and departure times.
    
    Args:
        df (pd.DataFrame): DataFrame with 'Arrival_Time' and 'Departure_Time' columns
        
    Returns:
        float: Average turnaround time in hours
    """
    # Ensure datetime columns are in datetime format
    df['Arrival_Time'] = pd.to_datetime(df['Arrival_Time'])
    df['Departure_Time'] = pd.to_datetime(df['Departure_Time'])
    
    # Calculate turnaround time in hours
    turnaround_times = (df['Departure_Time'] - df['Arrival_Time']).dt.total_seconds() / 3600
    
    return turnaround_times.mean()

def analyze_container_dwell_times(df: pd.DataFrame) -> Dict[str, float]:
    """
    Analyze container dwell times and return key statistics.
    
    Args:
        df (pd.DataFrame): DataFrame with dwell time data
        
    Returns:
        Dict[str, float]: Dictionary containing median and standard deviation
    """
    dwell_times = df['dwell_time'].astype(float)
    
    return {
        'median': dwell_times.median(),
        'std_dev': dwell_times.std()
    }

def create_turnaround_histogram(df: pd.DataFrame, output_path: str = 'turnaround_histogram.png'):
    """
    Create a histogram of vessel turnaround times.
    
    Args:
        df (pd.DataFrame): DataFrame with arrival and departure times
        output_path (str): Path to save the histogram
    """
    turnaround_times = (df['Departure_Time'] - df['Arrival_Time']).dt.total_seconds() / 3600
    
    plt.figure(figsize=(10, 6))
    plt.hist(turnaround_times, bins=30, edgecolor='black')
    plt.title('Distribution of Vessel Turnaround Times')
    plt.xlabel('Turnaround Time (hours)')
    plt.ylabel('Frequency')
    plt.savefig(output_path)
    plt.close()

def create_route_map(routes_df: pd.DataFrame, output_path: str = 'route_map.html'):
    """
    Create an interactive map showing shipping routes using Folium.
    
    Args:
        routes_df (pd.DataFrame): DataFrame with route data including coordinates
        output_path (str): Path to save the HTML map
    """
    # Create a base map centered on the average coordinates
    center_lat = routes_df['latitude'].mean()
    center_lon = routes_df['longitude'].mean()
    m = folium.Map(location=[center_lat, center_lon], zoom_start=4)
    
    # Add route lines
    for _, route in routes_df.iterrows():
        folium.PolyLine(
            locations=[[route['start_lat'], route['start_lon']],
                      [route['end_lat'], route['end_lon']]],
            weight=2,
            color='blue',
            opacity=0.8
        ).add_to(m)
    
    m.save(output_path)

def calculate_berth_occupancy(df: pd.DataFrame) -> float:
    """
    Calculate berth occupancy rate.
    
    Args:
        df (pd.DataFrame): DataFrame with berth usage data
        
    Returns:
        float: Berth occupancy rate as a percentage
    """
    total_time = (df['Departure_Time'].max() - df['Arrival_Time'].min()).total_seconds()
    occupied_time = (df['Departure_Time'] - df['Arrival_Time']).sum().total_seconds()
    
    return (occupied_time / total_time) * 100

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
    return np.sqrt((2 * demand_rate * ordering_cost) / holding_cost) 