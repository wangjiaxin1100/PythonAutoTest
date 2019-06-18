def city_country(city,country):
    print(city.title() + " , " + country.title())
city_country(city='beijing',country='china')


def make_album(name,album,amount=''):
    if amount:
        album_name = {'name':name,'album':album,'amount':amount}
    else:
        album_name = {'name':name,'album':album}
    return album_name
musician = make_album('miankong','good bye Jack')
print(musician)
musician = make_album('miankong','good bye Jack',amount='5')
print(musician)

while True:
    print("You can any time quit by type q")
    f_name = input("Enter a singer's name:")
    if f_name == 'q':
        break
    f_album = input("Enter a album's name:")
    if f_album == 'q':
        break
    players = make_album(f_name,f_album)
    print(players)