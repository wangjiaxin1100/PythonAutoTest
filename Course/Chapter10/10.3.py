print("Please enter your name:")
file_name = 'guest.txt'
with open(file_name,'w') as file_object:
    while True:
        name = input("name:")
        if name == 'q':
            break
        file_object.write(name.rstrip()+"\n")