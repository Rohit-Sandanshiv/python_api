import json
import os
import sqlite3
from .db_connection import get_db_connection


def get_global_id(FirstName):
    """Fetches the GlobalId for a given FirstName."""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT GlobalId FROM Consumer WHERE FirstName = ?"
            results = cursor.execute(query, (FirstName,)).fetchall()
            return (results[0][0], True) if results else ("", False)
    except Exception as e:
        print(f"Error fetching GlobalId: {e}")
        return "", False


def create_global_id():
    """Creates a globalId for a consumer"""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            num = cursor.execute(""" SELECT glob from counter_table""").fetchone()[0]
            prefix = 'GLOB-C'
            num = str(int(num) + 1).rjust(len(num), "0")
            global_id = prefix + num
            cursor.execute("""UPDATE counter_table SET glob = ? WHERE id = 1""", (num,))
            conn.commit()
            return global_id
    except Exception as e:
        print(f"Error Creating GlobalId: {e}")
        return ""


def get_consumer_key(global_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT consumer_pk_id FROM Consumer WHERE GlobalId = ?"
    results = cursor.execute(query, (global_id,)).fetchone()  # Use fetchone() for a single row

    if results:  # Check if a row is found
        return results[0]
    else:
        return None  # Return None if no result is found


# print(create_global_id())

