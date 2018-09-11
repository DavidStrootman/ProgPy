from datetime import datetime

with open('hardlopers.txt', 'w+') as file:
    current_date = datetime.today().strftime("%a %d %b %Y")
    current_time = datetime.today().strftime("%T")
    runner = input('Vul naam van hardloper in')

    file.write(current_date + ', ' + current_time + ', ' + runner)