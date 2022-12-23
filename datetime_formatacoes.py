from datetime import datetime as dt

formatado = '%d/%m/%Y'
new_format = '%y/'
my_data = dt.now()
print(type(my_data))
print(my_data)
my_new_data = dt.strftime(my_data, formatado)
print(my_new_data)

my_str_data = str(my_new_data)
print(type(my_str_data))
print(my_str_data)
my_str_formada = dt.strptime(my_str_data, formatado)
print(my_str_formada)
my_new_data = dt.strftime(my_str_formada, formatado)
print(my_new_data)
