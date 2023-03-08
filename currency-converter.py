money = {'baht' : 41.46,
         'dong' : 28079.27,
         'euro' : 1.12,
         'rupiah' : 18278.35,
         'yen' : 162.78}


def converting_currency():
    amount = input("How much would you like to convert? (write number:) £")
    currency_to = input("What currency would you like to convert to? (write word:) ").lower()       # key
    if currency_to in money:
        converted = int(amount)*money[currency_to]
        print(converted)
    else:
        return "Currency exchange not available!"


converting_currency()
