from datetime import datetime
import csv

surname = None
current_date = datetime.today().strftime("%a %d %b %Y")
current_time = datetime.today().strftime("%H:%M")
formatted_date = current_date + ' at ' + current_time

with open('login.csv', 'w', newline='') as file:
    file_writer = csv.writer(file, delimiter=';',)

    while not surname == 'einde':
        surname = input('Voer uw achternaam in: ')

        if surname != 'einde':
            initials = input('Voer de voorletters van uw naam in: ')
            date_of_birth = input('Voer uw geboortedatum in: ')
            email_address = input('Voer uw e-mailadres in: ')

            file_writer.writerow([formatted_date] + [initials, surname, date_of_birth, email_address])
