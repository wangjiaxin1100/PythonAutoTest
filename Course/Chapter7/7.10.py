dream_place = "If you could visit one place in the world,where would you go:"
dream_place += "\nContinue the research?(yes/no)"
dream_places = []
while True:
    city = input(dream_place)
    if city == 'no':
        break
    dream_places.append(city)
print(dream_places)