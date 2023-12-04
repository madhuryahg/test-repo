# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True
    # changing this will either run or not run the message_friends function.
}


def authenticated(fn):
    def wraper(*args, **kwargs):
        if 'valid' in args[0] and args[0]['valid'] is True:
            fn(*args, **kwargs)
        else:
            print('Invalid user')

    return wraper


# code here

@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
