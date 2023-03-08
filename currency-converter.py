money = {'baht' : 41.46,
         'dong' : 28079.27,
         'euro' : 1.12,
         'rupiah' : 18278.35,
         'yen' : 162.78}


def converting_currency():
    amount = input("How much would you like to convert? (write number:) £")
    currency_to = input("What currency would you like to convert to? (write word:) ").lower()       # key
    for m in money:
        if currency_to == m:
            converted = amount*money[int(m)]
    return converted


converting_currency()
