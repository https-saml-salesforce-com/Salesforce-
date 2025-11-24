#!/usr/bin/env python3
"""
Test script to validate the database setup
Run this after migrations and seeds have been applied
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from db_manager import get_db_connection

def test_connection():
    """Test database connection"""
    print("Testing database connection...")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT version();')
        version = cursor.fetchone()
        print(f"✓ Connected to PostgreSQL: {version[0][:50]}...")
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"✗ Connection failed: {e}")
        return False

def test_schema_migrations_table():
    """Test that schema_migrations table exists"""
    print("\nTesting schema_migrations table...")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM schema_migrations;")
        count = cursor.fetchone()[0]
        print(f"✓ schema_migrations table exists with {count} migration(s)")
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"✗ Test failed: {e}")
        return False

def test_users_table():
    """Test that users table exists and has data"""
    print("\nTesting users table...")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM users;")
        count = cursor.fetchone()[0]
        print(f"✓ users table exists with {count} user(s)")
        
        cursor.execute("SELECT username, email FROM users LIMIT 3;")
        users = cursor.fetchall()
        for user in users:
            print(f"  - {user[0]} ({user[1]})")
        
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"✗ Test failed: {e}")
        return False

def test_marble_items_table():
    """Test that marble_items table exists and has data"""
    print("\nTesting marble_items table...")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM marble_items;")
        count = cursor.fetchone()[0]
        print(f"✓ marble_items table exists with {count} item(s)")
        
        cursor.execute("SELECT name, category FROM marble_items LIMIT 3;")
        items = cursor.fetchall()
        for item in items:
            print(f"  - {item[0]} ({item[1]})")
        
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"✗ Test failed: {e}")
        return False

def test_indexes():
    """Test that indexes exist"""
    print("\nTesting indexes...")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT indexname FROM pg_indexes 
            WHERE schemaname = 'public' 
            AND tablename IN ('users', 'marble_items')
            ORDER BY indexname;
        """)
        indexes = cursor.fetchall()
        print(f"✓ Found {len(indexes)} index(es):")
        for idx in indexes:
            print(f"  - {idx[0]}")
        
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"✗ Test failed: {e}")
        return False

def run_all_tests():
    """Run all validation tests"""
    print("=" * 60)
    print("Database Setup Validation Tests")
    print("=" * 60)
    
    tests = [
        test_connection,
        test_schema_migrations_table,
        test_users_table,
        test_marble_items_table,
        test_indexes
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n" + "=" * 60)
    print(f"Results: {sum(results)}/{len(results)} tests passed")
    print("=" * 60)
    
    return all(results)

if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
