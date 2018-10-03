def is_empty(user_input):
    if user_input == '':
        return True
    else:
        return False

def is_out_of_range(user_input):
    if len(user_input) < 3 or len(user_input) > 20:
        return True
    else:
        return False

def contains_space(user_input):
    if ' ' in user_input:
        return True
    else:
        return False

def does_not_match(user_input, user_verify):
    if user_input != user_verify:
        return True
    else:
        return False
