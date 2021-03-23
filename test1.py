# porte feuille
wallet = 2000
computer_price = 1200

# prix de l'ordinateur est inferieur à 1000 dollars
if computer_price <= 1000:
    print("L'achat est possible")
    wallet -= computer_price
else:
    print("L'achat est impossible, vous n'avez que {}" .format(wallet))
