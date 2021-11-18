
the_shop = {'piekarnia':['chleb', 'pączek', 'bułki'],
             'warzywniak':['marchew', 'seler', 'rukola']}

summ = 0

print('Lista zakupów')
for shop, value in the_shop.items():
    summ += len(value)
    print(f'Idę do {shop.capitalize()} i kupuję tam {[item.capitalize() for item in value]}')
print(f'W sumie kupuję {summ} produktów.')

for i in range(0,101):
    if i % 5 == 0 and not i == 0:
        print(i, i**3)

