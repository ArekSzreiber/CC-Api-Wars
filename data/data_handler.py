from data import database_common as dc

@dc.connection_handler
def save_new_user(cursor, username, hashed_password):
    cursor.execute("""
        INSERT INTO public.users (username, password)
        VALUES (%s, %s)
    """, (username, hashed_password)
    )
