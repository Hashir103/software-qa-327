from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def setup_databases(client):
    '''
    This function is only ran one time to set up the information in our database. I left the code here to show how it works.
    '''
    # initial creating of database and collections
    db = client.database
    customers = db.customers
    restaurants = db.restaurants

    # changing to this schema versus the old one
    default_customer = {
        "account_info": {
            "email": "example@example.com",
            "password": "12345"
        },
        "personal_info": {
            "phone_number": "123-456-7890",
            "home_address": "123 John St."
        },
        "credit_card_info": {
            "card_type": "VISA",
            "card_numbers": "4502123345677689",
            "expiry_date": "09/24",
            "cvv":"102"
        }
    }

    # changing to this schema versus the old one
    default_restaurant = {
        "restaurant_name": "McDonalds",
        "restaurant_info": {
            "owner":"Ronald McDonald",
            "phone_number":"123-456-7890",
            "home_address":"1234. McDonalds St."
        },
        "direct_deposit_info": {
            "card_type": "VISA",
            "card_numbers": "4502123345677689",
            "expiry_date": "09/24",
            "cvv":"102" 
        },
        "order_queue": {
            "current_orders": {},
            "finished_orders": {}
        },
        "menu": {
            "Big Mac": 5.99, 
            "McChicken": 4.99, 
            "McNuggets": 6.99
        }
    }

    customers.insert_one(default_customer)
    restaurants.insert_one(default_restaurant)

def run_cluster():
    '''
    This function is only executed one time to set up the database with the initial parameters from Assignment 2
    '''

    # see notes
    uri = ""

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))


    try:
         # get databases
        db = client.database
        customers = db.customers
        restaurants = db.restaurants

        # first time set up
        # setup_databases(client)

        return [customers, restaurants]

    except Exception as e:
        print(e)


run_cluster()