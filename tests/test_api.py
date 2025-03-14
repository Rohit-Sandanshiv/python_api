import pytest
import requests

# Base URL for API
BASE_URL = "http://127.0.0.1:5000"

# Headers
HEADERS = {
    "Content-Type": "application/json",
    "TransactionId": "transaction_1",
    "ISOCountry": "INDIA"
}

# Sample consumer payload for insertion
consumer_payload_insert = {
    "consumers": [{
        "GlobalId": "",
        "pii": {
            "FirstName": "Rohit9",
            "LastName": "Sandanshiv",
            "MiddleName": "Shantaram",
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
        "purchases": [{
            "ProductID": "Apple16",
            "InvoiceDate": "2025-03-12",
            "BilledAmount": 60000,
            "quantity": 1
        }]
    }]
}

# Sample product payload
product_payload = {
    "products": [{
        "ProductID": "PROD0010",
        "ProductName": "Coffee",
        "Price": 2,
        "is_discounted": False,
        "discount": 0
    }]
}


def test_insert_consumer():
    url = f"{BASE_URL}/consumer/insert"
    response = requests.post(url, json=consumer_payload_insert, headers=HEADERS)

    assert response.status_code == 201  # Expecting HTTP 201 Created
    assert "Insert Successful" in response.json()["message"]


def test_add_product():
    url = f"{BASE_URL}/product/add_product"
    response = requests.post(url, json=product_payload, headers=HEADERS)

    assert response.status_code == 201  # Expecting HTTP 201 Created
    assert "Insert Successful" in response.json()["message"]



def test_get_consumer():
    url = f"{BASE_URL}/consumer/get?criteria=globalId:GLOB-C0000001,email:rssandanshiv782000@gmail.com,Mobile:9049945969"
    response = requests.get(url, headers=HEADERS)

    assert response.status_code == 200  # Expecting HTTP 200 OK
    assert response.json()["message"] == "Consumer details retrieved successfully"
    assert "sections" in response.json()  # Ensure consumer data is returned


def test_get_consumer_invalid():
    url = f"{BASE_URL}/consumer/get?criteria=globalId:INVALID_ID"
    response = requests.get(url, headers=HEADERS)

    assert response.status_code == 404  # Expecting HTTP 404 Not Found
    assert "User not found" in response.json()["message"]

