
# Abundance Marble Database

Database management system and integrations for Abundance Marble project.

## Features

### 🔗 Salesforce Integration
Complete integration with Salesforce CRM for seamless data synchronization. See [SALESFORCE_INTEGRATION.md](SALESFORCE_INTEGRATION.md) for details.

- **Two-way Data Sync**: Synchronize contacts and accounts between Abundance Marble database and Salesforce
- **Automated Connection Management**: Handles authentication and connection lifecycle
- **Error Handling**: Comprehensive logging and error recovery
- **Easy Configuration**: Environment-based configuration

### 📊 Database
PostgreSQL database hosted on Koyeb for the Abundance Marble project.

## Quick Start

### Prerequisites
- Python 3.7+
- PostgreSQL (hosted on Koyeb)
- Salesforce account with API access

### Installation

1. Clone the repository:
```bash
git clone https://github.com/godfirstjohnjames-gmail-com/Marble-database-.git
cd Marble-database-
```

2. Install dependencies:
```bash
pip install -r requirements-salesforce.txt
```

3. Configure environment variables:
```bash
cp .env.template .env
# Edit .env with your credentials
```

### Using Salesforce Integration

Run the demo to test the integration:
```bash
python salesforce_demo.py
```

Or use the module programmatically:
```python
from salesforce_integration import SalesforceIntegration

integration = SalesforceIntegration()
integration.connect_salesforce()
integration.connect_database()
# Perform sync operations
integration.close_connections()
```

## Documentation

- [Salesforce Integration Guide](SALESFORCE_INTEGRATION.md) - Complete setup and usage guide

## Project Structure

```
Marble-database-/
├── salesforce_integration.py    # Main Salesforce integration module
├── salesforce_demo.py            # Demo script with usage examples
├── requirements-salesforce.txt   # Python dependencies
├── .env.template                 # Configuration template
├── .gitignore                    # Git ignore rules
└── SALESFORCE_INTEGRATION.md     # Integration documentation
```

## Configuration

All sensitive configuration is managed through environment variables in the `.env` file:

- `DATABASE_HOST` - PostgreSQL host
- `DATABASE_USER` - Database username  
- `DATABASE_PASSWORD` - Database password
- `DATABASE_NAME` - Database name
- `SALESFORCE_USERNAME` - Salesforce username
- `SALESFORCE_PASSWORD` - Salesforce password
- `SALESFORCE_SECURITY_TOKEN` - Salesforce security token

⚠️ **Never commit the `.env` file to version control**

## Security

- All credentials are stored in environment variables
- `.env` file is excluded from version control via `.gitignore`
- Use `.env.template` as a reference for required configuration

## License

This project is part of the Abundance Marble database system.
