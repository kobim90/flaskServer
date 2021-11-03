
def input_non_empty(first_name, last_name, id_number):
    if not first_name or not last_name or not id_number:
        return {'message': 'Input must contain value'}


def input_string_check(first_name, last_name, id_number):
    if not isinstance(first_name, str) or not isinstance(last_name, str) or not isinstance(id_number, str):
        return {'message': 'all values must be of String type'}
    if not first_name.isalpha() or not last_name.isalpha():
        return {'message': 'first/last name must be characters only'}
    if not id_number.isdigit():
        return {'message': 'Id number must be numbers only'}
    if len(first_name) > 20 or len(last_name) > 20:
        return {'message': 'first/last name must be below 20 characters'}
    if len(first_name) < 2 or len(last_name) < 2:
        return {'message': 'first/last name must be at least 2 characters'}
    if len(id_number) > 9:
        return {'message': 'Id number must be 9 characters or below'}
