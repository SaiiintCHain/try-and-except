def add_everything_up(a, b):
    try:
        c = a + b
        print('No mistakes found')
        return c
    except TypeError as exc:
        print(f'Try harder, found <<{exc}>> mistake')
        c = str(a) + str(b)
        return c


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))