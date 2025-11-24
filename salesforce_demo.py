"""
Example script demonstrating Salesforce integration with Abundance Marble database.

This script shows how to:
1. Connect to both systems
2. Fetch data from the database
3. Sync data to Salesforce
4. Handle common scenarios
"""

import sys
import logging
from datetime import datetime
from salesforce_integration import SalesforceIntegration

# Configure detailed logging for demo
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def demo_connection_test():
    """Test connections to both Salesforce and database."""
    print("\n" + "=" * 60)
    print("DEMO: Connection Test")
    print("=" * 60)
    
    integration = SalesforceIntegration()
    
    print("\n1. Testing Salesforce connection...")
    sf_connected = integration.connect_salesforce()
    if sf_connected:
        print("   ✓ Salesforce connection successful")
    else:
        print("   ✗ Salesforce connection failed")
        print("   Please check your SALESFORCE_* environment variables")
    
    print("\n2. Testing database connection...")
    db_connected = integration.connect_database()
    if db_connected:
        print("   ✓ Database connection successful")
    else:
        print("   ✗ Database connection failed")
        print("   Please check your DATABASE_* environment variables")
    
    integration.close_connections()
    
    return sf_connected and db_connected


def demo_sync_contacts():
    """Demonstrate syncing contacts to Salesforce."""
    print("\n" + "=" * 60)
    print("DEMO: Syncing Contacts to Salesforce")
    print("=" * 60)
    
    integration = SalesforceIntegration()
    
    # Connect to both systems
    if not integration.connect_salesforce():
        print("Failed to connect to Salesforce")
        return False
    
    if not integration.connect_database():
        print("Failed to connect to database")
        return False
    
    # Sample contacts data
    sample_contacts = [
        {
            'FirstName': 'John',
            'LastName': 'Marble',
            'Email': 'john.marble@abundance.com',
            'Phone': '555-0101',
            'Title': 'Marble Specialist'
        },
        {
            'FirstName': 'Jane',
            'LastName': 'Stone',
            'Email': 'jane.stone@abundance.com',
            'Phone': '555-0102',
            'Title': 'Database Administrator'
        },
        {
            'FirstName': 'Bob',
            'LastName': 'Abundance',
            'Email': 'bob.abundance@marble.com',
            'Phone': '555-0103',
            'Title': 'Project Manager'
        }
    ]
    
    print(f"\nSyncing {len(sample_contacts)} sample contacts...")
    stats = integration.sync_contacts_to_salesforce(sample_contacts)
    
    print("\nSync Results:")
    print(f"  - Created: {stats['created']}")
    print(f"  - Updated: {stats['updated']}")
    print(f"  - Failed:  {stats['failed']}")
    
    integration.close_connections()
    return True


def demo_sync_accounts():
    """Demonstrate syncing accounts to Salesforce."""
    print("\n" + "=" * 60)
    print("DEMO: Syncing Accounts to Salesforce")
    print("=" * 60)
    
    integration = SalesforceIntegration()
    
    # Connect to both systems
    if not integration.connect_salesforce():
        print("Failed to connect to Salesforce")
        return False
    
    if not integration.connect_database():
        print("Failed to connect to database")
        return False
    
    # Sample accounts data
    sample_accounts = [
        {
            'Name': 'Abundance Marble Corporation',
            'Industry': 'Manufacturing',
            'Phone': '555-1000',
            'Website': 'www.abundancemarble.com',
            'BillingCity': 'New York',
            'BillingState': 'NY',
            'BillingCountry': 'USA'
        },
        {
            'Name': 'Marble Masters Inc',
            'Industry': 'Construction',
            'Phone': '555-2000',
            'Website': 'www.marblemasters.com',
            'BillingCity': 'Los Angeles',
            'BillingState': 'CA',
            'BillingCountry': 'USA'
        }
    ]
    
    print(f"\nSyncing {len(sample_accounts)} sample accounts...")
    stats = integration.sync_accounts_to_salesforce(sample_accounts)
    
    print("\nSync Results:")
    print(f"  - Created: {stats['created']}")
    print(f"  - Updated: {stats['updated']}")
    print(f"  - Failed:  {stats['failed']}")
    
    integration.close_connections()
    return True


def demo_configuration_check():
    """Check and display current configuration."""
    print("\n" + "=" * 60)
    print("DEMO: Configuration Check")
    print("=" * 60)
    
    integration = SalesforceIntegration()
    
    print("\nSalesforce Configuration:")
    if integration.sf_config.is_configured():
        print(f"  ✓ Username: {integration.sf_config.username}")
        print(f"  ✓ Domain: {integration.sf_config.domain}.salesforce.com")
        print(f"  ✓ API Version: {integration.sf_config.api_version}")
        print("  ✓ Password: [CONFIGURED]")
        print("  ✓ Security Token: [CONFIGURED]")
    else:
        print("  ✗ Salesforce not configured")
        print("  Please set environment variables:")
        print("    - SALESFORCE_USERNAME")
        print("    - SALESFORCE_PASSWORD")
        print("    - SALESFORCE_SECURITY_TOKEN")
    
    print("\nDatabase Configuration:")
    if integration.db_config.is_configured():
        print(f"  ✓ Host: {integration.db_config.host}")
        print(f"  ✓ User: {integration.db_config.user}")
        print(f"  ✓ Database: {integration.db_config.name}")
        print("  ✓ Password: [CONFIGURED]")
    else:
        print("  ✗ Database not configured")
        print("  Please check your .env file")


def main():
    """Run all demo scenarios."""
    print("\n" + "=" * 60)
    print("Abundance Marble - Salesforce Integration Demo")
    print("=" * 60)
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Check configuration
    demo_configuration_check()
    
    # Test connections
    if demo_connection_test():
        print("\n✓ All connections successful!")
        
        # Run sync demos
        demo_sync_contacts()
        demo_sync_accounts()
        
        print("\n" + "=" * 60)
        print("Demo completed successfully!")
        print("=" * 60)
    else:
        print("\n✗ Connection test failed")
        print("Please configure your credentials before running sync operations")
        print("\nSteps to configure:")
        print("1. Copy .env.template to .env")
        print("2. Fill in your Salesforce credentials")
        print("3. Verify database credentials")
        print("4. Run this demo again")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
