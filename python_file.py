# import the CSV module to parse data
import csv

# create a list of users whose passwords have been compromised
compromised_users = []

# open the file, stored in password_file
with open('passwords.csv') as password_file:
    password_csv = csv.DictReader(password_file)
    for row in password_csv:
        password_row = print(password_row['Username'])
