word = ''
# Het lijkt mij onlogisch om een break te gebruiken omdat je in de while de woordlengte al af kan vangen.
# while not(4 == len(word)):
while True:
    word = input('Geef een string van 4 letters:')

    if 4 == len(word):
        print('Inlezen van correcte string: ' + word + ' is geslaagd.')
    else:
        print(word + ' heeft ' + str(len(word)) + ' letters.')
        break
