numbers = range(10)
new_dict_for = {}

new_dict_comp = {n:n**2 for n in numbers if n%2 == 0}

print(new_dict_comp)