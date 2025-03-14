from lib.db_connection import get_db_connection


def add_product(products):
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            for product in products:
                query = """
                INSERT INTO Product (ProductID, ProductName, Price, is_discounted, discount)
                VALUES (?, ?, ?, ?, ?);
                """
                cursor.execute(query, (product.get("ProductID"), product.get("ProductName"), product.get("Price"),
                                       product.get("is_discounted"), product.get("discount")))
                conn.commit()
        return True
    except Exception as e:
        print(f"Error Adding Products: {e}")
        return False
