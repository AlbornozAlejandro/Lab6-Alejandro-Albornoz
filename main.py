
# This is Alejandro As Encoder

def encoder(password):

    # empty list to fill
    encoded_password = []

    # creates list with int values from string given
    for i in password:

        encoded_password.append(int(i))

    # loops over password to alter object
    for index,i in enumerate(encoded_password):

        encoded_password[index] = i + 3


        if encoded_password[index] > 9:

            # makes sure that its one digit
            encoded_password[index] = encoded_password[index] - 10

    # empty string to add too
    str_encode_password = ''

    # iterates over encoded password and turns into string
    for i in encoded_password:

        str_encode_password += str(i)

    return str_encode_password

#menue loop
while True:

    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

    option = input('Please enter an option:')

    # if-elif chain for menu selection
    if option == '1':
        # takes password
        password = input('Please enter your password to encode:')
        # encodes using encode func
        encoded_password = encoder(password)

        print('Your password has been encoded and stored!')

    elif option == '2':

        pass

    elif option == '3':
        break
