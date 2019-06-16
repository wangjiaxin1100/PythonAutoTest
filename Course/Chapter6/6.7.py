daniel_wang = {'first_name':'wang','last_name':'daniel','age':18,'city':'Beijing'}
print(daniel_wang)

print("Daniel's first name is "+ daniel_wang['first_name'] +".")

saven_chen = {'first_name':'chen','last_name':'saven','age':18,'city':'Beijing'}

liquan_zhang = {'first_name':'zhang','last_name':'liquan','age':19,'city':'Beijing'}

peoples = [daniel_wang,saven_chen,liquan_zhang]
for people in peoples:
    print(people)

# 6-9喜欢的地方
favourite_places = {'Kate':'Beijing','Mary':'Honkong','Mike':'Taiwan'}
for name,place in favourite_places.items():
    print(name.title()+"'s favourite place is "+place.title())


favourite_numbers = {
    'mary':[1,2,3],
    'kate':[4,5,6],
    'mike':[7,8,9,],
}

for name,number in favourite_numbers.items():
    print(name.title())
    print(number)


cities = {
    'Beijing':{
        'country':'China',
        'population':'1000000',
        'fact':'hometown',
    },
    'Shanghai':{
        'country': 'China',
        'population': '99999',
        'fact': 'finance',
    },
    'Chengdu':{
        'country': 'China',
        'population': '8888',
        'fact': 'tour',
    }
}

for city,city_info in cities.items():
    print('City Name: '+city.title())
    # print(city_info.items())
    city_country = city_info['country']
    city_population = city_info['population']
    city_fact = city_info['fact']
    print("Country: " + city_country.title())
    print("Population: "+ city_population.title())
    print("Fact: "+ city_fact.title())