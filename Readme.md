# Python API Project
Consumer Management API:
This is a simple Flask-based API for managing consumers and products. It supports adding, updating, and retrieving consumer details.

## Features
- Insert consumer details including personal info, address, and purchase history.
- Retrieve consumer information based on search criteria.
- Add new products to the database.
- Uses SQLite for database storage.
- Logs activities using a custom logger.

---

## File Structure
```
python_api_project/
│── lib/
│   │── __init__.py
│   │── add_product.py
│   │── CREATE_DDL.py
│   │── db_connection.py
│   │── dev_consumer.db
│   │── get_consumer.py
│   │── logger.py
│   │── mapping.py
│   │── process_all.py
│   │── utils.py
│
│── logs/
│   │── app.log
│
│── venv/ (virtual environment)
│
│── tests/  
│   │── test_api.py  
│
│── add_product_bp.py
│── app.py
│── consumer_post_bp.py
│── get_consumer_bp.py
│── request.py
│── sql_injection_notes
│── requirements.txt  
```

---

## Installation & Setup
### Prerequisites
- Python 3.7+
- `pip` (Python package manager)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/Rohit-Sandanshiv/python_api.git
   cd python_api
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Mac/Linux
   venv\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Flask app:
   ```sh
   python app.py
   ```
   The API will be available at `http://127.0.0.1:5000/`

---

## API Endpoints
### 1. Insert Consumer Data
**Endpoint:** `POST /consumer/insert`

**Payload:**
```json
{
  "consumers": [
    {
      "GlobalId": "",
      "pii": {
        "FirstName": "Rohit",
        "MiddleName": "Shantaram",
        "LastName": "Sandanshiv",
        "BirthDate": "2000-08-07",
        "Nationality": "INDIA",
        "Gender": "Male",
        "JoinDate": "2022-08-02"
      },
      "social_contact": {
        "Mobile": "9049945969",
        "Email": "rssandanshiv782000@gmail.com",
        "whatsAppID": "9049945969"
      },
      "address": {
        "AddressID": "A1012",
        "AddressLine1": "Wakad",
        "AddressLine2": "Bhumkar Chauk",
        "City": "Pune",
        "State": "Maharashtra",
        "Country": "India",
        "ZipCode": "411057"
      },
      "purchases": [
        {
          "ProductID": "Apple16",
          "InvoiceDate": "2025-03-12",
          "BilledAmount": 60000,
          "quantity": 2
        }
      ]
    }
  ]
}
```
**Response:**
```json
{
  "message": "Insert Successful...",
  "status": "success"
}
```
CURL Command (Windows CMD)
curl -v -H "Content-Type: application/json" -H "TransactionId: transaction_1" -H "ISOCountry: INDIA" --request POST --data "{ \"consumers\": [{ \"GlobalId\": \"\", \"pii\": { \"FirstName\": \"Rohit\", \"MiddleName\": \"Shantaram\", \"LastName\": \"Sandanshiv\", \"BirthDate\": \"2000-08-07\", \"Nationality\": \"INDIA\", \"Gender\": \"Male\", \"JoinDate\": \"2022-08-02\" }, \"social_contact\": { \"Mobile\": \"9049945969\", \"Email\": \"rssandanshiv782000@gmail.com\", \"whatsAppID\": \"9049945969\" }, \"address\": { \"AddressID\": \"A1012\", \"AddressLine1\": \"Wakad\", \"AddressLine2\": \"Bhumkar Chauk\", \"City\": \"Pune\", \"State\": \"Maharashtra\", \"Country\": \"India\", \"ZipCode\": \"411057\" }, \"purchases\": [{ \"ProductID\": \"Apple16\", \"InvoiceDate\": \"2025-03-12\", \"BilledAmount\": 60000, \"quantity\": 2 }] }] }" http://127.0.0.1:5000/consumer/insert


### 2. Retrieve Consumer Data
**Endpoint:** `GET /consumer/get?criteria=FirstName:Rohit,LastName:Sandanshiv`

**Response:**
```json
{
  "message": "Consumer details retrieved successfully",
  "status": "success",
  "sections": {
    "consumer": {
      "GlobalId": "GLOB-C0000001",
      "FirstName": "Rohit",
      "MiddleName": "Shantaram",
      "LastName": "Sandanshiv",
      "BirthDate": "2000-08-07",
      "Nationality": "INDIA",
      "JoinDate": "2022-08-02",
      "is_active": true,
      "is_member": true,
      "is_frequent_buyer": true
    },
    "address": {
      "AddressID": "A1012",
      "AddressLine1": "Wakad",
      "AddressLine2": "Bhumkar Chauk",
      "City": "Pune",
      "State": "Maharashtra",
      "Country": "India",
      "ZipCode": "411057"
    },
    "purchase": [
      {
        "ProductID": "Apple16",
        "InvoiceDate": "2025-03-12",
        "BilledAmount": 60000,
        "quantity": 2
      }
    ],
    "socialContact": {
      "Mobile": "9049945969",
      "Email": "rssandanshiv782000@gmail.com",
      "whatsAppID": "9049945969"
    }
  }
}
```
CURL Command (Windows CMD):
curl -v -H "Content-Type: application/json" -H "TransactionId: transaction_1" -H "ISOCountry: INDIA" --request GET "http://127.0.0.1:5000/consumer/get?criteria=globalId:GLOB-C0000001,email:rssandanshiv782000@gmail.com,Mobile:9049945969"


### 3. Add Product
**Endpoint:** `POST /product/add_product`

**Payload:**
```json
{
  "products": [
    {
      "ProductID": "P001",
      "ProductName": "Laptop",
      "Price": 50000,
      "is_discounted": true,
      "discount": 10
    }
  ]
}
```
**Response:**
```json
{
  "message": "Insert Successful...",
  "status": "success"
}
```
CURL Command (Windows CMD):
curl -v -H "Content-Type: application/json" -H "TransactionId: transaction_1" -H "ISOCountry: INDIA" --request POST --data "{ \"products\": [{ \"ProductID\": \"PROD0004\", \"ProductName\": \"Aloe Vera Gel\", \"Price\": 200, \"is_discounted\": true, \"discount\": 10 }] }" http://127.0.0.1:5000/product/add_product

---

## Future Scope & Improvements
1. **Enhance Security:**
   - Implement authentication using JWT tokens.
   - Protect against SQL injection by using ORM (e.g., SQLAlchemy).

2. **Database Optimization:**
   - Move from SQLite to PostgreSQL or MySQL for better scalability.
   - Add indexing to improve query performance.

3. **Logging & Monitoring:**
   - Improve logging mechanism to track API requests and errors.
   - Integrate with monitoring tools like Prometheus & Grafana.

4. **Error Handling:**
   - Provide more descriptive error messages.
   - Implement retry mechanisms for failed database transactions.

5. **Testing & Deployment:**
   - Write unit tests using `pytest`.
   - Deploy using Docker & Kubernetes.
others:
   * it requires proper catch error mechanism
   * one can do hashing and encrypting for handling PII data
   * input methods or payloads can be improved
   * one can add memberships or loyalty benefits to this api
   * logger is added make sure to use it for further debugging
   * status code and responses can be made better


---


## Contribution
Feel free to contribute by submitting issues or pull requests.

---

## Author
**Rohit Sandanshiv**

---

## License
MIT License

