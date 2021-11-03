from flask import request
from Helper.validations_funcs import input_non_empty, input_string_check


# checks if value exists
def non_empty(func):
    def wrapper(*args, **kwargs):
        data = request.get_json()
        first_name = data['firstName']
        last_name = data['lastName']
        id_number = data['idNumber']
        check = input_non_empty(first_name, last_name, id_number)
        return check or func(*args, **kwargs)

    return wrapper


# check if string inputs are valid
def valid_string(func):
    def wrapper(*args, **kwargs):
        data = request.get_json()
        first_name = data['firstName']
        last_name = data['lastName']
        id_number = data['idNumber']
        check = input_string_check(first_name, last_name, id_number)
        return check or func(*args, **kwargs)

    return wrapper
