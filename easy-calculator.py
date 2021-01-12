print('Простой калькулятор')
while True:
    a = float(input('Первое число: '))
    b = float(input('Второе число: '))
    c = input('Что делаем? (+, -, *, /): ')
    if c == '+':
        print('Результат: ', a + b)
    elif c == '-':
        print('Результат: ', a - b)
    elif c == '*':
        print('Результат: ', a * b)
    elif c == '/':
        print('Результат: ', a / b)
    else:
        print('Выбрана неверная операция!')
    s = input('Продолжить? (Да/Нет): ')
    if s == 'Да':
        print()
    elif s == 'Нет':
        print('Программа завершена!')
    else:
         print('Выбрано неверное значение!')
    break

