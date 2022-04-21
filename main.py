import itertools

first_names = ['Anna', 'Catarina']
middle_names = ['Luisa', 'Maria']

for first, middle in itertools.product(first_names, middle_names):
  print(first, middle)