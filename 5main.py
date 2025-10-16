event_code = input('введите код события (ERR, WRN, INF):')
  #обработка системы безопастности
match event_code:
    case 'ERR':
        print('ошибка системы')
    case 'WRN':
        print('предупреждение')
    case 'INF':
        print('информационное сообщение')
    case _:
        print('неизвестный код события')