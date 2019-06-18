def make_shirt(size,character):
    print("T-shirt's size is "+ size.title() + " and character is " + character.title() +".")
make_shirt(size='XL',character='Cool')


def make_shirt(new_size='XL',new_character='I love Python'):
    print(new_size +"   " + new_character)

make_shirt()
make_shirt(new_size='L',new_character='OK')

def describe_city(name,country='China'):
    print(name.title() +" is in " + country.title() +".")

describe_city(name='Beijing')
describe_city('shanghai','china')
describe_city('new yourk','america')