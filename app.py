from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os
from datetime import datetime
import re

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # TODO: Change this in production

# Helper functions
def load_crew_data():
    """Load crew data from JSON file if it exists"""
    if os.path.exists('crew_data.json'):
        try:
            with open('crew_data.json', 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Error reading crew data file")
            return []
    return []

def save_crew_data(data):
    """Save crew data to JSON file"""
    try:
        with open('crew_data.json', 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving data: {e}")
        return False

def validate_email(email):
    """Basic email validation"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_date(date_str):
    """Validate date format"""
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Routes
@app.route('/')
def index():
    crew_members = load_crew_data()
    return render_template('index.html', crew_members=crew_members)

@app.route('/add', methods=['GET', 'POST'])
def add_crew_member():
    if request.method == 'POST':
        # Get form data
        full_name = request.form.get('full_name', '').strip()
        rank = request.form.get('rank', '').strip()
        nationality = request.form.get('nationality', '').strip()
        date_of_birth = request.form.get('date_of_birth', '').strip()
        contact_number = request.form.get('contact_number', '').strip()
        email = request.form.get('email', '').strip()

        # Validate inputs
        if not all([full_name, rank, nationality, date_of_birth, contact_number, email]):
            flash('All fields are required!', 'danger')
            return redirect(url_for('add_crew_member'))

        if not validate_date(date_of_birth):
            flash('Invalid date format. Please use YYYY-MM-DD', 'danger')
            return redirect(url_for('add_crew_member'))

        if not validate_email(email):
            flash('Invalid email address!', 'danger')
            return redirect(url_for('add_crew_member'))

        # Create new crew member
        new_member = {
            'full_name': full_name,
            'rank': rank,
            'nationality': nationality,
            'date_of_birth': date_of_birth,
            'contact_number': contact_number,
            'email': email
        }

        # Load existing data and append new member
        crew_members = load_crew_data()
        crew_members.append(new_member)

        # Save updated data
        if save_crew_data(crew_members):
            flash('Crew member added successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Error saving crew member data!', 'danger')
            return redirect(url_for('add_crew_member'))

    return render_template('add.html')

@app.route('/delete/<int:index>', methods=['POST'])
def delete_crew_member(index):
    crew_members = load_crew_data()
    
    if 0 <= index < len(crew_members):
        crew_members.pop(index)
        if save_crew_data(crew_members):
            flash('Crew member deleted successfully!', 'success')
        else:
            flash('Error deleting crew member!', 'danger')
    else:
        flash('Invalid crew member index!', 'danger')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True) 