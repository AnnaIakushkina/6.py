tovar = 'Абрикрос'
cena = 93
ves = 7
cash = 1000
print('Чек')
print(f'{tovar} - {ves}кг - {cena}руб/кг')
print(f'Итого: {cena * ves}руб')
print(f'Внесено: {cash}руб')
print(f'Сдача: {cash - cena * ves}руб')

