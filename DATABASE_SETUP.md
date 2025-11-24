# Marble Database - Quick Start Guide

This repository contains a PostgreSQL database schema and migration system for the Marble Database project.

## What's Included

✅ **Database Schema** - Initial schema with users and marble_items tables
✅ **Migration System** - Version-tracked SQL migrations
✅ **Seed Data** - Sample test data for development
✅ **Management Scripts** - Python utilities for database operations
✅ **Documentation** - Comprehensive setup and usage guides

## Quick Setup

### 1. Prerequisites
- Python 3.8+
- PostgreSQL database access
- Database credentials in `.env` file

### 2. Install Dependencies
```bash
cd database
pip install -r requirements.txt
```

### 3. Run Database Setup
```bash
cd database/utils
python db_manager.py all
```

This command will:
- Create all necessary tables
- Apply all migrations
- Insert seed data

### 4. Verify Setup
```bash
python test_db.py
```

## Project Structure

```
.
├── database/
│   ├── README.md              # Detailed documentation
│   ├── schema/                # Schema definitions
│   │   └── 00_init.sql
│   ├── migrations/            # Versioned migrations
│   │   └── 001_initial_setup.sql
│   ├── seeds/                 # Seed data
│   │   └── 001_sample_data.sql
│   ├── utils/                 # Utility scripts
│   │   ├── db_manager.py      # Main management script
│   │   └── test_db.py         # Validation tests
│   └── requirements.txt       # Python dependencies
├── .env                       # Database credentials (not in git)
└── .gitignore                 # Git ignore rules
```

## Database Configuration

The `.env` file in the root directory contains:
```
DATABASE_HOST=your-host
DATABASE_USER=your-user  
DATABASE_PASSWORD=your-password
DATABASE_NAME=your-database-name
```

## Acceptance Criteria

✅ Migrations run successfully without errors
✅ Schema is properly documented  
✅ Seed data inserts test data correctly
✅ All tables have appropriate indexes
✅ Connection utility works with environment variables

## Next Steps

1. Review the detailed [database documentation](database/README.md)
2. Customize the schema for your specific needs
3. Add additional migrations as needed
4. Extend seed data with relevant test cases

## Support

For detailed documentation on:
- Creating new migrations
- Adding seed data
- Database structure
- Troubleshooting

See [database/README.md](database/README.md)
