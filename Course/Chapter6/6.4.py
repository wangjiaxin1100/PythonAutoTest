favourite_lanagues.update({'Kate':'Java','Saven':'C++','Daniel':'Cyuyan','Mary':'Jenkins','Polo':'PHP'})

for name,lanague in favourite_lanagues.items():
    print(name.title() +"'s favorite language is "+
          lanague.title() + ".")