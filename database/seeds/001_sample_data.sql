-- Seed data for Marble Database
-- This file contains initial test data

-- Insert test users
INSERT INTO users (username, email) VALUES 
    ('admin', 'admin@marble.db'),
    ('testuser', 'test@marble.db'),
    ('demo', 'demo@marble.db')
ON CONFLICT (username) DO NOTHING;

-- Insert sample marble items
-- Note: Since marble_items has no unique constraints, we check for existing data first
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM marble_items LIMIT 1) THEN
        INSERT INTO marble_items (name, description, category, created_by) VALUES 
            ('Classic White Marble', 'High quality white marble from Italy', 'Natural Stone', 1),
            ('Black Marble Slab', 'Premium black marble with white veining', 'Natural Stone', 1),
            ('Green Marble Tile', 'Beautiful green marble tiles', 'Tile', 2),
            ('Marble Sculpture', 'Hand-carved marble sculpture', 'Art', 2),
            ('Polished Marble Floor', 'Commercial grade polished marble flooring', 'Flooring', 1);
    END IF;
END $$;
