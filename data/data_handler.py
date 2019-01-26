from data import database_common as dc

@dc.connection_handler
def save_new_user(cursor, username, hashed_password):
    cursor.execute("""
        INSERT INTO public.users (username, password)
        VALUES (%s, %s);
    """, (username, hashed_password)
    )


@dc.connection_handler
def get_user_password(cursor, username):
    cursor.execute("""
        SELECT password FROM public.users
        WHERE username = %(username)s;
    """, {'username': username,
          }
    )
    result = cursor.fetchall()
    try:
        return result[0]['password']
    except ValueError:
        return False
    except IndexError:
        return False




@dc.connection_handler
def check_user_existence(cursor, username):
    cursor.execute("""
        SELECT username FROM public.users
        WHERE username = %(username)s;
    """, {'username': username,
          }
    )
    result = cursor.fetchall()
    try:
        return result[0].get('username')
    except IndexError:
        return False
