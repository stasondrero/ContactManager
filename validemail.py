'''Підпрограма для перевірки правильності введення користувачем електронної адреси'''
import re

def IsValidEmail(email):
    emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # Назва елетронної пошти
    @                       # Символ - @
    [a-zA-Z0-9.-]+          # Домен нижнього рівня
    (\.[a-zA-Z]{2,4})       # Домен верхнього рівня
    )''', re.VERBOSE)

    email_address = emailRegex.findall(email)
    if len(email_address) != 0:
        return True
    else:
        return False