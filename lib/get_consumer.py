from lib.db_connection import get_db_connection
from .mapping import consumer_ddl, social_contact_ddl, address_ddl, purchase_ddl, not_to_include_get_list


def get_consumer(search_params):

    search = [f"{i.split(':')[0]} = '{i.split(':')[1]}'" for i in search_params]
    query_params = " AND ".join(search)
    print(search)
    print(query_params)

    try:
        with get_db_connection() as conn:
            query = f""" SELECT GlobalId, consumer_pk_id from Consumer c INNER JOIN SocialContact s 
            on c.consumer_pk_id = s.ConsumerKey where {query_params}"""
            results = conn.execute(query).fetchall()
            if results:
                global_id, consumer_pk_id = results[0]

            print(global_id)
            print(consumer_pk_id)

        if global_id is not None and consumer_pk_id is not None:

            query = f""" SELECT *  from Consumer where GlobalId = ?"""
            consumer_data = conn.execute(query, (global_id, )).fetchall()
            print(consumer_data)

            query = f""" SELECT *  from Address where consumerKey = ?"""
            address_data = conn.execute(query, (consumer_pk_id, )).fetchall()
            print(address_data)

            query = f""" SELECT *  from SocialContact where consumerKey = ?"""
            social_data = conn.execute(query, (consumer_pk_id, )).fetchall()
            print(social_data)

            query = f""" SELECT *  from Purchase where consumerKey = ?"""
            purchase_data = conn.execute(query, (consumer_pk_id, )).fetchall()
            print(purchase_data)

            consumer_data_dict = {}
            for i in range(0, len(consumer_ddl)):
                if consumer_ddl[i] not in not_to_include_get_list:
                    consumer_data_dict[consumer_ddl[i]] = consumer_data[0][i]

            address_data_dict = {}
            for i in range(0, len(address_ddl)):
                if address_ddl[i] not in not_to_include_get_list:
                    address_data_dict[address_ddl[i]] = address_data[0][i]

            social_data_dict = {}
            for i in range(0, len(social_contact_ddl)):
                if social_contact_ddl[i] not in not_to_include_get_list:
                    social_data_dict[social_contact_ddl[i]] = social_data[0][i]

            purchase_list = []
            for purchase in purchase_data:
                purchase_data_dict = {}
                for i in range(0, len(purchase_ddl)):
                    if purchase_ddl[i] not in not_to_include_get_list:
                        purchase_data_dict[purchase_ddl[i]] = purchase[i]
                purchase_list.append(purchase_data_dict)
            output = {"consumer": consumer_data_dict, "address": address_data_dict, "socialContact": social_data_dict,
                      "purchase": purchase_list}
            return True, output
        else:
            return False, {"message": "User not found", "status": "error"}

    except Exception as e:
        print(e)
    return False, {"message": "User not found", "status": "error"}
