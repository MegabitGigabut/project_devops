
from db_connector import *

def get_user(user_id):
    user_name = get_record(user_id)
    return user_name

def create_user(user_creation_request):
    user_created = create_record(user_creation_request)
    return user_created

def update_user(user_id):
    sucessfull_update = update_record(user_id)
    print(sucessfull_update)
    return sucessfull_update


def delete_user(user_id):
    deleted_record = delete_record(user_id)
    return deleted_record