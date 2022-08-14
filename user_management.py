from flask import request, redirect
from db_management import get_db_connection


def add_user(name, email_address, password):
    """
    Adds a new user to the database.
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""INSERT INTO user_data
                              (full_name, email_address, password)
                              VALUES
                              (%s, %s, %s)""", [name, email_address, password])
            connection.commit()


def check_email_not_in_use(email):
    """
    Checks whether a specific email address already exists as a user in the database.
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT u.user_id
                              FROM user_data AS u
                              WHERE u.email_address = %s""", [email])
            user = cursor.fetchone()
            if user is None:
                return True
            else:
                return False


def update_height(height, user_id):
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""UPDATE user_data
                                 SET height = %s
                               WHERE user_id = %s""", [height, user_id])
            connection.commit()


def update_weight(weight, user_id):
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""UPDATE user_data
                                 SET weight = %s
                               WHERE user_id = %s""", [weight, user_id])
            connection.commit()


def get_user_info(user_id):
    """
    Gets details of a specific user based on their user id.
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT u.full_name, u.email_address, u.height, u.weight
                              FROM user_data AS u
                              WHERE u.user_id = %s""", [user_id])
            user = cursor.fetchone()
            return user


def check_login_details(email, password):
    """
    Checks if there is a user id that matches an email and password combination.
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT u.user_id
                              FROM user_data AS u
                              WHERE u.email_address = %s
                              AND u.password = %s""", [email, password])
            user = cursor.fetchone()
            if user is not None:
                return user['user_id']


def requires_sign_in(route_func):
    def signed_in_decorator(*args, **kwargs):
        if request.cookies.get('user_id') is None:
            return redirect('/signin')
        return route_func(*args, **kwargs)
    signed_in_decorator.__name__ = route_func.__name__
    return signed_in_decorator


def requires_sign_out(route_func):
    def signed_out_decorator(*args, **kwargs):
        if request.cookies.get('user_id') is not None:
            return redirect('/profile')
        return route_func(*args, **kwargs)
    signed_out_decorator.__name__ = route_func.__name__
    return signed_out_decorator
