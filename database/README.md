# Marble Database

A PostgreSQL database system for managing marble-related data including items, users, and related metadata.

## Database Structure

The database consists of the following main tables:

### Users Table
- Stores user account information
- Fields: id, username, email, created_at, updated_at

### Marble Items Table
- Stores information about marble items/products
- Fields: id, name, description, category, created_by, created_at, updated_at

### Schema Migrations Table
- Tracks applied database migrations
- Fields: version, applied_at

## Setup

### Prerequisites
- Python 3.8 or higher
- PostgreSQL database
- Access to the database credentials

### Installation

1. Install Python dependencies:
```bash
cd database
pip install -r requirements.txt
```

2. Configure environment variables:
Create or update `.env` file in the root directory with your database credentials:
```
DATABASE_HOST=your-host
DATABASE_USER=your-user
DATABASE_PASSWORD=your-password
DATABASE_NAME=your-database-name
```

### Running Migrations

To set up the database schema, run:

```bash
cd database/utils
python db_manager.py migrate
```

This will:
- Create the schema_migrations tracking table
- Apply all migration files in order
- Create all necessary tables and indexes

### Seeding Data

To populate the database with sample test data:

```bash
cd database/utils
python db_manager.py seed
```

### Complete Setup

To run both migrations and seeds in one command:

```bash
cd database/utils
python db_manager.py all
```

## Directory Structure

```
database/
├── schema/           # Schema definition files
│   └── 00_init.sql   # Initial schema
├── migrations/       # Migration files (versioned)
│   └── 001_initial_setup.sql
├── seeds/            # Seed data files
│   └── 001_sample_data.sql
├── utils/            # Utility scripts
│   └── db_manager.py # Database management script
└── requirements.txt  # Python dependencies
```

## Migration System

Migrations are SQL files that:
- Are numbered sequentially (001_, 002_, etc.)
- Include both up migrations and version tracking
- Are applied in order by the migration script
- Track which migrations have been applied in the schema_migrations table

### Creating a New Migration

1. Create a new file in `database/migrations/` with the next sequential number
2. Name it descriptively: `00X_description.sql`
3. Include the SQL changes and a record insertion to schema_migrations

Example:
```sql
-- Migration: Add new column
-- Version: 002

ALTER TABLE marble_items ADD COLUMN price DECIMAL(10,2);

INSERT INTO schema_migrations (version) VALUES ('002_add_price_column')
ON CONFLICT (version) DO NOTHING;
```

## Verification

After running migrations, you can verify the setup by connecting to your database and checking:

```sql
-- Check migrations applied
SELECT * FROM schema_migrations;

-- Check users
SELECT * FROM users;

-- Check marble items
SELECT * FROM marble_items;
```

## Acceptance Criteria

✅ Migrations run successfully without errors
✅ Schema is properly documented
✅ Seed data inserts test data correctly
✅ All tables have appropriate indexes
✅ Connection utility works with environment variables

## Troubleshooting

### Connection Issues
- Verify `.env` file exists and has correct credentials
- Check that the database server is accessible
- Ensure SSL is enabled if required by your host

### Migration Errors
- Migrations are designed to be idempotent (can run multiple times)
- Check the schema_migrations table to see which migrations have been applied
- Review error messages for SQL syntax or constraint violations

## Future Enhancements

Potential improvements to consider:
- Add rollback/down migrations
- Implement database versioning
- Add more comprehensive seed data
- Create database backup scripts
- Add data validation triggers
