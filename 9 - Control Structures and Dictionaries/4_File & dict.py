# Als je de tickersymbols opslaat als dict in file:
# def ticker(filename: str):
#     with open(filename, 'r') as file:
#         return eval(file.read())
#
#
# print(ticker('tickersymbols.txt'))


def ticker(filename: str):
    tickers = {}

    with open(filename, 'r') as file:
        for line in file:
            split_line = line.strip().split(':')
            dict_key = split_line[0]
            dict_value = split_line[1]
            tickers[dict_key] = dict_value
        return tickers


# zowel keys als values ophalen met een functie is niet erg SOlID
def get_symbol(filename: str, company_name: str) -> str:
    tickers = ticker(filename)
    if company_name in tickers:
        return tickers[company_name]
    return 'bedrijfsnaam "' + company_name + '" komt niet overeen met een symbol'


def get_company_name(filename: str, symbol: str) -> str:
    tickers = ticker(filename)
    for key, value in tickers.items():
        if value == symbol:
            return key
    return 'symbol "' + symbol + '" komt niet overeen met een bedrijfsnaam'


def prompt_company_name():
    company_name = input('Vul een bedrijfsnaam in: ')
    print(get_symbol('tickersymbols.txt', company_name))


def prompt_symbol():
    symbol = input('Vul een tickersymbol in: ')
    print(get_company_name('tickersymbols.txt', symbol))


prompt = "1: Ik wil een symbool opvragen\n" \
         "2: Ik wil een bedrijfsnaam opvragen"
action = int(input(prompt))

if action == 1:
    prompt_company_name()
if action == 2:
    prompt_symbol()
