def is_empty(user_input):
    if user_input == '':
        return True
    else:
        return False

def is_out_of_range(user_input):
    if 2 < len(user_input) < 21:
        return True
    else:
        return False
