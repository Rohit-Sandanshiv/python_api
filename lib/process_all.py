import uuid
from lib.utils import create_global_id, get_consumer_key
from lib.mapping import consumer_ddl, social_contact_ddl, purchase_ddl, address_ddl
from .db_connection import get_db_connection


def insert_backend(pii_data, address_data, social_data, purchase_data):
    """Inserts consumer data into multiple tables in the database."""
    global_id = create_global_id()
    emp_pk_id, social_pk_id, purchase_pk_id, address_pk_id = [str(uuid.uuid4()) for _ in range(4)]

    queries = [
        ("INSERT INTO Consumer (GlobalId, consumer_pk_id, FirstName, LastName, JoinDate, is_active, is_member, "
         "is_frequent_buyer) VALUES (?, ?, ?, ?, ?, 1, 1, 1);",
         (global_id, emp_pk_id, pii_data.get("FirstName"), pii_data.get("LastName"), pii_data.get("JoinDate"))),

        ("INSERT INTO SocialContact (social_pk_id, ConsumerKey, Email, Mobile, whatsAppID) VALUES (?, ?, ?, ?, ?);",
         (social_pk_id, emp_pk_id, social_data.get("Email"), social_data.get("Mobile"), social_data.get("whatsAppID"))),

        ("INSERT INTO Purchase (purchase_pk_id, ConsumerKey, ProductID, InvoiceDate, BilledAmount, quantity) VALUES ("
         "?, ?, ?, ?, ?, ?);",
         (purchase_pk_id, emp_pk_id, purchase_data.get("ProductID"), purchase_data.get("InvoiceDate"),
          purchase_data.get("BilledAmount"), purchase_data.get("quantity"))),

        ("INSERT INTO Address (address_pk_id, ConsumerKey, AddressID, AddressLine1, AddressLine2, City, State, "
         "Country, ZipCode) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);",
         (address_pk_id, emp_pk_id, address_data.get("AddressID"), address_data.get("AddressLine1"),
          address_data.get("AddressLine2"), address_data.get("City"), address_data.get("State"),
          address_data.get("Country"), address_data.get("ZipCode")))
    ]

    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            for query, params in queries:
                cursor.execute(query, params)
            conn.commit()
        return 1
    except Exception as e:
        print(f"Error inserting data: {e}")
        return 0


def update_backend(globalID, pii_data, address_data, social_data, purchase_data):
    """Updates consumer records and inserts new purchase records."""
    mapping = {"Consumer": pii_data, "Address": address_data, "SocialContact": social_data}
    mapping_ddl = {"Consumer": consumer_ddl, "Address": address_ddl, "SocialContact": social_contact_ddl}

    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            consumer_key = get_consumer_key(globalID)

            # Update Consumer, Address, and SocialContact
            for table, data in mapping.items():
                update_keys = [k for k in data if k in mapping_ddl[table] and data.get(k) is not None]
                if update_keys:
                    set_clause = ", ".join([f"{col} = ?" for col in update_keys])
                    query = f"UPDATE {table} SET {set_clause} WHERE {'GlobalId' if table == 'Consumer' else 'ConsumerKey'} = ?"
                    cursor.execute(query, (*[data[k] for k in update_keys], globalID if table == "Consumer" else consumer_key))

            # Insert new purchase record
            query_purchase = """
            INSERT INTO Purchase (purchase_pk_id, ConsumerKey, ProductID, InvoiceDate, BilledAmount, quantity)
            VALUES (?, ?, ?, ?, ?, ?);
            """
            cursor.execute(query_purchase, (str(uuid.uuid4()), consumer_key, purchase_data.get("ProductID"),
                                            purchase_data.get("InvoiceDate"), purchase_data.get("BilledAmount"),
                                            purchase_data.get("quantity")))

            conn.commit()
        return 1
    except Exception as e:
        print(f"Error updating data: {e}")
        return 0
