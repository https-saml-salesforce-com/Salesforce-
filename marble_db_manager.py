#!/usr/bin/env python3
"""
Marble Database Management Script

This script provides utilities to manage and query the marble business database.
"""

import json
import csv
from datetime import datetime
from typing import Dict, List, Optional


class MarbleDatabase:
    """Manager for marble business database operations"""
    
    def __init__(self, json_file='marble_businesses.json'):
        self.json_file = json_file
        self.data = self.load_data()
    
    def load_data(self) -> Dict:
        """Load database from JSON file"""
        try:
            with open(self.json_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                'businesses': [],
                'members': [],
                'metadata': {
                    'version': '1.0',
                    'last_updated': datetime.now().isoformat(),
                    'total_businesses': 0,
                    'total_members': 0,
                    'description': 'Database of marble and ceramic businesses and practitioners in Nigeria'
                }
            }
    
    def save_data(self):
        """Save database to JSON file"""
        self.data['metadata']['last_updated'] = datetime.now().isoformat()
        self.data['metadata']['total_businesses'] = len(self.data['businesses'])
        self.data['metadata']['total_members'] = len(self.data['members'])
        
        with open(self.json_file, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def get_business_by_id(self, business_id: str) -> Optional[Dict]:
        """Retrieve business by ID"""
        for business in self.data['businesses']:
            if business['id'] == business_id:
                return business
        return None
    
    def get_business_by_name(self, name: str) -> Optional[Dict]:
        """Retrieve business by name"""
        for business in self.data['businesses']:
            if business['name'].lower() == name.lower():
                return business
        return None
    
    def get_member_by_id(self, member_id: str) -> Optional[Dict]:
        """Retrieve member by ID"""
        for member in self.data['members']:
            if member['id'] == member_id:
                return member
        return None
    
    def get_members_by_business(self, business_id: str) -> List[Dict]:
        """Get all members of a specific business"""
        return [m for m in self.data['members'] if m['business_id'] == business_id]
    
    def list_businesses(self) -> List[Dict]:
        """List all businesses"""
        return self.data['businesses']
    
    def list_members(self) -> List[Dict]:
        """List all members"""
        return self.data['members']
    
    def export_to_csv(self):
        """Export database to CSV files"""
        # Export businesses
        if self.data['businesses']:
            with open('marble_businesses.csv', 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=[
                    'Business ID', 'Business Name', 'Registration Number', 
                    'Association', 'Address', 'City', 'State', 'Postal Code',
                    'Country', 'Coordinates', 'Phone', 'Email', 'Area Served',
                    'Status', 'Created Date', 'Salesforce Opportunity ID'
                ])
                writer.writeheader()
                for business in self.data['businesses']:
                    writer.writerow({
                        'Business ID': business['id'],
                        'Business Name': business['name'],
                        'Registration Number': business['registration_number'],
                        'Association': business['association'],
                        'Address': business['location']['address'],
                        'City': business['location']['city'],
                        'State': business['location']['state'],
                        'Postal Code': business['location']['postal_code'],
                        'Country': business['location']['country'],
                        'Coordinates': business['location']['coordinates'],
                        'Phone': business['contact']['phone'],
                        'Email': business['contact'].get('email', ''),
                        'Area Served': business.get('area_served', ''),
                        'Status': business['status'],
                        'Created Date': business['created_date'],
                        'Salesforce Opportunity ID': business.get('salesforce_opportunity_id', '')
                    })
        
        # Export members
        if self.data['members']:
            with open('marble_members.csv', 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=[
                    'Member ID', 'Business ID', 'Name', 'Designation', 'Phone',
                    'Business Name', 'Office Address', 'Location Coordinates',
                    'Association', 'Association Registration Number',
                    'Database Entry Date', 'Status', 'Notes'
                ])
                writer.writeheader()
                for member in self.data['members']:
                    writer.writerow({
                        'Member ID': member['id'],
                        'Business ID': member['business_id'],
                        'Name': member['name'],
                        'Designation': member['designation'],
                        'Phone': member['phone'],
                        'Business Name': member['business_name'],
                        'Office Address': member['office_address'],
                        'Location Coordinates': member['location_coordinates'],
                        'Association': member['association_membership']['organization'],
                        'Association Registration Number': member['association_membership']['registration_number'],
                        'Database Entry Date': member.get('database_entry_date', member.get('membership_date', '')),
                        'Status': member['status'],
                        'Notes': member['association_membership'].get('note', '')
                    })
    
    def print_summary(self):
        """Print database summary"""
        print("=" * 60)
        print("MARBLE DATABASE SUMMARY")
        print("=" * 60)
        print(f"Version: {self.data['metadata']['version']}")
        print(f"Last Updated: {self.data['metadata']['last_updated']}")
        print(f"Total Businesses: {self.data['metadata']['total_businesses']}")
        print(f"Total Members: {self.data['metadata']['total_members']}")
        print("=" * 60)
        
        print("\nBUSINESSES:")
        print("-" * 60)
        for business in self.data['businesses']:
            print(f"ID: {business['id']}")
            print(f"Name: {business['name']}")
            print(f"Location: {business['location']['city']}, {business['location']['state']}")
            print(f"Phone: {business['contact']['phone']}")
            print(f"Status: {business['status']}")
            print("-" * 60)
        
        print("\nMEMBERS:")
        print("-" * 60)
        for member in self.data['members']:
            print(f"ID: {member['id']}")
            print(f"Name: {member['name']}")
            print(f"Business: {member['business_name']}")
            print(f"Designation: {member['designation']}")
            print(f"Phone: {member['phone']}")
            print("-" * 60)


def main():
    """Main function"""
    db = MarbleDatabase()
    db.print_summary()


if __name__ == '__main__':
    main()
