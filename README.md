# Seafarer Management System

A simple application to manage seafarer data, available as both a command-line interface and a web application.

## Features

- Add new crew members with details like name, rank, nationality, etc.
- View all crew members in a formatted table
- Delete crew members
- Save data to a JSON file
- Load data from a JSON file when the application starts

## Command-Line Interface

1. Run the application:
   ```
   python seafarer_manager.py
   ```

2. Use the menu options:
   - Option 1: Add a new crew member
   - Option 2: View all crew members
   - Option 3: Save data to file
   - Option 4: Exit the application

## Web Interface

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the Flask application:
   ```
   python app.py
   ```

3. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

4. Use the web interface to:
   - View all crew members
   - Add new crew members
   - Delete crew members

## Data Storage

Both interfaces use the same JSON file (`crew_data.json`) to store crew member data, so you can switch between interfaces and your data will be preserved.

## Requirements

- Python 3.6 or higher
- Flask (for web interface) 