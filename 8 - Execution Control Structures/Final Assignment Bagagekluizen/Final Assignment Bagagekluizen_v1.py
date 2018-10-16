def file_len(file_name):
    i = [0]
    with open(file_name) as file:
        for i in enumerate(file, 1):
            pass
    return i[0]


def get_action(prompt: str):
    while True:
        try:
            chosen_action = int(input(prompt))

            if chosen_action in range(1, 5):
                return chosen_action
        except ValueError:
            print('\n' + '\033[1m' + 'Voer aub een heel getal in: ' + '\033[0m' + '\n')


def toon_aantal_kluizen_vrij():
    print('Er zijn nog ' + str(12 - file_len('kluizen.txt')) + ' kluizen vrij.')


def nieuwe_kluis():
    with open('kluizen.txt', 'r') as file:
        lockers_in_use = []
        for line in file:
            lockers_in_use.append(int(line.split('|')[0]))

    locker_number = int(input('Vul het nummer van de kluis in:'))

    if locker_number not in lockers_in_use and 0 < locker_number < 13:
        new_locker_number = locker_number
    else:
        print('deze kluis is al in gebruik')
        return False

    new_locker_password = input('Vul een nieuw wachtwoord in:')

    with open('kluizen.txt', 'a') as file:
        file.write(str(new_locker_number) + '|' + str(new_locker_password) + '\n')


def kluis_openen():
    locker_number = input('Vul uw kluisnummer in:')

    with open('kluizen.txt', 'r') as file:
        for line in file:
            if int(locker_number) == int(line.split('|')[0]):
                locker_password = input('Vul uw wachtwoord in:')
                if locker_password == line.split('|', 1)[1].rstrip():
                    print('Uw kluis wordt nu geopend')

                    return True
                print('Wachtwoord komt niet overeen.')

                return False
    print('Kluis is niet in gebruik.')

    return False


prompt = "1: Ik wil weten hoeveel kluizen nog vrij zijn\n" \
         "2: Ik wil een nieuwe kluis\n" \
         "3: Ik wil even iets uit mijn kluis halen\n" \
         "4: Ik geef mijn kluis terug"
action = get_action(prompt)

if action == 1:
    toon_aantal_kluizen_vrij()
if action == 2:
    nieuwe_kluis()
if action == 3:
    kluis_openen()
if action == 4:
    print('Not implemented')
