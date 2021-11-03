from Models.users import Users
from Middleware.validations import non_empty, valid_string
from flask import request


def get_users_controller():
    try:
        user_list = Users.objects()
        res_list = []
        for user in user_list:
            data = {
                "id": str(user.id),
                "firstName": user.first_name,
                "lastName": user.last_name,
                "idNumber": user.id_number
            }
            res_list.append(data)

        return {'data': res_list}
    except Exception as e:
        return {'message': f'error getting users {repr(e)}'}, 500


@non_empty
@valid_string
def post_user_controller():
    try:
        data = request.get_json()
        first_name = data['firstName']
        last_name = data['lastName']
        id_number = data['idNumber']
        Users(
            first_name=first_name.strip(),
            last_name=last_name.strip(),
            id_number=id_number.strip()
        ).save()
        return {'data': 'user added!'}
    except Exception as e:
        return {'message': f'error posting users {repr(e)}'}, 500
