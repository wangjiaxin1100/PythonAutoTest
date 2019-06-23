def make_car(manufacturer,type,**others):
    profile = {}
    profile['manufacturer'] = manufacturer
    profile['type'] = type
    for key ,value in others.items():
        profile[key] = value
    return profile
car = make_car('subaru','outback',
               color='blue',
               tow_package=True)
print(car)