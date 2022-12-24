ticket_num = int(input('Введите количество билетов '))

total_sum = 0

for user in range(ticket_num):
    age = int(input('Введите возраст '))
    if age < 18: total_sum += 0
    elif 18 <= age < 25: total_sum += 990
    elif age >= 25: total_sum += 1390
if ticket_num <= 3:
    print(f'Сумма к оплате {total_sum}')
if ticket_num > 3:
    print(f'Сумма к оплате со скидкой {total_sum*0.9}')



