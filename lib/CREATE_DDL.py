import sqlite3
import os
from db_connection import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

# to ensure foreign key works
cursor.execute("PRAGMA foreign_keys = ON;")

# Create Consumer Table
cursor.execute('DROP TABLE IF EXISTS Consumer')
cursor.execute("""
CREATE TABLE IF NOT EXISTS Consumer (
    GlobalId TEXT,
    consumer_pk_id TEXT PRIMARY KEY,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    JoinDate DATE,
    is_active BOOLEAN,
    is_member BOOLEAN,
    is_frequent_buyer BOOLEAN
);
""")

# Create SocialContact
cursor.execute('DROP TABLE IF EXISTS SocialContact')
cursor.execute("""
CREATE TABLE IF NOT EXISTS SocialContact (
    social_pk_id TEXT PRIMARY KEY,
    ConsumerKey TEXT,
    Email TEXT,
    Mobile TEXT,
    whatsAppID TEXT,
    FOREIGN KEY (ConsumerKey) REFERENCES Consumer(consumer_pk_id) ON DELETE CASCADE
);
""")

# Create Address Table
cursor.execute('DROP TABLE IF EXISTS Address')
cursor.execute("""
CREATE TABLE IF NOT EXISTS Address (
    address_pk_id TEXT PRIMARY KEY,
    ConsumerKey TEXT,
    AddressID TEXT,
    AddressLine1 TEXT,
    AddressLine2 TEXT,
    City TEXT,
    State TEXT,
    Country TEXT,
    ZipCode TEXT,
    FOREIGN KEY (ConsumerKey) REFERENCES Consumer(consumer_pk_id) ON DELETE CASCADE
);
""")

# Create Purchase Table
cursor.execute('DROP TABLE IF EXISTS Purchase')
cursor.execute("""
CREATE TABLE IF NOT EXISTS Purchase (
    purchase_pk_id TEXT PRIMARY KEY,
    ConsumerKey TEXT,
    ProductID TEXT,
    InvoiceDate DATE,
    BilledAmount REAL,
    quantity TEXT,
    FOREIGN KEY (ConsumerKey) REFERENCES Consumer(consumer_pk_id) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID) ON DELETE CASCADE
);
""")

# Create Product Table
cursor.execute('DROP TABLE IF EXISTS Product')
cursor.execute("""
CREATE TABLE IF NOT EXISTS Product (
    ProductID TEXT UNIQUE,
    ProductName TEXT NOT NULL,
    Price REAL NOT NULL,
    is_discounted BOOLEAN,
    discount REAL
);
""")

# Create Product Table
cursor.execute('DROP TABLE IF EXISTS counter_table')
cursor.execute("""
CREATE TABLE IF NOT EXISTS counter_table (
    id INTEGER PRIMARY KEY,
    glob TEXT
);
""")
cursor.execute("""INSERT INTO counter_table VALUES (1, "0000000")""")
conn.commit()

# # Create Membership Table
# cursor.execute('DROP TABLE IF EXISTS Membership')
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS Membership (
#     membership_pk_id TEXT PRIMARY KEY,
#     ConsumerKey TEXT,
#     MembershipName TEXT,
#     MembershipValidity INTEGER,  -- Assuming validity is in months/years
#     MembershipAmount REAL,  -- Allows decimal values
#     membership_activated_Date DATE,
#     FOREIGN KEY (ConsumerKey) REFERENCES Consumer(consumer_pk_id) ON DELETE CASCADE
# );
# """)

print("✅ Database and tables created successfully!")
print("✅ Tables created successfully in dev_consumer_DB")


conn.commit()
conn.close()
