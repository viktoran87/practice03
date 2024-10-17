def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])


values_list = ['param', 57, [5, 9, 2]]
values_dict = {'a': 48.5, 'b': True, 'c': "dict"}
print_params(*values_list)
print_params(**values_dict)


values_list_2 = ['value', False]
print_params(*values_list_2, 42)
