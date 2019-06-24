from collections import OrderedDict

# favourite_lanagues.update({'Kate':'Java','Saven':'C++','Daniel':'Cyuyan','Mary':'Jenkins','Polo':'PHP'})
#
# for name,lanague in favourite_lanagues.items():
#     print(name.title() +"'s favorite language is "+
#           lanague.title() + ".")


language = OrderedDict()
language['Kate'] = 'Java'
language['Saven'] = 'C++'
language['Daniel'] = 'Cyuyan'
language['Mary'] = 'Jenkins'
language['Polo'] = 'PHP'

for name, lanague in language.items():
    print(name.title() + "'s favorite language is " +
          lanague.title() + ".")
