#!/usr/bin/env python3
"""
Database connection utility for Marble Database
Provides functions to connect to PostgreSQL and run migrations
"""

import os
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
from urllib.parse import unquote

# Load environment variables
load_dotenv()

def get_db_connection():
    """Create and return a database connection"""
    try:
        conn = psycopg2.connect(
            host=os.getenv('DATABASE_HOST'),
            user=os.getenv('DATABASE_USER'),
            password=os.getenv('DATABASE_PASSWORD'),
            database=unquote(os.getenv('DATABASE_NAME', 'postgres')),
            sslmode='require'
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        raise

def run_migration(migration_file):
    """Run a single migration file"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        with open(migration_file, 'r') as f:
            sql_content = f.read()
        
        cursor.execute(sql_content)
        conn.commit()
        print(f"Successfully applied migration: {migration_file}")
    except Exception as e:
        conn.rollback()
        print(f"Error applying migration {migration_file}: {e}")
        raise
    finally:
        cursor.close()
        conn.close()

def run_all_migrations():
    """Run all migrations in order"""
    migrations_dir = os.path.join(os.path.dirname(__file__), '..', 'migrations')
    
    # First, ensure the schema_migrations table exists
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS schema_migrations (
                version VARCHAR(255) PRIMARY KEY,
                applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
    finally:
        cursor.close()
        conn.close()
    
    # Get list of migration files
    migration_files = sorted([
        f for f in os.listdir(migrations_dir) 
        if f.endswith('.sql')
    ])
    
    for migration_file in migration_files:
        migration_path = os.path.join(migrations_dir, migration_file)
        run_migration(migration_path)

def seed_database():
    """Run seed data scripts"""
    seeds_dir = os.path.join(os.path.dirname(__file__), '..', 'seeds')
    seed_files = sorted([
        f for f in os.listdir(seeds_dir) 
        if f.endswith('.sql')
    ])
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    for seed_file in seed_files:
        seed_path = os.path.join(seeds_dir, seed_file)
        try:
            with open(seed_path, 'r') as f:
                sql_content = f.read()
            
            cursor.execute(sql_content)
            conn.commit()
            print(f"Successfully seeded data: {seed_file}")
        except Exception as e:
            conn.rollback()
            print(f"Error seeding {seed_file}: {e}")
            raise
    
    cursor.close()
    conn.close()

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python db_manager.py [migrate|seed|all]")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == 'migrate':
        print("Running migrations...")
        run_all_migrations()
        print("Migrations completed successfully!")
    elif command == 'seed':
        print("Seeding database...")
        seed_database()
        print("Database seeded successfully!")
    elif command == 'all':
        print("Running migrations...")
        run_all_migrations()
        print("Seeding database...")
        seed_database()
        print("Database setup completed successfully!")
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
