table_names = ["Consumer", "SocialContact", "Address", "Purchase", "Product"]
consumer_ddl = ["GlobalId", "consumer_pk_id", "FirstName", "LastName", "JoinDate", "is_active", "is_member",
                "is_frequent_buyer"]
social_contact_ddl = ["social_pk_id", "consumerKey", "Email", "Mobile", "whatsAppID"]
purchase_ddl = ["purchase_pk_id", "consumerKey", "ProductID", "InvoiceDate", "BilledAmount", "quantity"]
product_ddl = ["ProductID", "ProductName", "Price", "is_discounted", "discount"]
address_ddl = ["address_pk_id", "consumerKey", "AddressID", "AddressLine1", "AddressLine2", "City", "State", "Country",
               "ZipCode"]

not_to_include_get_list = ["consumer_pk_id", "social_pk_id", "ConsumerKey", "consumerKey", "purchase_pk_id", "address_pk_id"]