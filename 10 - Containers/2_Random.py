import random


def monopolyworp() -> print:
    rolls = 1

    def roll():
        nonlocal rolls
        die1 = random.randint(1, 7)
        die2 = random.randint(1, 7)

        print(str(die1) + " + " + str(die2) + " = " + str(die1 + die2))

        if 3 > rolls:
            if die1 == die2:
                rolls += 1

                roll()
        else:
            print('ga naar de gevangenis')


monopolyworp()
