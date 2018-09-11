user_input = eval(input("Geef lijst met minimaal 10 strings: "))
four_length_words = []


for word in user_input:
    if len(word) == 4:
        four_length_words.append(word)


print('De nieuw-gemaakte lijst met alle vier-letter strings is:' + str(four_length_words))
