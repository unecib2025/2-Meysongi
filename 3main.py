danger_level=int(input('введите уровень угрозы 1-100: '))
if 1<danger_level<30:
    print('низкий уровень угрозы')
elif 30<danger_level<70:
    print('средний уровень угрозы')
else:
    print('Критический уровень угрозы')