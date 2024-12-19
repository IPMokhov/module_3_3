def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(8, 'дом', False)
print_params(777, 'диван')
print_params(b = 'стол')
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [888, 'дом', False]
values_dict = {'a': 500, 'b': 'диван', 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [8, 'глаз']
print_params(*values_list_2, 42)
