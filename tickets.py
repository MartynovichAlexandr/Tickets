print('Сколько билетов вы хотете купить? Введите:')
count = int(input())

total = 0
for x in range(count):
	number = x + 1
	print('Введите возраст посетителя №%d' % (number))
	age = int(input())
	price = 0
	if age >= 18:
		price = 990
	if age >= 25:
		price = 1390
	total = total + price

print('Стоимость билетов: %.2f рублей' % (total))

if count > 3 and total > 0:
	disc_total = total * 0.9
	print('Стоимость со скидкой: %.2f рублей' % (disc_total))
