import bcrypt


def hash_password(plain_text):
    hashed_bytes = bcrypt.hashpw(plain_text.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def verify_password(plain_text, hashed_password):
    return bcrypt.checkpw(plain_text.encode('utf-8'), hashed_password.encode('utf-8'))

if __name__ == '__main__':
    # Test the above functions manually
    original_password = 'asdasd'  # From registration form
    print('original_password: ' + original_password)

    hashed_password = hash_password(original_password)  # This shall be saved in the DB
    print('hashed_password: ' + hashed_password)
    print("length of hashed password: " + str(len(hashed_password)))
    user_input_password = 'cos tamasdasdasdadasd'  # From a login form, a mistyped input
    is_matching = verify_password(user_input_password, hashed_password)
    print('is_matching: ' + str(is_matching))

    user_input_password = 'asdasd'  # From a login form, the correct input
    is_matching = verify_password(user_input_password, hashed_password)
    print('is_matching: ' + str(is_matching))

