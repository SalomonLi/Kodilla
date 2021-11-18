the_shop = {'piekarnia':['Chleb', 'Pączek', 'Bułki'],
             'warzywniak':['Marchew', 'Seler', 'Rukola']}

summ = 0

print('Lista zakupów')
for shop, value in the_shop.items():
    summ += len(value)
    print(f'Idę do {shop.capitalize()} i kupuję tam {value}')
print(f'W sumie kupuję {summ} produktów.')

#for i in range(0,101,5):
#    print(i, i**5)
