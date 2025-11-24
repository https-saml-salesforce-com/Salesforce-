# Salesforce Integration for Abundance Marble Database

This integration enables seamless data synchronization between the Abundance Marble database and Salesforce CRM.

## Features

- **Database Connection**: Connect to the Abundance Marble PostgreSQL database on Koyeb
- **Salesforce Integration**: Authenticate and interact with Salesforce API
- **Data Synchronization**: Sync contacts and accounts between systems
- **Error Handling**: Comprehensive logging and error management
- **Configurable**: Easy configuration through environment variables

## Prerequisites

- Python 3.7 or higher
- Access to Abundance Marble database
- Salesforce account with API access
- Salesforce security token

## Installation

1. Install required Python packages:

```bash
pip install simple-salesforce psycopg2-binary python-dotenv
```

2. Configure your credentials:

Copy the `.env.template` file to `.env` and fill in your credentials:

```bash
cp .env.template .env
```

Edit `.env` with your actual credentials:
- `SALESFORCE_USERNAME`: Your Salesforce username
- `SALESFORCE_PASSWORD`: Your Salesforce password
- `SALESFORCE_SECURITY_TOKEN`: Your Salesforce security token
- `DATABASE_HOST`: Abundance Marble database host
- `DATABASE_USER`: Database username
- `DATABASE_PASSWORD`: Database password
- `DATABASE_NAME`: Database name (default: "Abundance Marble")

## Getting Salesforce Security Token

1. Log in to Salesforce
2. Go to Settings → My Personal Information → Reset My Security Token
3. Click "Reset Security Token"
4. Check your email for the new security token

## Usage

### Running the Integration

```bash
python salesforce_integration.py
```

### Using as a Module

```python
from salesforce_integration import SalesforceIntegration

# Initialize integration
integration = SalesforceIntegration()

# Connect to Salesforce
integration.connect_salesforce()

# Connect to database
integration.connect_database()

# Sync contacts to Salesforce
contacts = [
    {
        'name': 'John Doe',
        'email': 'john@example.com',
        'phone': '555-0100'
    }
]
stats = integration.sync_contacts_to_salesforce(contacts)
print(f"Synced {stats['created']} contacts")

# Close connections
integration.close_connections()
```

## Configuration Options

### Salesforce Domain

- `login`: Use for production Salesforce instances (default)
- `test`: Use for Salesforce sandbox environments

### API Version

The default API version is 58.0. You can change this by setting:

```
SALESFORCE_API_VERSION=59.0
```

## Data Flow

```
Abundance Marble Database (PostgreSQL)
              ↕
    Salesforce Integration
              ↕
      Salesforce CRM
```

## Sync Operations

### Contacts Sync
- Fetches contacts from Abundance Marble database
- Creates new contacts in Salesforce
- Updates existing contacts based on matching criteria

### Accounts Sync
- Fetches account data from database
- Syncs to Salesforce Account objects
- Maintains data consistency

## Error Handling

The integration includes comprehensive error handling:
- Connection failures are logged with detailed error messages
- Sync failures are tracked and reported
- Failed records are counted in sync statistics

## Logging

Logs include:
- Connection status
- Sync operations progress
- Error messages with stack traces
- Statistics for each sync operation

## Security Considerations

- Never commit `.env` file to version control
- Keep your Salesforce security token secure
- Regularly rotate your Salesforce password and security token
- Use environment-specific credentials for production/test

## Troubleshooting

### Connection Issues

**Problem**: Cannot connect to Salesforce
- Verify your credentials in `.env`
- Check if your IP is whitelisted in Salesforce
- Ensure security token is current

**Problem**: Cannot connect to database
- Verify database host and credentials
- Check network connectivity to Koyeb
- Ensure database is accessible from your location

### Sync Issues

**Problem**: Records failing to sync
- Check Salesforce field mappings
- Verify required fields are populated
- Review error logs for specific failure reasons

## Support

For issues or questions about:
- Abundance Marble database: Contact database administrator
- Salesforce configuration: Refer to Salesforce documentation
- Integration issues: Check logs and error messages

## License

This integration is part of the Abundance Marble database project.
