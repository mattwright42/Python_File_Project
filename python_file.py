# import the CSV module to parse data
import json
import csv

# create a list of users whose passwords have been compromised
compromised_users = []

# open the file, stored in password_file
with open('passwords.csv') as password_file:
    # pass the object holder to CSV reader for parsing
    password_csv = csv.DictReader(password_file)
    # iterate through each line in the CSV
    for password_row in password_csv:
        # add the username to the compromised_user list
        compromised_users.append(password_row['Username'])

# open a txt file in write mode
with open('compromised_users.txt', 'w') as compromised_user_file:
    # iterate over each user
    for compromised_user in compromised_users:
        # write the username to compromised_user_file
        compromised_user_file.write(compromised_user)

# open a new JSON file
with open('boss_message.json', 'w') as boss_message:
    # create a dictionary object
    boss_message_dict = {'recipient': 'The Boss',
                         'message': 'Mission Success'}
    # write boss_message_dict to boss_message using json.dump()
    json.dump(boss_message_dict, boss_message)

# open new_passwords.csv in write mode
with open('new_passwords.csv', 'w') as new_passwords_obj:
    slash_null_sig = """
 _  _     ___   __  ____
/ )( \   / __) /  \(_  _)
) \/ (  ( (_ \(  O ) )(
\____/   \___/ \__/ (__)
 _  _   __    ___  __ _  ____  ____
/ )( \ / _\  / __)(  / )(  __)(    \
) __ (/    \( (__  )  (  ) _)  ) D (
\_)(_/\_/\_/ \___)(__\_)(____)(____/
        ____  __     __   ____  _  _
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __
(  ( \/ )( \(  )  (  )
/    /) \/ (/ (_/\/ (_/\
\_)__)\____/\____/\____/ 
"""
    new_passwords_obj.write(slash_null_sig)
