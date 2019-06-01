Name = 'Eric'
print("Hello "+Name+",would you like to learn some Python today?")

first_name = ' WANG'
last_name = ' JIAXIN '
full_name = first_name+last_name
print(full_name.lower())
print(full_name.upper())
print(full_name.title())

print(full_name.title()+' once said,"A person who never made a mistake never tried anything new."')

famous_person = full_name.title()
message = famous_person + ' once said,"A person who never made a mistake never tried anything new."'
print(message)

print(full_name.title().lstrip())
print(full_name.title().rstrip())
print(full_name.title().strip())