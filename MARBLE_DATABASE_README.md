# Marble Business Database

This repository contains a database of marble and ceramic businesses and practitioners, primarily focused on Nigeria.

## Database Files

### 1. marble_businesses.json
A JSON-formatted database containing:
- **businesses**: Array of marble and ceramic business entities
- **members**: Array of individual members/practitioners
- **metadata**: Database version and statistics

### 2. marble_businesses.csv
CSV format of business information with columns:
- Business ID
- Business Name
- Registration Number
- Association
- Address, City, State, Postal Code, Country
- Coordinates (Plus Code)
- Phone, Email
- Area Served
- Status
- Created Date
- Salesforce Opportunity ID

### 3. marble_members.csv
CSV format of member information with columns:
- Member ID
- Business ID (foreign key to businesses)
- Name
- Designation
- Phone
- Business Name
- Office Address
- Location Coordinates
- Association
- Association Registration Number
- Membership Date
- Status

## Current Entries

### Businesses
1. **Abundance Marble & Ceramic Works**
   - Registration: RC NO: 8388715
   - Location: Ido-Osun, Osun State, Nigeria
   - Coordinates: QFMP+P3G
   - Phone: 08137665702
   - Association: Marble Works and Designs Practitioners Association, Osun State

### Members
1. **James John Ayo**
   - Business: Abundance Marble & Ceramic Works
   - Designation: Member
   - Phone: 08137665702
   - Location: Ido-Osun, Osun State

## Data Sources
- Salesforce Opportunity: 006QH00000F8e4UYAR
- Membership Card: Marble Works and Designs Practitioners Association, Osun State

## Adding New Entries

To add new businesses or members:
1. Edit the JSON file with proper structure
2. Update the CSV files accordingly
3. Increment the total counts in metadata
4. Update the last_updated timestamp

## Location Format
- Coordinates use Plus Code format (e.g., QFMP+P3G)
- Full address includes: Street/Area, City, State, Postal Code, Country

## Status Values
- **active**: Currently operating
- **inactive**: No longer operating
- **pending**: Verification pending
