# pylint: disable=all

import requests

url_insert_consumer = "http://127.0.0.1:5000/consumer/insert"
url_add_product = "http://127.0.0.1:5000/product/add_product"
url_get_consumer = "http://127.0.0.1:5000/consumer/get?criteria=globalId:GLOB-C0000001,email:rssandanshiv782000@gmail.com,Mobile:9049945969"

consumer_payload_insert = {"consumers": [{ "GlobalId": "", "pii": { "Gender": "Male", "FirstName": "RohitSandanshiv", "LastName": "Sandanshiv", "MiddleName": "Shantaram", "BirthYear": "2000", "BirthMonth": "08", "Birthday": "07", "JoinDate": "2022-08-02", "Nationality": "INDIA" }, "social_contact": { "Mobile": "9049945969", "Email": "rssandanshiv782000@gmail.com", "whatsAppID": "9049945969" }, "address": { "AddressID": "A1012", "AddressLine1": "Wakad", "AddressLine2": "Bhumkar Chauk", "City": "Pune", "State": "Maharashtra", "Country": "India", "ZipCode": "411057" }, "purchases": [{ "ProductID": "Apple16", "InvoiceDate": "2025-03-12", "BilledAmount": "60000", "quantity": "1" }] }]}
consumer_payload_update = {"consumers": [{ "GlobalId": "", "pii": { "Gender": "Male", "FirstName": "RohitSandanshiv", "LastName": "hehe", "MiddleName": "Shantaram", "BirthYear": "2000", "BirthMonth": "08", "Birthday": "07", "JoinDate": "2022-08-02", "Nationality": "INDIA" }, "social_contact": { "Mobile": "9049945969", "Email": "rssandanshiv782000@gmail.com", "whatsAppID": "9049945969" }, "address": { "AddressID": "A1012", "AddressLine1": "Wakad", "AddressLine2": "Bhumkar Chauk", "City": "Pune", "State": "Maharashtra", "Country": "India", "ZipCode": "411057" }, "purchases": [{ "ProductID": "Apple16", "InvoiceDate": "2025-03-12", "BilledAmount": "60000", "quantity": "1" }] }]}
product_payload = {"products": [{"ProductID":"PROD0005", "ProductName":"Coffe", "Price":"2", "is_discounted":0, "discount":"0"}]}

headers = {"Content-Type": "application/json", "TransactionId": "transaction_1", "ISOCountry": "INDIA"}

print("Inserting a consumer...")
response = requests.post(url_insert_consumer, json=consumer_payload_insert, headers=headers)
print(response.content)
print(response.status_code)

print("Updating a consumer...")
response = requests.post(url_insert_consumer, json=consumer_payload_update, headers=headers)
print(response.content)
print(response.status_code)

print("Inserting a Product...")
response = requests.post(url_add_product, json=product_payload, headers=headers)
print(response.content)
print(response.status_code)

print("Fetching a Consumer...")
response = requests.get(url_get_consumer, headers=headers)
print(response.content)
print(response.status_code)

# Alternatively we can run these requests in cmd :---
# curl -v -H "Content-Type: application/json" -H "TransactionId: transation_1" -H "ISOCountry: INDIA" --request POST --data "{ \"consumers\": [{ \"GlobalId\": \"\", \"pii\": { \"Gender\": \"Male\", \"FirstName\": \"Rohit\", \"LastName\": \"Sandanshiv\", \"MiddleName\": \"Shantaram\", \"BirthYear\": \"2000\", \"BirthMonth\": \"08\", \"Birthday\": \"07\", \"JoinDate\": \"2022-08-02\", \"Nationality\": \"INDIA\" }, \"social_contact\": { \"Mobile\": \"9049945969\", \"Email\": \"rssandanshiv782000@gmail.com\", \"whatsAppID\": \"9049945969\" }, \"address\": { \"AddressID\": \"A1012\", \"AddressLine1\": \"Wakad\", \"AddressLine2\": \"Bhumkar Chauk\", \"City\": \"Pune\", \"State\": \"Maharashtra\", \"Country\": \"India\", \"ZipCode\": \"411057\" }, \"purchases\": [{ \"ProductID\": \"Apple16\", \"InvoiceDate\": \"2025-03-12\", \"BilledAmount\": \"60000\", \"quantity\": \"1\" }] }] }" http://127.0.0.1:5000/consumer/insert
#
# curl -v -H "Content-Type: application/json" -H "TransactionId: transation_1" -H "ISOCountry: INDIA" --request POST --data "{\"products\": [{\"ProductID\":\"PROD0004\", \"ProductName\":\"Alloe vera gel\", \"Price\":\"200\", \"is_discounted\":1, \"discount\":\"10\"}]}" http://127.0.0.1:5000/product/add_product
#
# curl -v -H "Content-Type: application/json" -H "TransactionId: transation_1" -H "ISOCountry: INDIA" --request GET  http://127.0.0.1:5000/consumer/get?criteria=globalId:GLOB-C0000001,email:rssandanshiv782000@gmail.com,Mobile:9049945969