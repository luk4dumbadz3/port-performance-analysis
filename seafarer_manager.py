#!/usr/bin/env python3
"""
Seafarer Management System

A simple command-line application to manage seafarer data.
"""

import os
import sys
from datetime import datetime
import json

# Global variable to store crew members
crew_members = []

# Load existing data if available
try:
    if os.path.exists('crew_data.json'):
        with open('crew_data.json', 'r') as f:
            crew_members = json.load(f)
        print(f"Loaded {len(crew_members)} crew members from file.")
except Exception as e:
    print(f"Error loading data: {e}")

# Main program loop
while True:
    # Clear screen for better readability
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Display menu
    print("\n=== Seafarer Management System ===")
    print("1. Add a new crew member")
    print("2. View all crew members")
    print("3. Save data")
    print("4. Exit")
    print("================================")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    # Add a new crew member
    if choice == '1':
        print("\n=== Add New Crew Member ===")
        
        # Get crew member information
        full_name = input("Full Name: ").strip()
        while not full_name:
            print("Name cannot be empty.")
            full_name = input("Full Name: ").strip()
        
        rank = input("Rank: ").strip()
        while not rank:
            print("Rank cannot be empty.")
            rank = input("Rank: ").strip()
        
        nationality = input("Nationality: ").strip()
        while not nationality:
            print("Nationality cannot be empty.")
            nationality = input("Nationality: ").strip()
        
        date_of_birth = input("Date of Birth (YYYY-MM-DD): ").strip()
        while True:
            try:
                datetime.strptime(date_of_birth, '%Y-%m-%d')
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                date_of_birth = input("Date of Birth (YYYY-MM-DD): ").strip()
        
        contact_number = input("Contact Number: ").strip()
        while not contact_number:
            print("Contact number cannot be empty.")
            contact_number = input("Contact Number: ").strip()
        
        email = input("Email Address: ").strip()
        while not email or '@' not in email:
            print("Please enter a valid email address.")
            email = input("Email Address: ").strip()
        
        # Create crew member dictionary
        crew_member = {
            'full_name': full_name,
            'rank': rank,
            'nationality': nationality,
            'date_of_birth': date_of_birth,
            'contact_number': contact_number,
            'email': email
        }
        
        # Add to the list
        crew_members.append(crew_member)
        print(f"\nCrew member {full_name} added successfully!")
    
    # View all crew members
    elif choice == '2':
        if not crew_members:
            print("\nNo crew members found in the system.")
        else:
            print("\n=== Crew Members ===")
            print(f"{'Full Name':<30} {'Rank':<20} {'Nationality':<15} {'Date of Birth':<12} {'Contact':<15} {'Email':<25}")
            print("-" * 120)
            
            for member in crew_members:
                print(f"{member['full_name']:<30} {member['rank']:<20} {member['nationality']:<15} "
                      f"{member['date_of_birth']:<12} {member['contact_number']:<15} {member['email']:<25}")
            
            print(f"\nTotal crew members: {len(crew_members)}")
    
    # Save data
    elif choice == '3':
        try:
            with open('crew_data.json', 'w') as f:
                json.dump(crew_members, f, indent=4)
            print("\nData saved successfully to crew_data.json")
        except Exception as e:
            print(f"\nError saving data: {e}")
    
    # Exit
    elif choice == '4':
        # Ask if user wants to save before exiting
        if crew_members:
            save_choice = input("\nDo you want to save data before exiting? (y/n): ").strip().lower()
            if save_choice == 'y':
                try:
                    with open('crew_data.json', 'w') as f:
                        json.dump(crew_members, f, indent=4)
                    print("\nData saved successfully to crew_data.json")
                except Exception as e:
                    print(f"\nError saving data: {e}")
        print("\nThank you for using the Seafarer Management System. Goodbye!")
        sys.exit(0)
    
    # Invalid choice
    else:
        print("\nInvalid choice. Please try again.")
    
    input("\nPress Enter to continue...") 