
# Password checking
def password_checking(user, password, password_confirmation):
    if password == password_confirmation:
        if len(password) > 8:
            return [True, 'OK']
        else:
            return [False, 'password is too short']
    else:
        return [False, 'confirm password is not the same']
