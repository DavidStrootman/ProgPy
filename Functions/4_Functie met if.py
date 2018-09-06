def new_password(oldpassword, newpassword):
    if newpassword != oldpassword and 5 < len(newpassword):
        return True

    return False


print(new_password('test123', 'test123'))
